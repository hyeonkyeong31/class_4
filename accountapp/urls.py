from django.urls import path

from accountapp.views import go_home, AccountCreateView

app_name = 'accountapp'
urlpatterns = [
    path('go_home/', go_home, name = 'go_home'),

    path('create/', AccountCreateView.as_view(), name = 'create')
]