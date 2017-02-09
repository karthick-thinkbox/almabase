from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
 
from django.views.generic.list import ListView
from .models import Inventory
from django.template import Template,context
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from  django.db.models import Q



class gamelist(ListView):
    model=Inventory
    template_name='home.html'
    
    
    def get_queryset(self):
        filter=self.request.GET.get('filter' ,'')
        sort=self.request.GET.get('sortchoice' ,'')
        order=self.request.GET.get('order' ,'')
        qs=super(gamelist,self).get_queryset()
        
    
        if filter== '' and sort=='':
            
            return Inventory.objects.all()
        elif filter:
            return (Inventory.objects.filter(Q(title__icontains = filter) | Q(platform__icontains = filter) )).order_by('-score')
        elif sort and order=='asc' :
            return Inventory.objects.all().order_by(sort)
        elif sort and order=='dsc' :
            return Inventory.objects.all().order_by('-'+sort)
        
        
            
    
    
class detail(DetailView):
    
    model=Inventory
    template_name='detail_page.html'
    
def logout_page(request):
    logout(request)
    return render (request,'logout.html')

# Create your views here.
