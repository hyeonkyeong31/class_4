from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
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