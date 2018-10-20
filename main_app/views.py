from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Widget
from django.http import HttpResponseRedirect
from .forms import WidgetForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = WidgetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        widgets = Widget.objects.all()
        form = WidgetForm()
        return render(request, 'base.html', {'widgets': widgets, 'form':form})


class WidgetCreate(CreateView):
    model = Widget
    fields = '__all__'

class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'



