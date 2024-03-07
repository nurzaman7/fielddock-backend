from django.urls import path, include
from rest_framework import routers

from .views import login_view, dashboard, logout_view, add_fieldcomponent, FieldComponentViewSet, AdminLoginView

field_component_router = routers.SimpleRouter()
field_component_router.register('fieldcomponents', FieldComponentViewSet)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('api/', include(field_component_router.urls)),
    path('api/login/', AdminLoginView.as_view(), name='admin_login'),
    path('add_fieldcomponent/', add_fieldcomponent, name='add_fieldcomponent')
]
