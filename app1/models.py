from django.db import models

# Create your models here.


class Customer(models.Model):
    #id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    
    

#class MyModel(models.Model):
    # id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
