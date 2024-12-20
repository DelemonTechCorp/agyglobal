from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('base/',views.base,name='base'),
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('contact_view',views.contact_view,name='contact_view'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('blogs/',views.blogs,name='blogs'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('mining/',views.mining,name='mining'),
    path('equipment',views.equipment,name='equipment'),
    path('foodstuff',views.foodstuff,name='foodstuff'),
    path('sugar',views.sugar,name='sugar'),
    path('gold',views.gold,name='gold'),
    path('gallery',views.gallery,name='gallery')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)