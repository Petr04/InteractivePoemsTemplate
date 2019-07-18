import random

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from poems.models import Poem


def read(request):
	# получаем все законченные тексты
	poems = Poem.objects.filter(ended=True)
	if poems.count() == 0:
		return HttpResponse("Пока еще нет готовых.")

	# выбираем случайную
	poem = random.choice(poems)
	# TODO: сделать красивый шаблон
	return HttpResponse(poem.text)


def write(request):
	if request.method == 'GET':
		poems = Poem.objects.filter(ended=False)
		if poems.count() == 0:
			# создаем новый текст
			poem = Poem()
			poem.text = ""
			poem.save()
		else:
			# выбираем один из текущих
			poem = random.choice(poems)
		
		return render(request, 'index.html', {'text': poem.text, 'id': poem.id})

	if request.method == 'POST':
		print(request.POST)
		id = request.POST['id']
		# находим нашу поэму с конкретным id...
		poem = Poem.objects.get(pk=id)

		poem.text += request.POST['text']
		if request.POST['button'] == 'write':
			poem.ended = True

		# сохраняем
		poem.save()
		# TODO: возможно, редирект на конкретный текст
		return redirect('/')
