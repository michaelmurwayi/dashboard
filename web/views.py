from django.shortcuts import render
from django.views.generic import TemplateView

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
        
        companies = api_request(request, self.url)
        return render(request, self.template_name, {"companies":companies})

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

def get_access_token(email, password):
    # get authentication token from api and save to session
    
    url = 'http://127.0.0.1:8080/login/'
    data = {'email': email, "password":password}
    response = requests.post(url, data=data)
    token = response.json()["access"]
    
    return token


def api_request(request, url):
    try:
        headers = {
                'content-type': "application/json",
                'Authorization': f'Bearer {request.session["token"]}'
                }
        response = requests.get(url, headers=headers)
        print(response.status_code)
        if response.status_code == 401:
            email = "mike1@gmail.com"
            password = "C11h28no3"
            request.session["token"] = get_access_token(email, password)
            headers = {
                'content-type': "application/json",
                'Authorization': f'Bearer {request.session["token"]}'
                }
            response = requests.get(url, headers=headers)

            return response.json()
        else:
            return response.json()
    except Exception:
        raise Exception

        return "Error occured Making request"