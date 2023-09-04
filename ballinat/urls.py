from ballinat.views import *
from django.urls import path, include

from ballinat import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('blog/', views.blog, name="blog"),
    path('blog_single/', views.blog_single, name="blog-single"),
    path('product_single/', views.product_single, name="product-single"),
    path('contact/', views.contact, name="contact"),
    path('gallery/', views.product, name="gallery"),

    # path(r'^nested_admin/', include('nested_admin.urls')),
]

