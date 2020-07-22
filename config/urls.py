from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    # Base pages 
    path(
        '',
        TemplateView.as_view(template_name="pages/home.html"),
        name='home'
    ),
    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),

    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),

    # User management

    # My stuff: custom urls includes go here
    path('covid',    include('utilities.covidstatus.urls',      namespace='covidstatus')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)