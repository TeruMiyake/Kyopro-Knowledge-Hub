from django.contrib import admin

# 作成したモデルのインポート
from main.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Keyword)
admin.site.register(Explanation)
admin.site.register(LinkForB)
admin.site.register(LinkForA)
admin.site.register(Library)
admin.site.register(ProblemForB)
admin.site.register(ProblemForA)