# Generated by Django 4.2.4 on 2023-09-02 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ballinat', '0003_alter_contacts_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesSlide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='slides_images/')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('type_of_page', models.IntegerField(blank=True, choices=[(0, 'Home'), (1, 'About'), (2, 'Gallery'), (3, 'Blog'), (41, 'Contacts')], null=True)),
                ('active_in_footer', models.IntegerField(blank=True, choices=[(0, 'no'), (1, 'yes')], null=True)),
            ],
        ),
    ]
