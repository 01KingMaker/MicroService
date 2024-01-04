from django.contrib import admin
from django.urls import path
from PythonMicroService.views import qr_code, student

from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('code/<str:text>/', qr_code.generate_qr_code),
    path('students/', student.get_all_students),
    path('students/insert', student.save_students)
]
