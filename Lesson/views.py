from django.shortcuts import render, get_object_or_404

from .models import Lesson, Theme
from Goods.models import Kind

def lesson(request):
    all_Lessons = Lesson.objects.all()
    all_Themes = Theme.objects.all()
    all_Kinds = Kind.objects.all()
    context = {
        "all_Themes": all_Themes,
        "all_Lessons": all_Lessons,
        "all_Kinds": all_Kinds
    }
    return render(request, "lesson.html", context)