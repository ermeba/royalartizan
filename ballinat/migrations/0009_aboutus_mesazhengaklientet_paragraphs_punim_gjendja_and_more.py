# Generated by Django 4.2.4 on 2023-09-03 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ballinat', '0008_gjendja_punim_teknikat_fototepunimit'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='about_us_image/')),
                ('since', models.CharField(blank=True, max_length=300, null=True)),
                ('yars_of_experience', models.CharField(blank=True, max_length=10, null=True)),
                ('experience_sentecne', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MesazheNgaKlientet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emri_mbiemri', models.CharField(blank=True, max_length=50, null=True)),
                ('profesioni', models.CharField(blank=True, max_length=50, null=True)),
                ('mesazhi', models.CharField(blank=True, max_length=120, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='about_us_image/')),
            ],
        ),
        migrations.CreateModel(
            name='Paragraphs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='punim',
            name='gjendja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ballinat.gjendja'),
        ),
        migrations.AddField(
            model_name='punim',
            name='teknikat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ballinat.teknikat'),
        ),
        migrations.AddField(
            model_name='teknikat',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='teknika_image/'),
        ),
    ]
