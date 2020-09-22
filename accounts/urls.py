from django.urls import path


from . import views

urlpatterns = [
  path('', views.index, name='accountsindex'),
  # signup はデフォルトで用意されていないため
  path('signup/', views.SignUpView.as_view(), name='signup'),
]