# Generated by Django 4.2.4 on 2023-09-03 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ballinat', '0011_slide_title_part1_slide_title_part2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='title_part1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='slide',
            name='title_part2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='slide',
            name='title_part3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='slide',
            name='title_part4',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
