from django.shortcuts import render
# Create your views here.
from .models import CovidBRStates, CovidAllStates, covid_br_results, covid_all_results

def get_br_info(request):
    return render(request,'covidstatus/covid_br_list.html', {'covid_list':covid_br_results})
def get_all_info(request):
    return render(request,'covidstatus/covid_all_list.html', {'covid_list':covid_all_results})
