
# admin_site/urls.py
from django.urls import path
from .views import login_view, dashboard, logout_view, add_fieldcomponent, FieldComponentViewSet

urlpatterns = [
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('add_fieldcomponent/', add_fieldcomponent, name='add_fieldcomponent'),  # Add the URL pattern for the new view
    path('api/fieldcomponents/', FieldComponentViewSet.as_view({'get': 'list', 'post': 'create'}), name='fieldcomponents-list'),


]


