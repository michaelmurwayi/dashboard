from django.shortcuts import render
from django.views.generic import TemplateView
import requests

# Create your views here.

# Super admin views
# This views are restricted only to Super admin role users

class DashboardView(TemplateView):
    template_name = "super-admin/dashboard.html"

class SuperAdminCompanyView(TemplateView):
    template_name = "super-admin/companies.html"
    url = "http://127.0.0.1:8080/companies/"

    def get(self, request):
        email = "mike1@gmail.com"
        password = "C11h28no3"
        if check_token(request) == 404:
            request.session["token"] = get_access_token(email, password)
        
        companies = api_get_request(request, self.url)
        return render(request, self.template_name, {"companies":companies})
    
    def post(self,request):
        data = {
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "location": request.POST.get("location"),
        }
        if request.POST.get("_method") == "PUT":
            id = request.POST.get('company_id')
            api_put_request(request, id, self.url, data)
        else:
            api_post_request(request,self.url, data)

        companies = api_get_request(request, self.url)
        return render(request, self.template_name, {"companies":companies})
    

class SuperAdminSaccoView(TemplateView):
    template_name = "super-admin/saccos.html"
    url = "http://127.0.0.1:8080/saccos/"
    
    def get(self, request):
        email = "mike1@gmail.com"
        password = "C11h28no3"
        if check_token(request) == 404:
            request.session["token"] = get_access_token(email, password)
        
        saccos = api_get_request(request, self.url)
        company_url = "http://127.0.0.1:8080/companies/"
        companies = api_get_request(request, company_url)
        
        
        return render(request, self.template_name, {"saccos":saccos, "companies":companies})
    
    def post(self,request):

        data = {
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "location": request.POST.get("location"),
            "company": request.POST.get("company"),
        }
        if request.POST.get("_method") == "PUT":
            id = request.POST.get('sacco_id')
            api_put_request(request, id, self.url, data)
        else:
            api_post_request(request,self.url, data)

        
        saccos = api_get_request(request, self.url)
        
        
        return render(request, self.template_name, {"saccos":saccos})
    
    
class SuperAdminUsersView(TemplateView):
    template_name = "super-admin/users.html"
    
    def get(self, request):
        users = [
            {
                "id":"1",
                "firstname":"Rick",
                "lastname":"Sanchez",
                "email":"tropical@gmail.com",
                "phonenumber":"+2547455445"
            },
            {
                "id":"2",
                "firstname":"Morty",
                "lastname":"Sanchez",
                "email":"bora@gmail.com",
                "phonenumber":"+254756655665"
            }
        ]
        return render(request, self.template_name, {"users":users})
class SuperAdminChartsView(TemplateView):
    template_name = "super-admin/charts.html"

class SuperAdminEventsView(TemplateView):
    template_name = "super-admin/events.html"

class SuperAdminMapsView(TemplateView):
    template_name = "super-admin/maps.html"


def check_token(request):
    try:
        token = request.session["token"]
        return 200
    except:
        return 404

def get_access_token(email, password):
    # get authentication token from api and save to session
    
    url = 'http://127.0.0.1:8080/login/'
    data = {'email': email, "password":password}
    response = requests.post(url, data=data)
    token = response.json()["access"]

    return token



def api_get_request(request, url):
    try:
        headers = {
                'content-type': "application/json",
                'Authorization': f'Bearer {request.session["token"]}'
                }
        response = requests.get(url, headers=headers)   
        if response.status_code == 401:
            headers = add_auth_token(request)
            response = requests.get(url, headers=headers)

            return response.json()
        else:
            return response.json()
    except Exception:
        raise Exception

        return "Error occured Making request"

def api_put_request(request, id, url, data):
    # making put request to the data api
    put_url = f"{url}{id}/"   
    try:
        headers = {
                'content-type': "application/json",
                'Authorization': f'Bearer {request.session["token"]}'
                }
        response = requests.put(put_url, headers=headers, json=data)   
        if response.status_code == 401:
            headers = add_auth_token(request)
            response = requests.put(url, headers=headers, json=data)
            return response.json()
        else:
            print(response.text)
            return response.json()
    except Exception:
        raise Exception
        return "Error occured Making request"


def api_post_request(request, url, data):
    try:
        headers = {
                'content-type': "application/json",
                'Authorization': f'Bearer {request.session["token"]}'
                }
        response = requests.post(url, headers=headers, json=data)   
        if response.status_code == 401:
            headers = add_auth_token(request)
            response = requests.post(url, headers=headers, json=data)
            return response.json()
        else:
            print(response.text)
            return response.json()
    except Exception:
        raise Exception

        return "Error occured Making request"

def add_auth_token(request):
    # adds Bearer token to the request headers
    # returns headers
    email = "mike1@gmail.com"
    password = "C11h28no3"
    request.session["token"] = get_access_token(email, password)
    headers = {
        'content-type': "application/json",
        'Authorization': f'Bearer {request.session["token"]}'
        }
    
    return headers