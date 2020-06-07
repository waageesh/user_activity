from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	# user_related = 	User.objects.all() #copying content from User model to a variable
	# u_related = None
	# for key in user_related:
	# 	u_related = key.user_activity.all() # using above copied variable, again get activity model
	# 	break
	activities = serializers.StringRelatedField(many=True)
	class Meta:
		model = User #fields = "__all__" #takes all fields, use tuple/list for less  fields-> ["activity","us#er_id"]
		#activities = serializers.StringRelatedField(many=True)
		fields = ['user_id' , 'real_name' ,'tz' ,  'activities'] #["u_related" , "user_id","real_name"]

		start_time = serializers.SerializerMethodField()
		end_time = serializers.SerializerMethodField()


		#fields = [ "u_related","user_id" ,"real_name" ,"tz" ]
	def get_start_time(self,obj):
		if not obj.activity:
			return obj.activity , obj.activity.start_time
		return obj.activity.start_time
	def get_end_time(self,obj):
		if not obj.activity:
			return obj.activity , obj.activity.end_time
		return obj.activity.end_time


class Activity_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Activity
		fields = "__all__"