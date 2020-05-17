from django.contrib import admin
from django.urls import path
from eventapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),

    path('services/',views.services_d, name='services'),
    path('details/',views.details,name='details_page'),
    path('about_us',views.aboutus,name='about')
]