from django.urls import path
from . import views

app_name = "covidstatus"
urlpatterns = [
    path(route='br/',view=views.get_br_info,name='brlist'),
    path(route='all/',view=views.get_all_info,name='alllist'),
]