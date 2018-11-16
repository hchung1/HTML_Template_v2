"""cs_club URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cs_app.views import HomeView, AboutView, MembersListView, MembersView, TripsListView, TripsView, ProjectListView, ProjectView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('members/', MembersListView.as_view(), name='memberslist'),
    path('members/<int:pk>/', MembersView.as_view(), name='members'),
    path('trips/', TripsListView.as_view(), name='tripslist'),
    path('trips/<int:pk>/', TripsView.as_view(), name='trips'),
    path('project', ProjectListView.as_view(), name='projectlist'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project'),
    path('admin/', admin.site.urls),
]
