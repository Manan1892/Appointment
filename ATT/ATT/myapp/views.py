from django.shortcuts import render,redirect
from myapp.models import *
from django.views import View
from django.db.models import  Q
from django.http import HttpResponse,JsonResponse
import json


# Create your views here.

class Home(View):
	
	
	def get(self, request, *args, **kwargs):
		data = AppointmentsModel.objects.all()
		return render(request, 'index.html',{'data':data})

	def post(self, request, *args, **kwargs):
		data = request.POST
		obj = AppointmentsModel(appointment_date=data['appointment_date'],appointment_time=data['appointment_time'],description=data['description'])
		obj.save()
		return redirect('/')

class Appoinments(View):
	def get(self, request, *args, **kwargs):
		data = list(AppointmentsModel.objects.all().values('appointment_date','appointment_time','description'))
		return HttpResponse(json.dumps(data),content_type="application/json")


class SearchAppoinments(View):
	def get(self, request, *args, **kwargs):
		key = request.GET['key']
		data = list(AppointmentsModel.objects.filter(Q(appointment_date__icontains=key)|
										   Q(appointment_time__icontains=key)|
										   Q(description__icontains=key)).values('appointment_date','appointment_time','description'))

		return HttpResponse(json.dumps(data),content_type="application/json")