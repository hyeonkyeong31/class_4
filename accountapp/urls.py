from django.urls import path

from accountapp.views import go_home

app_name = 'accountapp'
urlpatterns = [
    path('go_home/', go_home, name = 'go_home'),
]