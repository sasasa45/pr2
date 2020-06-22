from django.shortcuts import render
from django.views.generic import *
from .forms import *
from django.contrib.auth.models import User
from django.urls import reverse_lazy,reverse
from .models import Customer
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
class SignUpView(CreateView):
    template_name='sign.html'
    form_class=SignupForm
    model=User
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.request.POST.get('password1'))
        self.object.save()
        Customer.objects.create(user=self.object)
        self.kwargs['pk']=Customer.objects.get(user=self.object).pk
        return super().form_valid(form)
    def get_success_url(self):
         print('sdfsdfdsfsd')
         return reverse('customer_create',kwargs={'pk':self.kwargs['pk']})

@login_required
def customerupdate(request):
    user=request.user
    customer=Customer.objects.get(user=user)
    if request.method=='POST':
        user_form=UserForm(request.POST,instance=user)
        customer_form=CustomerForm(request.POST, request.FILES,instance=customer)
        if user_form.is_valid()  and customer_form.is_valid():
            user_form.save()
            cust=customer_form.save(commit=False)
            # if request.FILES.get('picture'):
            #     cust.picture=request.FILES['picture']
            #     print('aaa')
            cust.save()
    else:
        user_form=UserForm(instance=user)
        customer_form=CustomerForm(instance=customer)


    context={'user':user_form,'customer':customer_form,'pic':customer.picture}
    return render(request,'profile.html',context)
