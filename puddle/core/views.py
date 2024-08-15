from django.shortcuts import render,redirect
from item.models import Category,Item
# from .forms import SignupForm
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.core.mail import send_mail

from django.conf import settings

# Create your views here.

def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    return render(request,'core/index.html',{
        'category':categories,
        'items':items,
    })


def contact(request):
    return render(request,'core/contact.html') 



class userreg(generic.CreateView):
    form_class = userregform
    template_name = 'core/signup.html'
    success_url = reverse_lazy('core:login')
    def form_valid(self, form):
        user =form.save(commit=False)
        password=form.cleaned_data['password']
        user.set_password(password)
        user.save()
        userdetails.objects.create(user=user)
        return super().form_valid(form)   
    

class userlogin(generic.View):
    form_class=AuthenticationForm
    template_name='core/login.html'
    def get(self,request):
        data=User.objects.all()
        for i in data:
            request.session['userid']=i.id
        form=AuthenticationForm
        return render(request,'core/login.html',{'form':form})
    def post(self,request):
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('core:index')
            else:
                return HttpResponse('Invalid credentials...')
        else:
            return HttpResponse('Form is invalid...')    
        
        