from django.conf import settings
from django.db import models
try:
    # Django >= 1.10
    from django.urls import reverse
except ImportError:
    # Django < 1.10
    from django.core.urlresolvers import reverse

from . import BaseRole, Creator, TimeStampedModelMixin
from .. import managers


class PublicationSeries(TimeStampedModelMixin, models.Model):
    """
    A way to group `Publication`s into series.
    """
    title = models.CharField(null=False, blank=False, max_length=255,
            help_text="e.g. 'The London Review of Books'.")
    url = models.URLField(null=False, blank=True, max_length=255,
            verbose_name='URL', help_text="e.g. 'https://www.lrb.co.uk/'.")

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Publication series'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('spectator:publicationseries_detail',
                                                        kwargs={'pk':self.pk})


class PublicationRole(BaseRole):
    """
    Linking a creator to a Publication, optionally via their role (e.g.
    'Author', 'Editor', etc.)
    """
    creator = models.ForeignKey('Creator', blank=False,
                    on_delete=models.CASCADE, related_name='publication_roles')

    publication = models.ForeignKey('Publication', on_delete=models.CASCADE,
                                                        related_name='roles')


class Publication(TimeStampedModelMixin, models.Model):
    """
    Get a Publication's creators:

        publication = Publication.objects.get(pk=1)

        # Just the creators:
        for creator in publication.creators.all():
            print(creator.name)

        # Include their roles:
        for role in publication.roles.all():
            print(role.publication, role.creator, role.role_name)

    Get its readings:

        for reading in publication.reading_set.all():
            print(reading.start_date, reading.end_date)
    """

    KIND_CHOICES = (
        ('book', 'Book'),
        ('periodical', 'Periodical'),
    )

    title = models.CharField(null=False, blank=False, max_length=255,
            help_text="e.g. 'Aurora' or 'Vol. 39 No. 4, 16 February 2017'.")
    series = models.ForeignKey('PublicationSeries', blank=True, null=True,
                                                    on_delete=models.SET_NULL)
    kind = models.CharField(max_length=20, choices=KIND_CHOICES,
                                                        default='book')
    official_url = models.URLField(null=False, blank=True, max_length=255,
            verbose_name='Official URL',
            help_text="Official URL for this book/issue.")
    isbn_uk = models.CharField(null=False, blank=True, max_length=20,
            verbose_name='UK ISBN', help_text="e.g. '0356500489'.")
    isbn_us = models.CharField(null=False, blank=True, max_length=20,
            verbose_name='US ISBN', help_text="e.g. '0316098094'.")
    notes_url = models.URLField(null=False, blank=True, max_length=255,
            verbose_name='Notes URL', help_text="URL of your notes/review.")

    creators = models.ManyToManyField(Creator, through='PublicationRole',
                                                related_name='publications')

    objects = models.Manager()
    # Publications that are currently being read:
    in_progress_objects = managers.InProgressPublicationsManager()
    # Publications that haven't been started (have no Readings):
    unread_objects = managers.UnreadPublicationsManager()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('spectator:publication_detail', kwargs={'pk':self.pk})

    @property
    def amazon_uk_url(self):
        url = ''
        if self.isbn_uk:
            url = 'https://www.amazon.co.uk/gp/product/{}/'.format(self.isbn_uk)
            if hasattr(settings, 'SPECTATOR_AMAZON') and 'uk' in settings.SPECTATOR_AMAZON:
                url = '{}?tag={}'.format(url, settings.SPECTATOR_AMAZON['uk'])
        return url

    @property
    def amazon_us_url(self):
        url = ''
        if self.isbn_us:
            url = 'https://www.amazon.com/dp/{}/'.format(self.isbn_us)
            if hasattr(settings, 'SPECTATOR_AMAZON') and 'us' in settings.SPECTATOR_AMAZON:
                url = '{}?tag={}'.format(url, settings.SPECTATOR_AMAZON['us'])
        return url

    @property
    def amazon_urls(self):
        urls = []
        if self.isbn_uk:
            urls.append({
                'url': self.amazon_uk_url,
                'name': 'Amazon.co.uk',
                'country': 'UK',
            })
        if self.isbn_us:
            urls.append({
                'url': self.amazon_us_url,
                'name': 'Amazon.com',
                'country': 'USA',
            })
        return urls

    @property
    def has_urls(self):
        "Handy for templates."
        if self.isbn_uk or self.isbn_us or self.official_url or self.notes_url:
            return True
        else:
            return False


class Reading(TimeStampedModelMixin, models.Model):
    """
    A period when a Publication was read.
    """
    # Via https://www.flickr.com/services/api/misc.dates.html
    DATE_GRANULARITIES = (
        # (0, 'Y-m-d H:i:s'),
        (3, 'Y-m-d'),
        (4, 'Y-m'),
        (6, 'Y'),
        # (8, 'Circa...'),
    )

    publication = models.ForeignKey('Publication', null=False, blank=False)

    start_date = models.DateField(null=True, blank=True)
    start_granularity = models.PositiveSmallIntegerField(null=False,
            blank=False, default=3, choices=DATE_GRANULARITIES)
    end_date = models.DateField(null=True, blank=True)
    end_granularity = models.PositiveSmallIntegerField(null=False,
            blank=False, default=3, choices=DATE_GRANULARITIES)
    is_finished = models.BooleanField(default=False,
            help_text="Did you finish the publication?")

    objects = managers.EndDateDescendingReadingsManager()
    objects_asc = managers.EndDateAscendingReadingsManager()

    class Meta:
        get_latest_by = 'end_date'

    def __str__(self):
        return '{} ({} to {})'.format(
                            self.publication, self.start_date, self.end_date)

