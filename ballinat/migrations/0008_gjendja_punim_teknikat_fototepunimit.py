# Generated by Django 4.2.4 on 2023-09-02 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ballinat', '0007_rename_slug_of_service_slide_blog_slug_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gjendja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gjendja', models.CharField(blank=True, max_length=40, null=True)),
                ('ngjyra', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Punim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='punim_image/')),
                ('title', models.CharField(blank=True, max_length=40, null=True)),
                ('pershkrimi', models.CharField(blank=True, max_length=40, null=True)),
                ('date_created', models.DateField()),
                ('active_in_footer', models.IntegerField(blank=True, choices=[(0, 'no'), (1, 'yes')], null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('slug_blog', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teknikat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teknika', models.CharField(blank=True, max_length=40, null=True)),
                ('pershkrimi', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FototEPunimit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='punim_image/')),
                ('punim', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ballinat.punim')),
            ],
        ),
    ]
