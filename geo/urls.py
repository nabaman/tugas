
from django.contrib import admin
from django.urls import path,include
from .views import dashboard_view,send_api
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('',dashboard_view),
    path('send-api/',send_api)
]
