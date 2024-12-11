"""
URL configuration for three_amigos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from bookings import views
from dates import views
from enquiries import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_index, name='index'),
    path('base/', views.get_base, name='base'),
    path('dates/', views.get_dates, name='dates'),
    path('results/', views.get_results, name='results'),
    path('info/', views.get_info, name='info'), 
    path('bookings/', include('bookings.urls', namespace="bookings")),
    path('enquiry/', include('enquiries.urls', namespace="enquiry")),
    path('dates/', include('dates.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'bookings.views.error_404'
