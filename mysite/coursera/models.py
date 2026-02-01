from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):

    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    title=models.CharField(max_length=30)
    price=models.IntegerField()
    image=models.URLField(max_length=700)
    instructor_name =models.CharField()
    summary=models.CharField(max_length=5000,default="This course introduces fundamental concepts of computer systems and information technology. It covers basic hardware and software components, operating systems, data management, and essential computer applications. Students develop practical skills in using computers effectively, understanding digital tools, and applying problem-solving techniques relevant to academic and professional environments. ")


    
    def __str__(self):
        return self.title