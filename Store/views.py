from django.shortcuts import render, get_object_or_404

from .models import Store, Theme
from Goods.models import Kind
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


def store(request):
    all_Stores = Store.objects.all()
    all_Themes = Theme.objects.all()
    all_Kinds = Kind.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(all_Stores, 6, request=request)

    shop = p.page(page)

    context = {
        "all_Themes": all_Themes,
        "all_Stores": shop,
        "all_Kinds": all_Kinds
    }
    return render(request, "store.html", context)


def storedet(request, pk):
    all_Themes = Theme.objects.all()
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'store-det.html', context={"all_Themes": all_Themes, 'store': store})
