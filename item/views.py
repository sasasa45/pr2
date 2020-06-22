from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import *
from .models import Items, Categories
from .filter import CategoryFilter,SearchFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
class ItemsIndex(ListView):
    template_name='index.html'
    queryset=Items.objects.all().order_by('?')[:8]
    context_object_name='item_list'
class CategoriesDetail(DetailView):
    template_name='category_list.html'
    model=Categories
    slug_field='name'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        items=Categories.objects.get(name=kwargs.get('object')).items_set.all()
        filter=CategoryFilter(self.request.GET,queryset=items)
        context['filter_form']=filter
        context['items']= filter.qs
        context['category']= Categories.objects.get(name=kwargs.get('object'))
        return context
class ItemsSearch(ListView):
    template_name='search_item.html'
    model=Items
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        lib={}
        if len(self.request.GET.get('search'))>2:
            items=Items.objects.all()
        else:
            items=Items.objects.none()
        filter=SearchFilter(self.request.GET,queryset=items)
        for cat in Categories.objects.all():
            count=0
            for i in filter.qs:
                if i.category==cat:
                    count+=1
                    lib[cat.name]=count
        context['filter_form']=filter
        context['items']= filter.qs
        context['category']= lib
        return context
class ItemDetail(DetailView):
    template_name='item_detail.html'
    model=Items
    context_object_name='item'
@login_required
def like(request,pk):
    item=get_object_or_404(Items,pk=pk)
    item.like.add(request.user)
    messages.success(request,'The Item was added to favorites!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
@login_required
def unlike(request,pk):
    item=get_object_or_404(Items,pk=pk)
    item.like.remove(request.user)
    messages.success(request,'The Item was removed from favorites!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
@login_required
def add_to_cart(request,pk):
    if  'items' not in request.session:
        request.session['items']={}
    request.session['items'][pk]=1
    request.session.modified=True
    messages.success(request,'The Item was added to CART!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
class LikeView(LoginRequiredMixin,ListView):
    template_name='likes.html'
    context_object_name='items'
    def get_queryset(self):
        print(self.request.user.items_set.all())
        return self.request.user.items_set.all()
