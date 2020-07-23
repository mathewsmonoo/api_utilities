from django.db import models
import pip._vendor.requests as rqst
from django.utils.dateparse import parse_date, parse_datetime


url_br  =  'https://covid19-brazil-api.now.sh/api/report/v1'
url_all =  'https://covid19-brazil-api.now.sh/api/report/v1/countries'

# Create your models here.
class CovidBRStates(object):
    def __init__(self,uid,uf,state,cases,deaths,suspects,refuses, datetime):
        self.uid         = uid     
        self.uf          = uf      
        self.state       = state   
        self.cases       = cases   
        self.deaths      = deaths  
        self.suspects    = suspects
        self.refuses     = refuses
        self.datetime    = datetime
        
    def get_datetime(self):
        date = parse_datetime(self.datetime)
        return(date.strftime("%d/%m/%y - %H:%M:%S"))

class CovidAllStates(object):
    def __init__(self,country,cases,confirmed,deaths,recovered,updated_at):
        self.country     = country     
        self.cases       = cases      
        self.confirmed   = confirmed   
        self.deaths      = deaths  
        self.recovered   = recovered
        self.updated_at  = updated_at
        
    def get_datetime(self):
        date = parse_datetime(self.updated_at)
        return(date.strftime("%d/%m/%y - %H:%M:%S"))

def covid_br_results():
    resp    = rqst.get(url=url_br)
    if (resp.status_code != 200):
        print("API Offline")
    else:
        mydict  = resp.json()
        #The json starts with 'data', so i need to access the data inside this.
        mylist = mydict['data']

    results_list = []
    for i,j in enumerate(mylist):
        # Create a holder object with the info
        holder = CovidBRStates(mylist[i]['uid'],mylist[i]['uf'],mylist[i]['state'],mylist[i]['cases'],mylist[i]['deaths'],mylist[i]['suspects'],mylist[i]['refuses'],mylist[i]['datetime'])
        # Add that object to my list
        results_list.append(holder)

    return results_list


def covid_all_results():
    resp    = rqst.get(url=url_all)
    if (resp.status_code != 200):
        print("API Offline")
    else:
        mydict  = resp.json()
        #The json starts with 'data', so i need to access the data inside this.
        mylist = mydict['data']

    results_list = []
    for i,j in enumerate(mylist):
        # Create a holder object with the info
        holder = CovidAllStates(mylist[i]['country'],mylist[i]['cases'],mylist[i]['confirmed'],mylist[i]['deaths'],mylist[i]['recovered'],mylist[i]['updated_at'])
        # Add that object to my list
        results_list.append(holder)

    return results_list