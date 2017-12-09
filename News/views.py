from django.shortcuts import render, get_object_or_404

from .models import News,Theme
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from Goods.models import Kind

def news(request):
    all_News = News.objects.all()
    all_Themes = Theme.objects.all()
    all_Kinds = Kind.objects.all()

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(all_News, 6, request=request)

    newss = p.page(page)

    context = {
        "all_Themes": all_Themes,
        "all_News": newss,
        "all_Kinds": all_Kinds
     }
    return render(request, "news.html", context)

def newsdet(request, pk):
    all_Themes = Theme.objects.all()
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news-det.html', context={"all_Themes": all_Themes, 'news': news})


