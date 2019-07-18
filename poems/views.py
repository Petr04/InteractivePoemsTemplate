import random

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from poems.models import Poem, Paragraph


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

		poem = random.choice(poems)

		pars = Paragraph.objects.filter(poem=poem)

		return render(request, 'append.html', {'pars': pars, 'id': poem.id})

	if request.method == 'POST':
		poem = Poem.objects.get(pk=request.POST['id'])

		par = Paragraph(
			author=request.POST['author'],
			text=request.POST['text'],
			poem=poem
		)

		par.save()

		if request.POST['button'] == 'write':
			poem.ended = True
			poem.save()

		return redirect('/')

def write_new(request):
	if request.method == 'GET':
		return render(request, 'write_new.html')

	if request.method == 'POST':
		poem = Poem()
		par = Paragraph(
			poem=poem,
			author=request.POST['author'],
			text=request.POST['text']
		)

		poem.save()
		par.save()

		return redirect('/')
