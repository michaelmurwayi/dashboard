from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# Super admin views
# This views are restricted only to Super admin role users

class DashboardView(TemplateView):
    template_name = "super-admin/dashboard.html"

class SuperAdminCompanyView(TemplateView):
    template_name = "super-admin/companies.html"

class SuperAdminSaccoView(TemplateView):
    template_name = "super-admin/saccos.html"

class SuperAdminUsersView(TemplateView):
    template_name = "super-admin/users.html"

class SuperAdminChartsView(TemplateView):
    template_name = "super-admin/charts.html"

class SuperAdminEventsView(TemplateView):
    template_name = "super-admin/events.html"

class SuperAdminMapsView(TemplateView):
    template_name = "super-admin/maps.html"
