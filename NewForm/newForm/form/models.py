from django.db import models

# Create your models here.

class First_Name(models.Model):
    top_name =models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name



class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20,unique=True)
    on_delete=models.CASCADE,
    #on_delete=models.SET(Webpage),

    # def __str__(self):
    #     return self.name 


# class Username(models.Model):
#     name= models.ForeignKey(Webpage,on_delete=models.CASCADE,)
#     date =models.DateField()
#     on_delete=models.CASCADE,
#     #on_delete=models.SET(Webpage),
#     def __str__(self):
#         return str(self.date)

