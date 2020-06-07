from django.db import models

# Create your models here.
class User(models.Model):
	#activity = models.ManyToManyField("Activity" 	 ,blank = True, related_name='user_activity'  )
	user_id = models.CharField(max_length=30 , default = 'W012A3CDE')
	real_name = models.CharField(max_length=50  , default = 'JOHN DAVID')
	tz = models.CharField(max_length=50 , default = 'America/Los_Angeles' )
	# def __str__(self):
	# 	return '%: %s' % (self.user_id, self.real_name)

class Activity(models.Model):
	user = models.ForeignKey("User" , on_delete = models.DO_NOTHING , blank = True ,related_name = 'activities'  )
	start_time = models.CharField(null = False, max_length = 50 , default = 'Feb 1 2020  1:33PM')
	end_time = models.CharField(null = False , max_length = 50 , default = 'Feb 1 2020  1:33PM')
	#timings = ['start_time : ' , start_time , 'end_time' , end_time]
	#start_time = "start_time : " + str(start_time)
	#end_time  = "end_time : " + str(end_time)
	def __str__(self):
# 		return {'start_time' : self.start_time, 'end_time' : self.end_time}
		return 'start_time : %s , end_time :%s' % (self.start_time, self.end_time)