from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from item.models import Items
from django.urls import reverse
from .forms import OrderForm
from django.urls import reverse_lazy
from .models import Order, Promocodes, Particle
from django.contrib import messages
from valuation.models import OrderComment
from .filters import OrderFilter
from django.db.models import Q
class Cart(LoginRequiredMixin, ListView):
    template_name='cart.html'
    model=Items
    context_object_name='list'
    def get_queryset(self):
        try:
            return Items.objects.filter(pk__in=self.request.session['items'].keys())
        except:
            return Items.objects.none()
class Refresh(LoginRequiredMixin,RedirectView):
    def get(self,request, *args, **kwargs):
        try:
            for key in request.GET:
                request.session['items'][key]=int(request.GET[key])
                request.session.modified=True
        except:
            print('refresh')
        return super().get(request, *args, **kwargs)
    def get_redirect_url(self, *args, **kwargs):
        return reverse('cart')
class DeleteItemCart(LoginRequiredMixin,RedirectView):
    def get(self, request, *args, **kwargs):
        request.session['items'].pop(str(kwargs['pk']))
        request.session.modified=True
        return super().get(request, *args, **kwargs)
    def get_redirect_url(self, *args, **kwargs):
        return reverse('cart')
class CheckoutView(LoginRequiredMixin,CreateView):
    template_name='checkout.html'
    form_class=OrderForm
    success_url=reverse_lazy('index')
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        self.object.suma=0
        for key in self.request.session['items']:
            Particle.objects.create(order=self.object, item=Items.objects.get(pk=int(key)), amount=self.request.session['items'][key])
            self.object.suma+=(Items.objects.get(pk=int(key)).price*self.request.session['items'][key])

        if self.request.session.get('promocode'):
            self.object.suma+=self.request.session['promocode']
        self.object.save()
        messages.success(self.request, 'The order was created')
        return super().form_valid(form)
    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        try:
            context['items'] = Items.objects.filter(pk__in=self.request.session['items'].keys())
        except:
            pass
        return context
class Promocode(LoginRequiredMixin,RedirectView):
    def get(self, request, *args, **kwargs):
        value=Promocodes.objects.filter(name=request.GET.get('promocode'))
        for i in value:
            request.session['promocode']=i.value
            request.session.modified=True
            messages.success(request, 'Promocode was added')
        return super().get(request, *args, **kwargs)
    def get_redirect_url(self, *args, **kwargs):
        return reverse('checkout')
class OrderList(LoginRequiredMixin,ListView):
    model=Order
    template_name='order_list.html'
    context_object_name='list'
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
class OrderDetail(LoginRequiredMixin,DetailView):
    model=Order
    template_name='order_detail.html'
    context_object_name='order'
class OrderCommentView(LoginRequiredMixin,RedirectView):
    model=OrderComment
    def get_redirect_url(self,*args, **kwargs):
        return reverse('orderdetail', kwargs={'pk':kwargs.get('pk')})
    def get(self, request, *args, **kwargs):
        if request.method == 'POST':
            print(request.POST.get('text'))
            if request.POST.get('text'):
                OrderComment.objects.create(order=Order.objects.get(pk=kwargs.get('pk')),
                                            text=request.POST.get('text')
                                            )
        return super().get(request, *args, **kwargs)
class StaffOrderView(UserPassesTestMixin ,ListView):
    def test_func(self):
        return self.request.user.is_staff
    model=Order
    template_name='staff_order_list.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        orders=Order.objects.filter(Q(manager=None)|Q(manager=self.request.user.username))
        context['orders']=orders
        return context
class OrderUpdate(UserPassesTestMixin,UpdateView):
    def test_func(self):
        if Order.objects.get(pk=self.kwargs.get('pk')).manager==self.request.user.username or Order.objects.get(pk=self.kwargs.get('pk')).manager==None:
            return True
        else:
            return False
    model=Order
    template_name='update_order.html'
    fields=['first_name','last_name','phone','city','status','payment_data','manager','delivery','filial_number']
