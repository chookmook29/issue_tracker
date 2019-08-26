
from django.shortcuts import render
from users.models import CustomUser


def home(request):
    """Dataset is used in d3.js wordcloud in index.html template, users number
       narrowed to five for design reasons"""
    dataset_cloud = CustomUser.objects.all().order_by('-amount_comments')[:8]
    # Different size of databases for both charts to improve readability
    dataset_pie = CustomUser.objects.all().order_by('-amount_comments')[:5]
    return render(request, 'charts.html', {'dataset_cloud': dataset_cloud, 'dataset_pie': dataset_pie})


def info(request):
    return render(request, 'info.html')
