from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Jobs, Investment_table, Investors, Job_Seekers, StartUps
from .forms import startupsform,jobseekersform,Jobsform,Investment_tableform,Investorsform
from django.shortcuts import redirect

# Create your views here.
class JobListView(ListView):
    model = Jobs
    template_name = "startup_app/available_jobs.html"
    context_object_name = 'jobs'
    ordering = ['job_type']

class InvestmentListView(ListView):
    model = Investment_table
    template_name = "startup_app/home.html"
    context_object_name = 'itable'

class InvestorListView(ListView):
    model = Investors
    template_name = 'startup_app/investorlist.html'
    context_object_name = 'investor_table'
    ordering = ['name']

class JobSeekersListView(ListView):
    model = Job_Seekers
    template_name = 'startup_app/jobseekerlist.html'
    context_object_name = 'seeker_table'

class StartUpListView(ListView):
    model = StartUps
    template_name = 'startup_app/startup_table.html'
    context_object_name = 'startup_table'

class JobDetailView(DetailView):
    model = Jobs
    template_name = "startup_app/job_detail.html"
    context_object_name = 'job_detail'


class InvestorDetailView(DetailView):
    model = Investors
    template_name = 'startup_app/investor_detail.html'
    context_object_name = 'investor'

class StartUpDetailView(DetailView):
    model = StartUps
    template_name = 'startup_app/startup_detail.html'
    context_object_name = 'startup'

class JobSeekerDetailView(DetailView):
    model = Job_Seekers
    template_name = 'startup_app/seeker_detail.html'
    context_object_name = 'seeker'

class InvestmentDetailView(DetailView):
    model = Investment_table
    template_name = 'startup_app/investment_detail.html'
    context_object_name = 'investment'

def startup_new(request):
    if request.method == "POST":
       form = startupsform(request.POST)
       if form.is_valid():
           StartUps = form.save(commit=False)
           StartUps.author = request.user
           StartUps.save()
           return render(request,'startup_app/startup_table.html')
    else:
        form = startupsform()
    return render(request, 'startup_app/startup_edit.html', {'form': form})

def investor_new(request):
    if request.method == "POST":
       form = Investorsform(request.POST)
       if form.is_valid():
           Investors = form.save(commit=False)
           Investors.author = request.user
           Investors.save()
           return render(request,'startup_app/investorlist.html')
    else:
        form = Investorsform()
    return render(request, 'startup_app/investor_edit.html', {'form': form})

def investment_new(request):
    if request.method == "POST":
       form = Investment_tableform(request.POST)
       if form.is_valid():
           Investment_table = form.save(commit=False)
           Investment_table.author = request.user
           Investment_table.save()
           return render(request,'startup_app/home.html')
    else:
        form = Investment_tableform()
    return render(request, 'startup_app/investment_edit.html', {'form': form})

def jobs_new(request):
    if request.method == "POST":
       form = Jobsform(request.POST)
       if form.is_valid():
           Jobs = form.save(commit=False)
           Jobs.author = request.user
           Jobs.save()
           return render(request,'startup_app/available_jobs.html')
    else:
        form = Jobsform()
    return render(request, 'startup_app/job_edit.html', {'form': form})

def seekers_new(request):
    if request.method == "POST":
       form = jobseekersform(request.POST)
       if form.is_valid():
           Job_Seekers = form.save(commit=False)
           Job_Seekers.author = request.user
           Job_Seekers.save()
           return render(request,'startup_app/jobseekerlist.html')
    else:
        form = jobseekersform()
    return render(request, 'startup_app/seekers_edit.html', {'form': form})
