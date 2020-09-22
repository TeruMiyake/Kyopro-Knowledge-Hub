from django.db import models
from django.contrib import admin
from django.conf import settings # カスタムユーザーモデルを使うため

from django.urls import reverse # レコード追加後の遷移先指定のため

import uuid # UUIDFieldを使うため

# Create your models here.
# モデルを作ったら、admin.py を編集！


# カテゴリ、タグ
# [keyword_id, category(or tag)_id] の組は unique にしたいが……？

class Category(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  text = models.CharField(max_length=40, unique=True) # カテゴリ名
  votes = models.IntegerField(default=0)
  author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True
  )
  def __str__(self):
    return self.text

class Tag(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  text = models.CharField(max_length=60, unique=True) # タグ名
  votes = models.IntegerField(default=0)
  author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True
  )
  def __str__(self):
    return self.text

class Keyword(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  text = models.CharField(max_length=50, unique=True) # キーワード名
  votes = models.IntegerField(default=0)
  categories = models.ManyToManyField(Category, blank=True)
  tags = models.ManyToManyField(Tag, blank=True)
  author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True
  )
  def __str__(self):
    return self.text
  # create, update成功時の遷移先を定義
  def get_absolute_url(self):
      return reverse("detail", kwargs={'keyword_id': self.id})



# 説明、リンク、問題
# [keyword_id, text(or url)] の組は unique

class Explanation(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  keyword_id = models.ForeignKey(Keyword, on_delete=models.CASCADE)
  text = models.CharField(max_length=100) # 説明
  votes = models.IntegerField(default=0)
  author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True
  )
  def __str__(self):
    return self.text
  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=['keyword_id', 'text'],
        name='unique_expls'
      )
    ]

class LinkForB(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  keyword_id = models.ForeignKey(Keyword, on_delete=models.CASCADE)
  text = models.CharField(max_length=120) # リンクタイトル
  url = models.CharField(max_length=400) # URL
  votes = models.IntegerField(default=0)
  author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True
  )
  def __str__(self):
    return self.text
  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=['keyword_id', 'url'],
        name='unique_lforbs'
      )
    ]

class LinkForA(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  keyword_id = models.ForeignKey(Keyword, on_delete=models.CASCADE)
  text = models.CharField(max_length=120) # リンクタイトル
  url = models.CharField(max_length=400) # URL
  votes = models.IntegerField(default=0)
  author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True
  )
  def __str__(self):
    return self.text
  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=['keyword_id', 'url'],
        name='unique_lforas'
      )
    ]

class Library(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  keyword_id = models.ForeignKey(Keyword, on_delete=models.CASCADE)
  text = models.CharField(max_length=120) # ライブラリへのリンクタイトル
  url = models.CharField(max_length=400) # URL
  votes = models.IntegerField(default=0)
  author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True
  )
  def __str__(self):
    return self.text
  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=['keyword_id', 'url'],
        name='unique_libraries'
      )
    ]

class ProblemForB(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  keyword_id = models.ForeignKey(Keyword, on_delete=models.CASCADE)
  text = models.CharField(max_length=80) # リンクタイトル
  url = models.CharField(max_length=400) # URL
  votes = models.IntegerField(default=0)
  author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True
  )
  def __str__(self):
    return self.text
  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=['keyword_id', 'url'],
        name='unique_pforbs'
      )
    ]

class ProblemForA(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  keyword_id = models.ForeignKey(Keyword, on_delete=models.CASCADE)
  text = models.CharField(max_length=80) # リンクタイトル
  url = models.CharField(max_length=400) # URL
  votes = models.IntegerField(default=0)
  author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.SET_NULL,
    null=True
  )
  def __str__(self):
    return self.text
  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=['keyword_id', 'url'],
        name='unique_pforas'
      )
    ]


