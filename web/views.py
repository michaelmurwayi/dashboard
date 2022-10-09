from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# Super admin views
# This views are restricted only to Super admin role users

class DashboardView(TemplateView):
    template_name = "super-admin/dashboard.html"

class SuperAdminCompanyView(TemplateView):
    template_name = "super-admin/companies.html"

    def get(self, request):
        companies = [
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
