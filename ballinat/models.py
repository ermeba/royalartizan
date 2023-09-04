from django.core.validators import URLValidator
from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.


"""
==================================================SLIDES ===============================================================
"""

slide_choices = ((0, 'Home'), (1, 'About'), (2, 'Gallery'), (3, 'Blog'), (41, 'Contacts'))
active_footer = ((0, 'no'), (1, 'yes'))
active_number_choices = ((0, 'NO'), (1, 'YES'))


class Slide(models.Model):
    image = models.ImageField(upload_to='slides_images/', blank=True, null=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    title_part1 = models.CharField(max_length=20, null=True, blank=True)
    title_part2 = models.CharField(max_length=20, null=True, blank=True)
    title_part3 = models.CharField(max_length=20, null=True, blank=True)
    title_part4 = models.CharField(max_length=20, null=True, blank=True)
    type_of_page = models.IntegerField(choices=slide_choices, null=True, blank=True)
    active_in_footer = models.IntegerField(choices=active_footer, null=True, blank=True)
    active = models.IntegerField(choices=active_number_choices, null=True, blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="100" height="100" />'.format(self.image.url))
        else:
            return '(No image)'


"""
==================================================AFTER SLIDES==========================================================
"""


class AfterSlides(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    pershkirmi = models.CharField(max_length=93, null=True, blank=True)
    ikona = models.CharField(max_length=20, null=True, blank=True)
    active = models.IntegerField(choices=active_number_choices, null=True, blank=True)
    prapavija = models.CharField(max_length=10, null=True, blank=True)


"""
==================================================ABOUT US==============================================================
"""


class AboutUs(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to='about_us_image/', blank=True, null=True)
    since = models.CharField(max_length=300, null=True, blank=True)
    yars_of_experience = models.CharField(max_length=10, null=True, blank=True)
    experience_sentecne = models.CharField(max_length=300, null=True, blank=True)
    active = models.IntegerField(choices=active_number_choices, null=True, blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="100" height="100" />'.format(self.image.url))
        else:
            return '(No image)'


class Paragraphs(models.Model):
    paragraph = models.CharField(max_length=2000, null=True, blank=True)
    about = models.ForeignKey(AboutUs, on_delete=models.CASCADE, blank=True, null=True)


"""
==================================================NUMRAT================================================================
"""


class Numrat(models.Model):
    numri = models.CharField(max_length=30, null=True, blank=True)
    pershkirmi = models.CharField(max_length=93, null=True, blank=True)
    active = models.IntegerField(choices=active_number_choices, null=True, blank=True)


"""
==================================================TESTIMONIAL===========================================================
"""


class MesazheNgaKlientet(models.Model):
    emri_mbiemri = models.CharField(max_length=50, null=True, blank=True)
    profesioni = models.CharField(max_length=50, null=True, blank=True)
    mesazhi = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(upload_to='about_us_image/', blank=True, null=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{0}" width="100" height="100" />'.format(self.image.url))
        else:
            return '(No image)'

"""
==================================================BLOG==================================================================
"""


class Blog(models.Model):
    main_image = models.ImageField(upload_to='blog_image/', blank=True, null=True)
    title = models.CharField(max_length=40, null=True, blank=True)
    date_created = models.DateField()
    short_summery = models.CharField(max_length=100, null=True, blank=True)
    active_in_footer = models.IntegerField(choices=active_footer, null=True, blank=True)
    slug_blog = models.SlugField(unique=True, null=True, blank=True)

    def image_preview(self):
        if self.main_image:
            return mark_safe('<img src="{0}" width="100" height="100" />'.format(self.main_image.url))
        else:
            return '(No image)'


class Subtitle(models.Model):
    subtitle = models.CharField(max_length=300, null=True, blank=True)
    subimage = models.ImageField(upload_to='activity_image/', blank=True, null=True)
    title = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True)


class Paragraph(models.Model):
    text = models.CharField(max_length=1000, null=True, blank=True)
    subtitle = models.ForeignKey(Subtitle, on_delete=models.CASCADE, blank=True, null=True)


"""
==================================================GJENDJA===============================================================
"""


class Gjendja(models.Model):
    gjendja = models.CharField(max_length=40, null=True, blank=True)
    ngjyra = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.gjendja

"""
==================================================TEKNIKAT==============================================================
"""


class Teknikat(models.Model):
    teknika = models.CharField(max_length=40, null=True, blank=True)
    foto = models.ImageField(upload_to='teknika_image/', blank=True, null=True)
    pershkrimi = models.CharField(max_length=40, null=True, blank=True)
    active = models.IntegerField(choices=active_number_choices, null=True, blank=True)

    def image_preview(self):
        if self.foto:
            return mark_safe('<img src="{0}" width="100" height="100" />'.format(self.foto.url))
        else:
            return '(No image)'
    def __str__(self):
        return self.teknika


"""
==================================================PUNIMET===============================================================
"""


class Punim(models.Model):
    main_image = models.ImageField(upload_to='punim_image/', blank=True, null=True)
    title = models.CharField(max_length=40, null=True, blank=True)
    pershkrimi = models.CharField(max_length=40, null=True, blank=True)
    date_created = models.DateField()
    active_in_footer = models.IntegerField(choices=active_footer, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    teknikat = models.ForeignKey(Teknikat, on_delete=models.CASCADE, blank=True, null=True)
    gjendja = models.ForeignKey(Gjendja, on_delete=models.CASCADE, blank=True, null=True)
    slug_blog = models.SlugField(unique=True, null=True, blank=True)

    def image_preview(self):
        if self.main_image:
            return mark_safe('<img src="{0}" width="100" height="100" />'.format(self.main_image.url))
        else:
            return '(No image)'

class FototEPunimit(models.Model):
    foto = models.ImageField(upload_to='punim_image/', blank=True, null=True)
    punim = models.ForeignKey(Punim, on_delete=models.CASCADE, blank=True, null=True)


"""
==================================================CONTACT INFO==========================================================
"""


class Contacts(models.Model):
    phone_number = models.CharField(max_length=300, null=True, blank=True)
    email = models.CharField(max_length=300, null=True, blank=True)
    map_link = models.TextField(validators=[URLValidator()], null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    location = models.CharField(max_length=300, null=True, blank=True)
    message = models.CharField(max_length=300, null=True, blank=True)
    company_name = models.CharField(max_length=300, null=True, blank=True)
    company_type = models.CharField(max_length=300, null=True, blank=True)
    website = models.CharField(max_length=300, null=True, blank=True)
    active = models.IntegerField(choices=active_number_choices, null=True, blank=True)


social_medias = ((0, 'instagram'), (1, 'facebook'), (2, 'linkedin'), (3, 'twitter'), (4, 'telegraf'))


class TypeOfSocialMedia(models.Model):
    name_of_media = models.IntegerField(choices=social_medias, null=True, blank=True)
    icon_of_social_media = models.ImageField(upload_to='social_media_icon/', blank=True, null=True)
    link_of_social_media = models.CharField(max_length=700, null=True, blank=True)

    def __str__(self):
        return self.get_name_of_media_display()








