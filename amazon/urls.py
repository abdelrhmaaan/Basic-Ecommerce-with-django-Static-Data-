from django.urls import path
# from amazon.views import hello_world, bootstrap,hiFriend,home_page,return_to_homepage
from . import views as v

urlpatterns = [
    path('home',v.return_to_homepage,name='home'),
    path('aboutus',v.about_us,name='aboutus'),
    path('contactus',v.contact_us,name='contactus'),
    path('productpage/<int:id>',v.product_page,name='productpage'),
]
