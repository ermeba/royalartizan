# Generated by Django 4.2.4 on 2023-09-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ballinat', '0018_punim_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='short_summery',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
