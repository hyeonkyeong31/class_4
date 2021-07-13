from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import NewModel


def go_home(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        new_model = NewModel()
        new_model.text = temp
        new_model.save()
        return HttpResponseRedirect(reverse('accountapp:go_home'))


    else:
        data_list = NewModel.objects.all()
        return render(request, 'accountapp/go_home.html',
                      context={'data_list': data_list})

class AccountCreateView(CreateView):
    model =User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:go_home')
    template_name = 'accountapp/create.html'