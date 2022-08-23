#from django.conf.urls import url
from django.urls import re_path as url
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^departments$',views.departmentApi),
    url(r'^departments/([0-9]+)$', views.departmentApi),

    url(r'^employee$',views.employeeApi),
    url(r'^employee/([0-9]+)$', views.employeeApi),

    url(r'/employee/save_file',views.save_file)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)