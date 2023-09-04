# Generated by Django 4.2.4 on 2023-09-03 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ballinat', '0009_aboutus_mesazhengaklientet_paragraphs_punim_gjendja_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AfterSlides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=30, null=True)),
                ('pershkirmi', models.CharField(blank=True, max_length=93, null=True)),
                ('ikona', models.CharField(blank=True, max_length=20, null=True)),
                ('active', models.IntegerField(blank=True, choices=[(0, 'NO'), (1, 'YES')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Numrat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numri', models.CharField(blank=True, max_length=30, null=True)),
                ('pershkirmi', models.CharField(blank=True, max_length=93, null=True)),
                ('active', models.IntegerField(blank=True, choices=[(0, 'NO'), (1, 'YES')], null=True)),
            ],
        ),
        migrations.AddField(
            model_name='aboutus',
            name='active',
            field=models.IntegerField(blank=True, choices=[(0, 'NO'), (1, 'YES')], null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='active',
            field=models.IntegerField(blank=True, choices=[(0, 'NO'), (1, 'YES')], null=True),
        ),
    ]
