from django.db import models

class employee(models.Model):
    name= models.CharField(max_length=250)
    Contact= models.IntegerField()
    email = models.EmailField(max_length=200,unique=True)
    About = models.TextField()
    portfolio_site = models.URLField()
    registered=models.BooleanField()
    date_of_birth= models.DateField()
    registered_on= models.DateTimeField(auto_now_add=True)
    salary = models.DecimalField(max_digits=10,decimal_places=5)
    membership_valid=models.DurationField()

    def __str__(self):
        return repr(self.id)
class  empArr(models.Model):
    Emp_id = models.ForeignKey(employee,on_delete=models.CASCADE)
    Arrival_time = models.DateTimeField()

    def __str__(self):
        return repr(self.Arrival_time)
