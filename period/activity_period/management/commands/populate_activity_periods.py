import datetime
import random

from django.core.management.base import BaseCommand

from activity_period.models import *


class Command(BaseCommand):
    help = "Save randomly generated activity period timings."

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument(
            'number_of_user_activities',
            type=int,
            help="Number of stock records to generate and save to database"
        )    

    def get_logged_in_period(self):
        # Naively generating a random date
        day = random.randint(1, 28)
        #month = random.randint(1, 12)
        year = random.randint(2015, 2020)
        mon = random.choice(['JAN','FEB','MAR','APR','MAY','JUNE','JULY','AUG','SEP','OCT','NOV','DEC'])
        hrs = random.randint(1,12)
        minutes = random.randint(1,60)
        periods = random.choice(['AM' , 'PM'])
        if len(str(minutes)) == 1:
            minutes = str(0)+str(minutes)
        start_time = str(mon)+" "+str(day)+" "+str(year)+"  "+str(hrs)+":"+str(minutes)+str(periods)
        if periods == "AM":
            periods = "PM"
        logged_out_time = random.randint(5,9)
        logged_out_day = random.randint(day,28)
        end_time = str(mon)+" "+str(logged_out_day)+" "+str(year)+"  "+str(logged_out_time)+":"+str(minutes)+str(periods)        
        return start_time , end_time

    def handle(self, *args, **options):
        activity_records = []
        user_records = []
        size = options["number_of_user_activities"]
        for _ in range(size):
            #user_id = random.choice(["A012A3PLO", "N012S3EJS" , "R012X3ZYO" , "W012A3CDE"])
            #activity_id = 0
            user_info = {'Michael Jordan': [1 , "A012A3PLO"] , 'Kevin Peter' : [2,"N012S3EJS" ], 'Thor Ragnorok': [ 3 , 'R012X3ZYO'] , 'Peter Parker':[4 , 'W012A3CDE']}
            items = random.choice(list(user_info.items()))
            real_name = items[0]
            user_id = items[1][1]
            activity_id = items[1][0]
            #real_name = random.choice(["Michael Jordan","Kevin Peter", "Thor Ragnorok" ,"Peter Parker"])
            tz = random.choice(['America/Los_Angeles' , 'Asia/Kolkatha' ,'Europe/london'  ])
            kwargs = {
                'start_time': self.get_logged_in_period()[0],
                'end_time': self.get_logged_in_period()[1],
                'user_id' : activity_id
            }
            user_details = {
                'user_id': user_id,
                'real_name' : real_name ,
                'tz' : tz
            }
            activity_record = Activity(**kwargs)
            user_record = User(**user_details)

            
            activity_records.append(activity_record)
            user_records.append(user_record)

        User.objects.bulk_create(user_records)
        self.stdout.write(self.style.SUCCESS('users populated sucessfully'))        
        Activity.objects.bulk_create(activity_records)
        self.stdout.write(self.style.SUCCESS('activities populated sucessfully'))

        self.stdout.write(self.style.SUCCESS('data populated sucessfully'))