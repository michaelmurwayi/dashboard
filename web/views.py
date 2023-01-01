from django.shortcuts import render
from django.views.generic import TemplateView
import requests
import json


# Create your views here.

# Super admin views
# This views are restricted only to Super admin role users

class DashboardView(TemplateView):
    template_name = "super-admin/dashboard.html"

class SuperAdminCompanyView(TemplateView):
    template_name = "super-admin/companies.html"
    url = "http://127.0.0.1:8080/companies/"
    users_url = "http://127.0.0.1:8080/users/"

    def get(self, request):
        email = "mike1@gmail.com"
        password = "C11h28no3"
        if check_token(request) == 404:
            request.session["token"] = get_access_token(email, password)
        
        users = api_get_request(request, self.users_url)
        companies = api_get_request(request, self.url)
        return render(request, self.template_name, {"companies":companies, "users":users})
    
    def post(self,request):
        data = {
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "location": request.POST.get("location"),
        }
        if request.POST.get("_method") == "PUT":
            put_url = f"{self.url}{request.POST.get('company_id')}/"
            api_put_request(request, put_url, data)
        else:
            api_post_request(request,self.url, data)

    
        companies = api_get_request(request, self.url)
        return render(request, self.template_name, {"companies":companies})


class SuperAdminCompanyAdminView(TemplateView):
    template_name = "super-admin/companies.html"   
    url = "http://127.0.0.1:8080/companies/"
    users_url = "http://127.0.0.1:8080/users/"

    def get(self, request):
        email = "mike1@gmail.com"
        password = "C11h28no3"
        if check_token(request) == 404:
            request.session["token"] = get_access_token(email, password)
        
        users = api_get_request(request, self.users_url)
        companies = api_get_request(request, self.url)
        print(users)
        return render(request, self.template_name, {"companies":companies, "users": users})
    
    def post(self, request):
        # post method will be used for adding new company admins
        # patch method will be used will deleting company admins

        email = "mike1@gmail.com"
        password = "C11h28no3"
        
        if check_token(request) == 404:
            request.session["token"] = get_access_token(email, password)

        if request.POST.get("form_name") == "add":

            data = {
                "company": request.POST.get("company_id"),
                "is_company_admin": True  
            }
        else:
            data = {
                "company": "",
                "is_company_admin": False
            }

        patch_url = f"{self.users_url}{request.POST.get('user_id')}/"
        
        print(patch_url)

        response = api_patch_request(request, patch_url, data)

        users = api_get_request(request, self.users_url)

        companies = api_get_request(request, self.url)
        
        return render(request, self.template_name, {"companies":companies, "users": users})

class SuperAdminSaccoView(TemplateView):
    template_name = "super-admin/saccos.html"

    def get(self, request):
        saccos = [
            {
                "id":"1",
                "name":"Tropical",
                "email":"tropical@gmail.com",
                "location":"Thika Road, Eastern Bypass",
                "phonenumber":"+2547455445"
            },
            {
                "id":"2",
                "name":"Kahawa Bora",
                "email":"bora@gmail.com",
                "location":"Thika, Garrisa Highway",
                "phonenumber":"+254756655665"
            }
        ]
        return render(request, self.template_name, {"saccos":saccos})

class SuperAdminUsersView(TemplateView):
    template_name = "super-admin/users.html"
    url = "http://127.0.0.1:8080/users/"
    register_url = "http://127.0.0.1:8080/api/register/"

    def get(self, request):
        email = "mike1@gmail.com"
        password = "C11h28no3"
        if check_token(request) == 404:
            request.session["token"] = get_access_token(email, password)
        
        users = api_get_request(request, self.url)
        
        return render(request, self.template_name, {"users":users})

    def post(self,request):

        data = {
            "first_name": request.POST.get("first_name"),
            "last_name": request.POST.get("last_name"),
            "email": request.POST.get("email"),
            "location": request.POST.get("location"),
            "phonenumber": request.POST.get("phonenumber"),
            "password": request.POST.get("password"),
            "password2": request.POST.get("password"),

        }
        print(data)
        if request.POST.get("_method") == "PUT":
            id = request.POST.get('id')
            api_put_request(request, id, self.url, data)
        else:
            api_post_request(request,self.register_url, data)

        
        saccos = api_get_request(request, self.url)
        
        users = api_get_request(request, self.url)
        
        return render(request, self.template_name, {"users":users, "saccos":saccos})
    

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

def api_patch_request(request, url, data):
    # making put request to the data api
       
    try:
        headers = {
                'content-type': "application/json",
                'Authorization': f'Bearer {request.session["token"]}'
                }
        response = requests.patch(url, headers=headers, json=data) 
          
        if response.status_code == 401:
            headers = add_auth_token(request)
            response = requests.patch(url, headers=headers, json=data)
            return response.json()
        else:
            print(response.text)
            return response.json()
    except Exception:
        raise Exception
        return "Error occured Making request"

def api_put_request(request, url, data):
    # making put request to the data api
       
    try:
        headers = {
                'content-type': "application/json",
                'Authorization': f'Bearer {request.session["token"]}'
                }
        response = requests.put(url, headers=headers, json=data) 
          
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
