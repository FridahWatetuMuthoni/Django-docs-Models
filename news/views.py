from django.shortcuts import render
from .models import Article

def year_archive(request, year):
    archive_list = Article.objects.filter(pub_date__year = year)
    context = {
        'year':year,
        'articles':archive_list
    }
    print(context)
    return render(request, 'news/year_archive.html',context)