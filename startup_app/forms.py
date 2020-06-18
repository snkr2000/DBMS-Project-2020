from django import forms
from .models import StartUps,Investors,Investment_table,Job_Seekers,Jobs

class startupsform(forms.ModelForm):
    class Meta:
        model = StartUps
        fields = ['name','siteurl','location','compEmail','regID','about',]

class Investorsform(forms.ModelForm):
    class Meta:
        model = Investors
        fields = ['name','email','about','interested_fields','amount_to_invest','place','website',]

class Investment_tableform(forms.ModelForm):
    class Meta:
        model = Investment_table
        fields = ['start_up','investor','amount_invested','day_invested',]

class Jobsform(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['job_type','location','salary','skill_set','years_of_experience','company',]

class jobseekersform(forms.ModelForm):
    class Meta:
        model = Job_Seekers
        fields = ['name','email','location','desired_field','skill_set','years_of_experience',]