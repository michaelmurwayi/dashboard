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
    pass

class SuperAdminUsersView(TemplateView):
    pass

class SuperAdminChartsView(TemplateView):
    pass

class SuperAdminEventsView(TemplateView):
    pass

class SuperAdminMapsView(TemplateView):
    pass
