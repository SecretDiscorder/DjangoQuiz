from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class courseName(models.Model):
	course_name= models.CharField(max_length= 200)
	def __str__(self):
		return self.course_name
from django.db import models


    		
class Question(models.Model):
	question_name= models.ForeignKey(courseName, on_delete=models.CASCADE)
	question = models.CharField(max_length= 200)
	time_limit = models.DurationField(default=timezone.timedelta(minutes=10))
    
	answer = models.IntegerField()
	option_one= models.CharField(max_length= 200, blank= True)
	option_two= models.CharField(max_length= 200, blank= True)
	option_three= models.CharField(max_length= 200, blank= True)
	option_four= models.CharField(max_length= 200, blank= True)
	option_five= models.CharField(max_length= 200, blank= True)
	marks= models.IntegerField(default=5)
	def __str__(self):
		return self.question
class ScoreBoard(models.Model):
	question_name= models.ForeignKey(courseName, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	score= models.IntegerField()