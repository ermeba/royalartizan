from django.shortcuts import render

from ballinat.models import Contacts, TypeOfSocialMedia, Slide, Teknikat, AboutUs, Paragraphs, AfterSlides, Punim, \
    MesazheNgaKlientet, Blog


# Create your views here.

def home(request):
    contacts = Contacts.objects.all().values()
    medias = TypeOfSocialMedia.objects.all().values()
    slide = Slide.objects.filter(active=1)
    teknikat = Teknikat.objects.filter(active=1)
    about = AboutUs.objects.filter(active=1)
    paragraph = Paragraphs.objects.filter(about__active=1)
    afterslide = AfterSlides.objects.filter(active=1)
    punimet = Punim.objects.all().order_by('-date_created')[:8]
    mesazhet = MesazheNgaKlientet.objects.all().values()
    blogs = Blog.objects.all().order_by('-date_created')[:4]

    context = {
        "contacts": contacts,
        "medias": medias,
        'slide': slide,
        'teknikat': teknikat,
        'about': about,
        'paragraph': paragraph,
        'afterslide': afterslide,
        'punimet': punimet,
        'mesazhet':mesazhet,
        'blogs': blogs,

    }
    return render(request, "index.html", context)


def about(request):

    contacts = Contacts.objects.all().values()
    medias = TypeOfSocialMedia.objects.all().values()
    slide = Slide.objects.filter(active=1)
    teknikat = Teknikat.objects.filter(active=1)
    about = AboutUs.objects.filter(active=1)
    paragraph = Paragraphs.objects.filter(about__active=1)
    afterslide = AfterSlides.objects.filter(active=1)
    mesazhet = MesazheNgaKlientet.objects.all().values()

    context = {
        "contacts": contacts,
        "medias": medias,
        'slide': slide,
        'teknikat': teknikat,
        'about': about,
        'paragraph':paragraph,
        'afterslide': afterslide,
        'mesazhet': mesazhet,
    }
    return render(request, "about.html", context)


def contact(request):
    contacts = Contacts.objects.filter(active=1)
    medias = TypeOfSocialMedia.objects.all().values()
    slide = Slide.objects.filter(active=1)

    context = {
        "contacts": contacts,
        "medias": medias,
        'slide': slide,

    }
    return render(request, "contact.html", context)


def product(request):
    contacts = Contacts.objects.all().values()
    medias = TypeOfSocialMedia.objects.all().values()
    slide = Slide.objects.filter(active=1)
    punimet = Punim.objects.all().order_by('-date_created')

    context = {
        "contacts": contacts,
        "medias": medias,
        'slide': slide,
        'punimet': punimet,

    }
    return render(request, "product.html", context)


def blog(request):
    contacts = Contacts.objects.all().values()
    medias = TypeOfSocialMedia.objects.all().values()
    slide = Slide.objects.filter(active=1)
    blogs = Blog.objects.all().order_by('-date_created')

    context = {
        "contacts": contacts,
        "medias": medias,
        'slide': slide,
        'blogs': blogs,

    }
    return render(request, "blog.html", context)


def blog_single(request):
    contacts = Contacts.objects.all().values()
    medias = TypeOfSocialMedia.objects.all().values()
    slide = Slide.objects.filter(active=1)

    context = {
        "contacts": contacts,
        "medias": medias,
        'slide': slide,

    }
    return render(request, "blog-single.html", context)


def product_single(request):
    contacts = Contacts.objects.all().values()
    medias = TypeOfSocialMedia.objects.all().values()
    slide = Slide.objects.filter(active=1)

    context = {
        "contacts": contacts,
        "medias": medias,
        'slide': slide,

    }
    return render(request, "product-single.html", context)