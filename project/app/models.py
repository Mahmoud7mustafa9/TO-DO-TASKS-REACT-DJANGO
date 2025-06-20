from django.db import models

# Create your models here.
class Project (models.Model):
    title = models.CharField( unique = True ,max_length= 3324)
    start_date = models.DateField()
    end_date= models.DateField()
    created= models.DateTimeField(auto_now_add=True)
    comments= models.TextField(max_length=400)
    status = models.CharField(max_length=100) 
    id = models.IntegerField(unique= True, primary_key=True)
    def __str__(self):
        return self.title