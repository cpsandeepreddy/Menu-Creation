# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from card.models import Data
from django.shortcuts import render,render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.generic.base import TemplateView
from card.forms import *

class Add(TemplateView):
    template_view='add.html'
    def get(self,request):
         form=TestForm()
         return render_to_response('add.html',locals(),context_instance=RequestContext(request))
    def post(self, request):
         form=TestForm(request.POST)
         if form.is_valid():
             title = form.cleaned_data['name']
             types = form.cleaned_data['types']
             ingradients=form.cleaned_data['ingradients']
             time_to_cook=form.cleaned_data['time_to_cook']
             steps=form.cleaned_data['steps']
             Data.objects.create(name=title,types=types,ingradients=ingradients,time_to_cook=time_to_cook,steps=steps)
             HttpResponseRedirect('/')
         else:
             return HttpResponse('Some Problem')
         return HttpResponseRedirect('/')

class Card(TemplateView):
    template_view='card.html'
    def get(self, request):
        s=Data.objects.all()
        return render_to_response('card.html',locals(),context_instance=RequestContext(request))
class Show(TemplateView):
    template_view='show.html'
    def get(self,request,id):
        s=Data.objects.get(id=id)
        return render_to_response('show.html',locals(),context_instance=RequestContext(request))
class Delete(TemplateView):
    def get(self,request,id):
        d=Data.objects.get(id=id)
        d.delete()
        return render(request,'card.html')
