import random

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from poems.models import Poem


def read(request):
    # получаем все закончиенные тексты
    poems = Poem.objects.filter(ended=True)
    if poems.count() == 0:
        return HttpResponse("Пока еще нет готовых.")

    # выбираем случайную
    poem = random.choice(poems)
    # TODO: сделать красивый шаблон
    return HttpResponse(poem.text)


def write(request):
    if request.method == 'GET':
        # TODO: стоит добавить возможность добавить возможность написать с нуля, даже если тексты уже есть
        poems = Poem.objects.filter(ended=False)
        if poems.count() == 0:
            # создаем новый текст
            poem = Poem()
            poem.text = ""
            poem.save()
        else:
            # выбираем один из текущих
            poem = random.choice(poems)
        # TODO: сделать шаблон для написания абзаца

    if request.method == 'POST':
        id = request.POST['id']
        # находим нашу поэму с конкретным id...
        poem = Poem.objects.get(pk=id)

        if request.POST['button'] == 'Добавить':
            poem.text = poem.text + request.POST['text']
        else:
            poem.text = poem.text + request.POST['text']
            poem.ended = True

        # сохраняем
        poem.save()
        # TODO: возможно, редирект на конкретный текст
        return redirect('/')
