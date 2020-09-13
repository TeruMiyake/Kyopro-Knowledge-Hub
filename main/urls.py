from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('search/', views.search, name='search'),
  path('searchc/', views.searchc, name='searchc'),
  path('searcht/', views.searcht, name='searcht'),
  path('cdetail/<uuid:category_id>', views.cdetail, name='cdetail'),
  path('tdetail/<uuid:tag_id>', views.tdetail, name='tdetail'),
  path('detail/<uuid:keyword_id>', views.detail, name='detail'),
]