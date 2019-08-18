
from django.shortcuts import render
from users.models import CustomUser


def home(request):
    """Dataset is used in d3.js wordcloud in index.html template, users number
       narrowed to five for design reasons"""
    dataset = CustomUser.objects.all().order_by('-amount_comments')[:7]
    return render(request, 'charts.html', {'dataset': dataset})


def info(request):
    return render(request, 'info.html')
