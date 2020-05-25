from django.shortcuts import render, redirect, reverse
from django.views import generic
from .models import IdInfo
from .forms import IcardForm
from django.http import HttpResponse



def home(request):
    form = IcardForm()
    if request.method == 'POST':
        form = IcardForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('icard:thanks'))
    context = {
        'form' : form
    }
    return render(request, 'icard/home.html', context)

def thankyou(request):
    return HttpResponse('Thank You')


class ClientList(generic.ListView):
    model = IdInfo
    template_name = 'icard/client-list.html'
    context_object_name = 'ids'