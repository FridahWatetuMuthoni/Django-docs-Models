# Django Models Notes

## Creating and django projects

1. Create a virtual environment and activate it

> > > python -m venv venv

> > > venv\Scripts\activate

2. Install django and create a requirements file

> > > pip install django

> > > pip freeze > requirements.txt

3. Create a django project and app

What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

> > > django-admin startproject mysite .

> > > python manage.py startapp news

4. running a server, you can include the port number

> > > python manage.py runserver

> > > python manage.py runserver 8080

## Models

models are used for creating tables in the database. The table name is the models name and the table fields are the models fields.

## Database Queries

```python
from news.models import Article, Reporter
from datetime import date
from django.utils import timezone


#Getting all the reporters and articles
reporters = Reporter.objects.all()
articles = Article.objects.all()


#Creating a new Reporter
reporter = Reporter(full_name='john smith)
reporter.save()

#Getting the created reporters details
name = reporter.full_name
id = reporter.id
reporter_articles = reporter.article_set.all()
Reporter.objects.get(id=id) or Reporter.objects.get(pk=id)
Reporter.objects.get(full_name=name)
Reporter.objects.get(full_name__startswith='joh')
Reporter.objects.get(full_name__icontains = 'mith')

#Creating a new Article
article = Article(pub_date=date.today(), headline='models django documentation', content='content example one', reporter=reporter)
article.save()

current_year = timezone.now().year
current_articles = Article.objects.get(pub_date__year=current_year)

```

## Database Queries two

Model:

```Python

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
```

Queries:

```python

from polls.models import Choice, Question
from django.utils import timezone

#create a new question

q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()

#gettings its data
id = q.id
question = q.question_text
pub = q.pub_date

#changing the question
q.question_text = 'Whats up?'
q.save()

#queries
Question.objects.all()
Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith='What')
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)
q = Question.objects.get(pk=1)
q.was_published_recently() #True

#choices options
question = Question.objects.get(pk = 1)
question.choice_set.all()
question.choice_set.create(choice_text='Not much', votes=0)
question.choice_set.create(choice_text='The Sky', votes=0)
question.choice_set.create(choice_text='Just hacking agai', votes=0)
question.choice_set.all()
question.choice_set.count()

```

## URLS MAPPING

```python

#Main project URLS
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('/',include('news.urls')),
    path('admin/', admin.site.urls),
]

#Our news app URLS
from django.urls import path
from . import views

urlpatterns = [
    path('articles/<int:year>/', views.year_archive, name='years_archive'),
    path('articles/<int:year>/<int:month>/', views.month_archive, name='month_archive'),
    path('articles/int:year>/<int:month>/<int:pk>/',views.artcle_detail, name='article_detail')
]
```

The code above maps URL paths to Python callback functions (“views”). The path strings use parameter tags to “capture” values from the URLs. When a user requests a page, Django runs through each path, in order, and stops at the first one that matches the requested URL. (If none of them matches, Django calls a special-case 404 view.)
For example, if a user requested the URL “/articles/2005/05/39323/”, Django would call the function news.views.
article_detail(request, year=2005, month=5, pk=39323).
Therefore the view will have access to the paraemeters.
The path function is passed four arguements, two are required: route and view, two are not
required kwargs and name.

## DJANGO VIEWS

Each view is responsible for doing one of two things: Returning an HttpResponse object containing the content for the requested page, or raising an exception such as Http404. The rest is up to you.Generally, a view retrieves data according to the parameters, loads a template and renders the template with the retrieved data. Here’s an example view for year_archive from above:

```python

from django.shortcuts import render
from .models import Article

def year_archive(request, year):
    archive_list = Article.objects.filter(pub_date__year = year)
    context = {
        'year':year,
        'articles':archive_list
    }
    return render(request, 'news/year_archive.html',context)
```
