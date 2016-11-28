from django.db import models

class Action(models.Model):
    id =            models.AutoField(primary_key=True)
    name =          models.CharField(max_length=50, unique=True, null=False)
    description =   models.TextField(null=True, default=None)

class Role(models.Model):
    id =            models.AutoField(primary_key=True)
    name =          models.CharField(max_length=20, unique=True, null=False)
    sub_role =      models.ForeignKey('self', on_delete=models.CASCADE) #TODO check if correct
    actions =       models.ManyToManyField(Action)


class User(models.Model):
    id =            models.AutoField(primary_key=True)
    name =          models.CharField(max_length=50, null=False)
    surname =       models.CharField(max_length=50, null=False)
    username =      models.CharField(max_length=50, unique=True, null=False)
    email =         models.EmailField(unique=True, null=False)
    password_hash = models.CharField(max_length=64, null=False)
    date_of_birth = models.DateField(null=True, default=None)
   
    role =          models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    class Meta:
        pass
