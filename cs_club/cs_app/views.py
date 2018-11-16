from django.shortcuts import render
from django.views import generic
from .models import Display, Member, Trip, Project


# Create your views here.
class HomeView(generic.TemplateView):
	model=Display
	template_name = "home.html"


class AboutView(generic.DetailView):
	model=Display
	template_name = 'about.html'


class MembersListView(generic.ListView):
	model=Member
	template_name = 'members_list.html'


class MembersView(generic.DetailView):
	model=Member
	template_name="members.html"


class TripsListView(generic.ListView):
	model=Trip
	template_name = 'trips_list.html'


class TripsView(generic.DetailView):
	model=Trip
	template_name="trips.html"


class ProjectListView(generic.ListView):
	model=Project
	template_name = 'project_list.html'


class ProjectView(generic.DetailView):
	model=Project
	template_name="project.html"
