"""babarkotsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from babarkotapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('',include('babarkotapp.urls')),
    path('admin/', admin.site.urls),
    path('Generate-Trial-Certificate/<int:id>', views.gen_trial, name="gentrial"),
    path('Generate-Bonafide-Certificate/<int:id>', views.gen_bonafide, name="genbona"),
    path('Generate-Birth-Certificate/<int:id>', views.gen_birth, name="genbirth"),
    path('Cash-Book-Locate-Entry/<int:id>', views.cashbook_filter, name="cashbook_filter"),
    path('Edit-Student/<int:id>', views.edit_student, name="edit_st"),
    path('View-All-Photos/<int:id>',views.view_gallery,name='viewgallery'),
    path('Edit-Profile/<int:id>', views.edit_profile, name="editprof"),
    path('Edit-Grant/<int:id>', views.edit_grant, name="editgrant"),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
