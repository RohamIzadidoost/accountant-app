from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from .models import *
from django.template import RequestContext
from django.urls import reverse
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    p = Paginator(Transaction.objects.all() , 5)
    context = {
        'transactions' : p.page(1).object_list
    }
    return render(request , 'main/main.html' , context)