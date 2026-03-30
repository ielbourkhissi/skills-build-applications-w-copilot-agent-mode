"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import os
from django.contrib import admin
from django.urls import path
codespace_name = os.environ.get('CODESPACE_NAME')
from octofit_tracker import views
from django.http import JsonResponse

codespace_name = os.environ.get('CODESPACE_NAME')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
else:
    base_url = "http://localhost:8000"

def api_root(request, format=None):
    return JsonResponse({
        'users': f'{base_url}/api/users/',
        'teams': f'{base_url}/api/teams/',
        'activities': f'{base_url}/api/activities/',
        'leaderboards': f'{base_url}/api/leaderboards/',
        'workouts': f'{base_url}/api/workouts/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/users/', views.users_list, name='users-list'),
    path('api/teams/', views.teams_list, name='teams-list'),
    path('api/activities/', views.activities_list, name='activities-list'),
    path('api/leaderboards/', views.leaderboards_list, name='leaderboards-list'),
    path('api/workouts/', views.workouts_list, name='workouts-list'),
    path('', api_root),
]
