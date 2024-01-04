from django.http import JsonResponse
from PythonMicroService.model.Student import Student
import random
import string, json
from datetime import datetime

students = []

def get_all_students(request):
  json_str = json.dumps([i.__dict__() for i in students])
  return JsonResponse(json_str, safe=False)

def save_students(request):
  name = request.POST.get('name')
  date_birth = request.POST.get('date')
  print(name)
  print(date_birth)
  std = Student(name, date_birth, 1)
  students.append(std)
  print(students)
  return JsonResponse("Success", safe=False)
