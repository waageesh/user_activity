from django.shortcuts import render

#below modules are imported for using RestAPI's , models , serializers
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.http import JsonResponse
import json, requests

class User_view(APIView):
	def get( self, 	request):
		user = User.objects.all()
		serializer = UserSerializer(user , many = True)
		json_data = serializer.data
		'''
		To send raw JSON response
		'''
		return JsonResponse(json_data, safe=False)

class User_Json_view(APIView):
	def get( self, 	request):
		''' to get JSON response from other API and using that data'''
		response = requests.get('https://waageesh.pythonanywhere.com/user', stream=True,verify=False, timeout=5)
		json_resp = response.json()
		l = len(json_resp)
		'''
		To prettify JSON data
		'''
		json_data = dict(zip(range(0,l), json_resp))
		json_object = json.dumps(json_data, indent=2)

		'''
		pagination results of serialized data

		'''
		user = User.objects.all()
		serializer = UserSerializer(user , many = True)

		page = request.GET.get('page',1)
		paginator = Paginator(serializer.data, 5)
		try:
			grp_paginated = paginator.page(page)
		except PageNotAnInteger:
			grp_paginated = paginator.page(1)
		except EmptyPage:
			grp_paginated = paginator.page(paginator.num_pages)

		return render(request, 'pagination.html', {'paginated_data' : grp_paginated, 'json_resp' : json_object})




class Home_view(APIView):
	def get(self, request):
		user = User.objects.all()
		serializer = UserSerializer(user , many = True)
		data = []
		'''
		customizing serialzied data to
		JSON reponse
		'''
		for each in serializer.data:
		    id = each['user_id']
		    name = each['real_name']
		    location = each['tz']
		    logged_period = []
		    for activity in each['activities']:
		        start = activity.split(',')[0].split(':',1)[1]
		        end = activity.split(',')[1].split(':',1)[1]
		        logged_period.append({'start':start,'end':end})
		    data.append({'user_id':id ,'real_name': name ,'tz': location ,'activities' : logged_period})
		
		# prettify the json data
		pretty_json_data = json.dumps(data, indent=2)
		
		'''
		pagination results of serialized data
		'''

		page = request.GET.get('page',1)
		paginator = Paginator(data, 5)
		try:
		    grp_paginated = paginator.page(page)
		except PageNotAnInteger:
		    grp_paginated = paginator.page(1)
		except EmptyPage:
		    grp_paginated = paginator.page(paginator.num_pages)
		# return paginated results
		return render(request, 'result.html', {'paginated_data' : grp_paginated, 'list_data' : data,'pretty_json_data':pretty_json_data})