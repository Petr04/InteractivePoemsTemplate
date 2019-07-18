import random

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from poems.models import Poem


def read(request):
	# получаем все законченные тексты
	poems = Poem.objects.filter(ended=True)
	if poems.count() == 0:
		return render(request, 'no_poems.html')

	# выбираем случайную
	poem = random.choice(poems)

	return render(request, 'read.html', {'text': poem.text})


def write(request):
	if request.method == 'GET':
		poems = Poem.objects.filter(ended=False)
		if poems.count() == 0:
			return render(request, 'no_poems.html')
		else:
			# выбираем один из текущих
			poem = random.choice(poems)
		
		return render(request, 'append.html', {'text': poem.text, 'id': poem.id})

	if request.method == 'POST':
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

def write_new(request):
	if request.method == 'GET':
		return render(request, 'write_new.html')

	if request.method == 'POST':
		poem = Poem()
		poem.text = request.POST['text']
		poem.save()

		return redirect('/')
