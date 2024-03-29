"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from views import index
from views import device_mgmt
from views import monitor_device


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.qyt_index),
    path('add_device/', device_mgmt.add_device),
    path('show_device/', device_mgmt.show_device),
    path('delete_device/<int:id>/', device_mgmt.delete_device),
    path('edit_device/<int:id>/', device_mgmt.edit_device),
    path('monitor_device', monitor_device.monitor_device),
    path('monitor_device/<str:chart_type>/<int:deviceid>/', monitor_device.chart_json),

]
