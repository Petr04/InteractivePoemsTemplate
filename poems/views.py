import random

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from poems.models import Poem, Paragraph


def read(request):
	poems = Poem.objects.filter(ended=True)
	pars = Paragraph.objects.filter(poem=random.choice(poems))

	return render(request, 'read.html', {'pars': pars})

def write(request, new=False):
	if request.method == 'GET':
		if new:
			return render(request, 'append.html', {'new': True})

		poems = Poem.objects.filter(ended=False)

		if poems.count() == 0:
			return render(request, 'no_poems.html')

		poem = random.choice(poems)

		pars = Paragraph.objects.filter(poem=poem)

		return render(
			request, 'append.html',
			{'pars': pars, 'id': poem.id, 'new': False}
		)

	if request.method == 'POST':
		if new:
			poem = Poem()
		else:
			poem = Poem.objects.get(pk=request.POST['id'])

		par = Paragraph(
			author=request.POST['author'],
			text=request.POST['text'],
			poem=poem
		)


		if request.POST['button'] == 'write':
			poem.ended = True

		poem.save()
		par.poem = poem

		par.save()

		return redirect('/')

def write_new(request):
	return write(request, new=True)
