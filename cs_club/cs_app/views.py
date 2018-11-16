from django.shortcuts import render
from django.views import generic
from .models import Members, Trips, Project


# Create your views here.
class HomeView(generic.TemplateView):
	template_name = "home.html"


class AboutView(generic.DetailView):
	template_name = 'about.html'


class MembersListView(generic.ListView):
	model=Members
	template_name = 'members_list.html'


class MembersView(generic.DetailView):
	model=Members
	template_name="members.html"


class TripsListView(generic.ListView):
	model=Trips
	template_name = 'trips_list.html'


class TripsView(generic.DetailView):
	model=Trips
	template_name="trips.html"


class ProjectListView(generic.ListView):
	model=Project
	template_name = 'project_list.html'


class ProjectView(generic.DetailView):
	model=Project
	template_name="project.html"
