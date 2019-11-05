from django.shortcuts import render,get_list_or_404
from django.views.generic import DetailView,ListView
from .models import Question
# Create your views here.

class HomeDetailView(ListView):
    model = Question
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Question.objects.order_by('-pub_date')[:5]
        context['data'] = data
        return context
