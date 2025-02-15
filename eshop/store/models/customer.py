from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50,null=False,default='')
    last_name = models.CharField (max_length=50,null=False,default='')
    phone = models.CharField(max_length=10,null=False,default='')
    email=models.EmailField(null=False,default='')
    password = models.CharField(max_length=100,null=False,default='')

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False