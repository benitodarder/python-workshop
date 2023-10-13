from django.db import models

      
class Country(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return  str(self.id) + ' ' + self.name  
        
class Sport(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return  str(self.id) + ' ' + self.name  

class Person(models.Model):
    name = models.CharField(max_length=200)
    dateBirth = models.DateTimeField('Birth date')
    nationalty = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    sports = models.ManyToManyField(Sport)
     
    def __str__(self):
        return str(self.id) + ' ' + self.name   
