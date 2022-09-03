from django.db import models

# Create your models here.
class banks(models.Model):
    bankname= models.CharField(max_length=300)

    def __str__(self) :
        return self.bankname



class bankclient(models.Model):
    firstname = models.CharField(max_length = 150)
    lastname = models.CharField(max_length = 150)
    birthdate = models.DateField()
    dni = models.CharField(max_length=13)
    phone = models.CharField(max_length=15)
    bankid = models.ForeignKey(banks, on_delete=models.CASCADE )

    def __str__(self) :
        return self.dni

    class meta:
        ordering= ('Created',)

