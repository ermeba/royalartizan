# Generated by Django 4.2.4 on 2023-09-03 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ballinat', '0010_afterslides_numrat_aboutus_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='title_part1',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='title_part2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='title_part3',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='title_part4',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
