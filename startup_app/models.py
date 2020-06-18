from django.db import models
from django.utils import timezone
# Create your models here.

class StartUps(models.Model):
    name      = models.CharField(max_length = 1000)
    siteurl   = models.CharField(max_length = 1000)
    location  = models.CharField(max_length = 1000)
    compEmail = models.EmailField(max_length = 1000)
    regID     = models.CharField(max_length = 500)
    about     = models.TextField(default = '-')

    def __str__(self):
        return(self.name)

class Investors(models.Model):
    name  = models.CharField(max_length = 1000)
    email = models.EmailField(max_length = 1000)
    about = models.TextField(default = '-')
    interested_fields = models.TextField()
    amount_to_invest  = models.DecimalField(max_digits = 20, decimal_places = 2)
    place = models.CharField(max_length = 500)
    website = models.CharField(max_length = 1000, default = '-')

    def __str__(self):
        return(self.name)

class Investment_table(models.Model):
    start_up = models.ForeignKey(StartUps, on_delete = models.CASCADE)
    investor = models.ForeignKey(Investors, on_delete = models.CASCADE)
    amount_invested = models.DecimalField(max_digits = 20, decimal_places = 2)
    day_invested = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return(self.start_up.name + " invested by " + self.investor.name)

class Jobs(models.Model):
    job_type = models.CharField(max_length = 1000)
    location = models.CharField(max_length = 1000)
    salary   = models.DecimalField(max_digits = 20, decimal_places = 2)
    skill_set = models.TextField()
    years_of_experience = models.IntegerField()
    company = models.ForeignKey(StartUps, on_delete = models.CASCADE)

    def __str__(self):
        return(self.job_type +" in " + self.company.name)

class Job_Seekers(models.Model):
    name      = models.CharField(max_length = 1000)
    email     = models.EmailField(max_length = 1000)
    location  = models.CharField(max_length = 1000)
    desired_field = models.CharField(max_length = 1000, default = "NULL")
    skill_set = models.TextField()
    years_of_experience = models.TextField()

    def __str__(self):
        return(self.name)
