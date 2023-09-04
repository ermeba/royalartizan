# Generated by Django 4.1 on 2023-09-01 14:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=300, null=True)),
                ('email', models.CharField(blank=True, max_length=300, null=True)),
                ('map_link', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('location', models.CharField(blank=True, max_length=300, null=True)),
                ('message', models.CharField(blank=True, max_length=300, null=True)),
                ('company_name', models.CharField(blank=True, max_length=300, null=True)),
                ('company_type', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfSocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_media', models.IntegerField(blank=True, choices=[(0, 'instagram'), (1, 'facebook'), (2, 'linkedin'), (3, 'twitter'), (4, 'telegraf')], null=True)),
                ('icon_of_social_media', models.ImageField(blank=True, null=True, upload_to='social_media_icon/')),
                ('link_of_social_media', models.CharField(blank=True, max_length=700, null=True)),
            ],
        ),
    ]
