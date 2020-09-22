from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q # 検索

# クラスベースビューのデコレート（login_required）をするため、method_decorator も必要になる
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# クラスベース汎用ビューのインポート
# レコード追加ビュー
from django.views.generic.edit import CreateView

# models.py からクラスとして定義されたモデル（＝DBテーブルになる）を読み込む
from .models import * # Keyword, Explanation, LinkForB, LinkForA

# forms.py からクラスとして定義されたフォームを読み込む
from .forms import *

# Create your views here.

def index(request):
  return render(request, 'main/index.html')

def search(request):
  # 検索窓の input で指定した name='qk' を使って受け取る
  searchword = request.GET.get('qk')
  if searchword:
    keywords = Keyword.objects.all()
    keywords = keywords.filter(
      Q(text__icontains=searchword) # icontains : 部分一致
    ).distinct() # 重複を省く（要るか？？modelsで重複を禁止すればいいのでは）
  else:
    keywords = Keyword.objects.all()
  return render(request, 'main/search.html', {'keywords':keywords, 'searchword':searchword})

# カテゴリを探す
def searchc(request):
  # 検索窓の input で指定した name='qc' を使って受け取る
  searchword = request.GET.get('qc')
  if searchword:
    categories = Category.objects.all()
    categories = categories.filter(
      Q(text__icontains=searchword) # icontains : 部分一致
    ).distinct() # 重複を省く（要るか？？modelsで重複を禁止すればいいのでは）
  else:
    categories = Category.objects.all()
  return render(request, 'main/searchc.html', {'categories':categories, 'searchword':searchword})

# タグを探す
def searcht(request):
  # 検索窓の input で指定した name='qt' を使って受け取る
  searchword = request.GET.get('qt')
  if searchword:
    tags = Tag.objects.all()
    tags = tags.filter(
      Q(text__icontains=searchword) # icontains : 部分一致
    ).distinct() # 重複を省く（要るか？？modelsで重複を禁止すればいいのでは）
  else:
    tags = Tag.objects.all()
  return render(request, 'main/searcht.html', {'tags':tags, 'searchword':searchword})



def detail(request, keyword_id):
  keyword = get_object_or_404(Keyword, id=keyword_id)
  # 検索
  expls = Explanation.objects.all()
  expls = expls.filter(
    Q(keyword_id__exact=keyword_id)
  ).distinct().order_by("-votes")

  lforbs = LinkForB.objects.all()
  lforbs = lforbs.filter(
    Q(keyword_id__exact=keyword_id)
  ).distinct().order_by("-votes")

  lforas = LinkForA.objects.all()
  lforas = lforas.filter(
    Q(keyword_id__exact=keyword_id)
  ).distinct().order_by("-votes")

  libraries = Library.objects.all()
  libraries = libraries.filter(
    Q(keyword_id__exact=keyword_id)
  ).distinct().order_by("-votes")
  
  pforbs = ProblemForB.objects.all()
  pforbs = pforbs.filter(
    Q(keyword_id__exact=keyword_id)
  ).distinct().order_by("-votes")

  pforas = ProblemForA.objects.all()
  pforas = pforas.filter(
    Q(keyword_id__exact=keyword_id)
  ).distinct().order_by("-votes")

  categories = keyword.categories.all().order_by("-votes")
  
  tags = keyword.tags.all().order_by("-votes")

  return render(request, 'main/detail.html', {'keyword_text':keyword.text, 'expls':expls, 'lforbs':lforbs, 'lforas':lforas, 'libraries':libraries, 'pforbs':pforbs, 'pforas':pforas, 'categories':categories, 'tags':tags})


# あるタグを持つキーワード一覧を表示
def tdetail(request, tag_id):
  tag = get_object_or_404(Tag, id=tag_id)
  keywords = Keyword.objects.filter(tags=tag)
  return render(request, 'main/tdetail.html', {'keywords':keywords, 'tag':tag})

# あるカテゴリを持つキーワード一覧を表示
def cdetail(request, category_id):
  category = get_object_or_404(Category, id=category_id)
  keywords = Keyword.objects.filter(categories=category)
  return render(request, 'main/cdetail.html', {'keywords':keywords, 'category':category})


# クラスベース汎用ビューを使ってみる

# レコードの追加を行う
# CreateView（やUpdateView）は、object ではなく、form という変数を生成するらしい？
@method_decorator(login_required, name='dispatch')
class MyCreateView(CreateView):
  model = Keyword
  fields = ("text", "categories", "tags", )
  template_name = "main/create.html"