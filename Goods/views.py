from django.shortcuts import render, get_object_or_404

from .models import Product, Theme, Kind
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

def goods(request):
    all_Products = Product.objects.all()
    all_Themes = Theme.objects.all()
    all_Kinds = Kind.objects.all()


    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(all_Products, 8, request=request)

    prod = p.page(page)

    context = {
        "all_Products": prod,
        "all_Themes": all_Themes,
        "all_Kinds": all_Kinds
     }
    return render(request, "goods.html", context)


def base(request):
    all_Kinds = Kind.objects.all()
    all_Products = Product.objects.all()
    context = {
        "all_Products": all_Products,
        "all_Kinds": all_Kinds
    }
    return render(request, "base.html", context)


def goodsdet(request, pk):
    all_Themes = Theme.objects.all()
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'goods-det.html', context={"all_Themes": all_Themes, 'product': product})

