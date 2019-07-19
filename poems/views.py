import random

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from poems.models import Poem, Paragraph


def read(request):
	poems = Poem.objects.filter(ended=True)
	if poems.count == 0:
		return render(request, 'no_poems.html', {'write': False})

	poem = random.choice(poems)
	pars = Paragraph.objects.filter(poem=poem)

	return render(request, 'read.html', {'name': poem.name, 'pars': pars})

def write(request, new=False):
	if request.method == 'GET':
		if new:
			return render(request, 'write.html', {'new': True})

		poems = Poem.objects.filter(ended=False)

		if poems.count() == 0:
			return render(request, 'no_poems.html', {'write': True})

		poem = random.choice(poems)

		pars = Paragraph.objects.filter(poem=poem, last=True)

		return render(
			request, 'write.html',
			{'name': poem.name, 'pars': pars, 'id': poem.id, 'new': False}
		)

	if request.method == 'POST':
		if new:
			poem = Poem(name=request.POST['name'])
		else:
			poem = Poem.objects.get(pk=request.POST['id'])

			last_par = Paragraph.objects.filter(poem=poem, last=True)[0]
			# Должен быть только один Paragraph, где last == True.
			last_par.last = False
			last_par.save()


		par = Paragraph(
			author=request.POST['author'],
			text=request.POST['text'],
			poem=poem,
			last=True
		)


		if request.POST['button'] == 'write':
			poem.ended = True

		poem.save()
		par.poem = poem

		par.save()

		return redirect('/')

def write_new(request):
	return write(request, new=True)
