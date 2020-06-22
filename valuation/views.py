from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment, Rate
from item.models import Items
from django.urls import reverse
from django.db.models import Q
# Create your views here.
class RateComment(LoginRequiredMixin, CreateView):
    template_name='create_comment.html'
    model=Comment
    fields=['text']
    def get_success_url(self, **kwargs):
        pk=self.kwargs['pk']
        return reverse('itemdetail', kwargs={'pk':pk})
    def form_valid(self, form):
        print(self.request.POST)
        item=Items.objects.get(pk=self.kwargs.get('pk'))
        user=self.request.user
        self.object=form.save(commit=False)
        self.object.user=user
        self.object.item=item
        self.object.save()
        if self.request.POST.get('rating'):
            Rate.objects.create(item=item,user=user,rate=int(self.request.POST.get('rating')))
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Rate.objects.filter(Q(user=self.request.user)&Q(item=Items.objects.get(pk=self.kwargs.get('pk')))):
            context["item"] = False
        else:
            context["item"] = True
        return context
