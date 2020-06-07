from django.urls import path
from .views  import *

urlpatterns = [
			path("user",User_view.as_view()),
			path("home",Home_view.as_view()),
			path("userjson",User_Json_view.as_view())

]

