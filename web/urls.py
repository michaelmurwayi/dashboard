from django.urls import path
from .views import DashboardView, SuperAdminCompanyView, SuperAdminSaccoView, SuperAdminUsersView, SuperAdminChartsView, SuperAdminEventsView, SuperAdminMapsView
urlpatterns = [
    # super admin routes
    path('super-admin/', DashboardView.as_view(), name="super-admin"),
    path('super-admin/company', SuperAdminCompanyView.as_view(), name="super-admin-company"),
    path('super-admin/sacco', SuperAdminSaccoView.as_view(), name="super-admin-sacco"),
    path('super-admin/users', SuperAdminUsersView.as_view(), name="super-admin-users"),
    path('super-admin/charts', SuperAdminChartsView.as_view(), name="super-admin-charts"),
    path('super-admin/events', SuperAdminEventsView.as_view(), name="super-admin-events"),
    path('super-admin/maps', SuperAdminMapsView.as_view(), name="super-admin-maps"),

]