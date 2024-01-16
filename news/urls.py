from django.urls import path 
from . import views


urlpatterns = [
    path('articles/<int:year>/', views.year_archive, name='years_archive'),
    path('articles/<int:year>/<int:month>/', views.month_archive, name='month_archive'),
    path('articles/int:year>/<int:month>/<int:pk>/',views.artcle_detail, name='article_detail')
]