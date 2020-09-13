from django import forms

# models.py からクラスとして定義されたモデル（＝DBテーブルになる）を読み込む
from .models import *

class KeywordForm(forms.ModelForm):
  class Meta:
    model = Keyword
    fields = ('text',)
