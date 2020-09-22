from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.urls import reverse_lazy

# 自分で定義したもの
from .forms import CustomUserCreationForm

# Create your views here.

# 
def index(request):
  return render(request, 'registration/home.html')

# アカウント作成
class SignUpView(CreateView):
  form_class = CustomUserCreationForm #ここを変更
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'
