# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 17:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import spectator.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConcertRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True, help_text='The time this item was created in the database.')),
                ('time_modified', models.DateTimeField(auto_now=True, help_text='The time this item was last saved to the database.')),
                ('role_name', models.CharField(blank=True, help_text="e.g. 'Headliner', 'Support', 'Editor', 'Illustrator', 'Director', etc. Optional.", max_length=50)),
                ('role_order', models.PositiveSmallIntegerField(default=1, help_text='The order in which the Creators will be listed.')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concert_roles', to='core.Creator')),
            ],
            options={
                'ordering': ('role_order', 'role_name'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True, help_text='The time this item was created in the database.')),
                ('time_modified', models.DateTimeField(auto_now=True, help_text='The time this item was last saved to the database.')),
                ('date', models.DateField(null=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='MiscEventRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True, help_text='The time this item was created in the database.')),
                ('time_modified', models.DateTimeField(auto_now=True, help_text='The time this item was last saved to the database.')),
                ('role_name', models.CharField(blank=True, help_text="e.g. 'Headliner', 'Support', 'Editor', 'Illustrator', 'Director', etc. Optional.", max_length=50)),
                ('role_order', models.PositiveSmallIntegerField(default=1, help_text='The order in which the Creators will be listed.')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='miscevent_roles', to='core.Creator')),
            ],
            options={
                'ordering': ('role_order', 'role_name'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True, help_text='The time this item was created in the database.')),
                ('time_modified', models.DateTimeField(auto_now=True, help_text='The time this item was last saved to the database.')),
                ('title', models.CharField(max_length=255)),
                ('title_sort', spectator.core.fields.NaturalSortField('title', db_index=True, default='', editable=False, help_text="e.g. 'haine, la' or 'unbelievable truth, the'.", max_length=255)),
                ('imdb_id', models.CharField(blank=True, help_text="Starts with 'tt', e.g. 'tt0100842'.", max_length=12, validators=[django.core.validators.RegexValidator(code='invalid_imdb_id', message='IMDb ID should be like "tt1234567"', regex='^tt\\d{7,10}$')], verbose_name='IMDb ID')),
                ('year', models.PositiveSmallIntegerField(blank=True, default=None, help_text='Year of release.', null=True)),
            ],
            options={
                'ordering': ('title_sort',),
            },
        ),
        migrations.CreateModel(
            name='MovieRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True, help_text='The time this item was created in the database.')),
                ('time_modified', models.DateTimeField(auto_now=True, help_text='The time this item was last saved to the database.')),
                ('role_name', models.CharField(blank=True, help_text="e.g. 'Headliner', 'Support', 'Editor', 'Illustrator', 'Director', etc. Optional.", max_length=50)),
                ('role_order', models.PositiveSmallIntegerField(default=1, help_text='The order in which the Creators will be listed.')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_roles', to='core.Creator')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='events.Movie')),
            ],
            options={
                'ordering': ('role_order', 'role_name'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True, help_text='The time this item was created in the database.')),
                ('time_modified', models.DateTimeField(auto_now=True, help_text='The time this item was last saved to the database.')),
                ('title', models.CharField(max_length=255)),
                ('title_sort', spectator.core.fields.NaturalSortField('title', db_index=True, default='', editable=False, help_text="e.g. 'big play, a' or 'biggest play, the'.", max_length=255)),
            ],
            options={
                'ordering': ('title_sort',),
            },
        ),
        migrations.CreateModel(
            name='PlayProduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True, help_text='The time this item was created in the database.')),
                ('time_modified', models.DateTimeField(auto_now=True, help_text='The time this item was last saved to the database.')),
                ('title', models.CharField(blank=True, help_text='Optional title of this production of the play.', max_length=255)),
            ],
            options={
                'ordering': ('play__title',),
            },
        ),
        migrations.CreateModel(
            name='PlayProductionRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True, help_text='The time this item was created in the database.')),
                ('time_modified', models.DateTimeField(auto_now=True, help_text='The time this item was last saved to the database.')),
                ('role_name', models.CharField(blank=True, help_text="e.g. 'Headliner', 'Support', 'Editor', 'Illustrator', 'Director', etc. Optional.", max_length=50)),
                ('role_order', models.PositiveSmallIntegerField(default=1, help_text='The order in which the Creators will be listed.')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='play_production_roles', to='core.Creator')),
                ('production', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='events.PlayProduction')),
            ],
            options={
                'ordering': ('role_order', 'role_name'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlayRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True, help_text='The time this item was created in the database.')),
                ('time_modified', models.DateTimeField(auto_now=True, help_text='The time this item was last saved to the database.')),
                ('role_name', models.CharField(blank=True, help_text="e.g. 'Headliner', 'Support', 'Editor', 'Illustrator', 'Director', etc. Optional.", max_length=50)),
                ('role_order', models.PositiveSmallIntegerField(default=1, help_text='The order in which the Creators will be listed.')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='play_roles', to='core.Creator')),
                ('play', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='events.Play')),
            ],
            options={
                'ordering': ('role_order', 'role_name'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True, help_text='The time this item was created in the database.')),
                ('time_modified', models.DateTimeField(auto_now=True, help_text='The time this item was last saved to the database.')),
                ('name', models.CharField(max_length=255)),
                ('name_sort', spectator.core.fields.NaturalSortField('name', db_index=True, default='', editable=False, help_text="e.g. 'venue, a' or 'biggest venue, the'.", max_length=255)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('country', models.CharField(blank=True, choices=[('AF', 'Afghanistan'), ('AX', 'Åland Islands'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antigua and Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia (Plurinational State of)'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BA', 'Bosnia and Herzegovina'), ('BW', 'Botswana'), ('BV', 'Bouvet Island'), ('BR', 'Brazil'), ('IO', 'British Indian Ocean Territory'), ('BN', 'Brunei Darussalam'), ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('CV', 'Cabo Verde'), ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('KY', 'Cayman Islands'), ('CF', 'Central African Republic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CX', 'Christmas Island'), ('CC', 'Cocos (Keeling) Islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CD', 'Congo (the Democratic Republic of the)'), ('CG', 'Congo'), ('CK', 'Cook Islands'), ('CR', 'Costa Rica'), ('CI', "Côte d'Ivoire"), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CW', 'Curaçao'), ('CY', 'Cyprus'), ('CZ', 'Czechia'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FK', 'Falkland Islands  [Malvinas]'), ('FO', 'Faroe Islands'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GF', 'French Guiana'), ('PF', 'French Polynesia'), ('TF', 'French Southern Territories'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'), ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GG', 'Guernsey'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HM', 'Heard Island and McDonald Islands'), ('VA', 'Holy See'), ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran (Islamic Republic of)'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IM', 'Isle of Man'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JE', 'Jersey'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KP', "Korea (the Democratic People's Republic of)"), ('KR', 'Korea (the Republic of)'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', "Lao People's Democratic Republic"), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macao'), ('MK', 'Macedonia (the former Yugoslav Republic of)'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesia (Federated States of)'), ('MD', 'Moldova (the Republic of)'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('NC', 'New Caledonia'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'), ('NF', 'Norfolk Island'), ('MP', 'Northern Mariana Islands'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestine, State of'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RE', 'Réunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('BL', 'Saint Barthélemy'), ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('MF', 'Saint Martin (French part)'), ('PM', 'Saint Pierre and Miquelon'), ('VC', 'Saint Vincent and the Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SX', 'Sint Maarten (Dutch part)'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('GS', 'South Georgia and the South Sandwich Islands'), ('SS', 'South Sudan'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SJ', 'Svalbard and Jan Mayen'), ('SZ', 'Swaziland'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syrian Arab Republic'), ('TW', 'Taiwan (Province of China)'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania, United Republic of'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'), ('TG', 'Togo'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TC', 'Turks and Caicos Islands'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'UK'), ('UM', 'United States Minor Outlying Islands'), ('US', 'USA'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VE', 'Venezuela (Bolivarian Republic of)'), ('VN', 'Viet Nam'), ('VG', 'Virgin Islands (British)'), ('VI', 'Virgin Islands (U.S.)'), ('WF', 'Wallis and Futuna'), ('EH', 'Western Sahara'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], help_text="The ISO 3166-1 alpha-2 code, e.g. 'GB' or 'FR'", max_length=2)),
            ],
            options={
                'ordering': ['name_sort'],
            },
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Event')),
                ('title', models.CharField(blank=True, help_text="Optional. e.g., 'Indietracks 2017', 'Radio 1 Roadshow'.", max_length=255)),
                ('title_sort', spectator.core.fields.NaturalSortField('title_to_sort', db_index=True, default='', editable=False, help_text="e.g. 'reading festival, the' or 'drifters, the'.", max_length=255)),
            ],
            options={
                'ordering': ('title_sort',),
            },
            bases=('events.event',),
        ),
        migrations.CreateModel(
            name='MiscEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Event')),
                ('title', models.CharField(blank=True, help_text="Optional. e.g., 'A Great Event'.", max_length=255)),
                ('title_sort', spectator.core.fields.NaturalSortField('title_to_sort', db_index=True, default='', editable=False, help_text="e.g. 'great event, a'.", max_length=255)),
            ],
            options={
                'ordering': ('title_sort',),
            },
            bases=('events.event',),
        ),
        migrations.CreateModel(
            name='MovieEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=('events.event',),
        ),
        migrations.CreateModel(
            name='PlayProductionEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=('events.event',),
        ),
        migrations.AddField(
            model_name='playproduction',
            name='creators',
            field=models.ManyToManyField(help_text='The director, actors, etc. in this production.', related_name='play_productions', through='events.PlayProductionRole', to='core.Creator'),
        ),
        migrations.AddField(
            model_name='playproduction',
            name='play',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Play'),
        ),
        migrations.AddField(
            model_name='play',
            name='creators',
            field=models.ManyToManyField(related_name='plays', through='events.PlayRole', to='core.Creator'),
        ),
        migrations.AddField(
            model_name='movie',
            name='creators',
            field=models.ManyToManyField(related_name='movies', through='events.MovieRole', to='core.Creator'),
        ),
        migrations.AddField(
            model_name='event',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_events.event_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Venue'),
        ),
        migrations.AddField(
            model_name='playproductionevent',
            name='production',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.PlayProduction'),
        ),
        migrations.AddField(
            model_name='movieevent',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Movie'),
        ),
        migrations.AddField(
            model_name='misceventrole',
            name='miscevent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='events.MiscEvent'),
        ),
        migrations.AddField(
            model_name='miscevent',
            name='creators',
            field=models.ManyToManyField(related_name='miscevents', through='events.MiscEventRole', to='core.Creator'),
        ),
        migrations.AddField(
            model_name='concertrole',
            name='concert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='events.Concert'),
        ),
        migrations.AddField(
            model_name='concert',
            name='creators',
            field=models.ManyToManyField(related_name='concerts', through='events.ConcertRole', to='core.Creator'),
        ),
    ]