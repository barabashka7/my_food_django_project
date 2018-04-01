from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include('my_food.urls')),
    path('login/', auth_views.login, {'template_name': 'my_food/login.html'}, name='login'),
    path('accounts/login/', auth_views.login, {'template_name': 'my_food/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': 'index'}, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
