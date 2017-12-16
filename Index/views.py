from django.shortcuts import render

from .models import Index
from Goods.models import Product, Kind
from Store.models import Store
from News.models import News
from Base.models import Bow, Tabbar


def index(request):
    all_Indexs = Index.objects.all()
    all_Products = Product.objects.all()
    all_Stores = Store.objects.all()
    all_News = News.objects.all()
    all_Kinds = Kind.objects.all()
    all_Bows = Bow.objects.all()
    all_Tabbars = Tabbar.objects.all()
    context = {
        "all_Products": all_Products,
        "all_Stores": all_Stores,
        "all_News": all_News,
        "all_Indexs": all_Indexs,
        "all_Bows": all_Bows,
        "all_Tabbars": all_Tabbars,
        "all_Kinds": all_Kinds
    }
    return render(request, "index.html", context)