import os

from django.shortcuts import render, reverse
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def home_page(request):
    """Получение доступных страниц"""
    template_page = 'home.html'
    pages = {
        'Главная страница': reverse('home'),
        # 'Показать текущее время': reverse('current_time'), Шаблон не реализован
        # 'Показать содержимое рабочей директории': reverse('workdir'), Шаблон не реализован
    }

    context = {
        'pages': pages
    }
    return render(request, template_page, context)


def actually_time(request):
    """Получение текущего времени"""
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M")
    msg = f'Текущее время: {formatted_time}'
    return HttpResponse(msg)


def working_directory_contents(request):
    """Получение рабочей директории"""
    project_dir = os.path.dirname(os.path.abspath(__file__))
    files = os.listdir(project_dir)
    return HttpResponse(files)
