from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    path('posts/', TemplateView.as_view(template_name='posts.html'), name='posts'),
    path('gallery/', TemplateView.as_view(template_name='gallery.html'), name='gallery'),
    path('contact-us/', TemplateView.as_view(template_name='contact-us.html'), name='contact'),
    path('resources/', TemplateView.as_view(template_name='resources.html'), name='resources'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),
]