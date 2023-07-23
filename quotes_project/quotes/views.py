
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Author, Quote


def index(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/index.html', {'quotes': quotes})


def author_detail(request, author_id):
    author = Author.objects.get(pk=author_id)
    quotes = Quote.objects.filter(author=author)
    return render(request, 'quotes/author_detail.html', {'author': author, 'quotes': quotes})


@login_required
def add_author(request):
    if request.method == 'POST':
        name = request.POST['name']
        author = Author.objects.create(name=name)
        return redirect('author_detail', author_id=author.pk)
    return render(request, 'quotes/add_author.html')


@login_required
def add_quote(request):
    if request.method == 'POST':
        text = request.POST['text']
        author_id = request.POST['author']
        author = Author.objects.get(pk=author_id)
        quote = Quote.objects.create(text=text, author=author)
        return redirect('author_detail', author_id=author.pk)

    authors = Author.objects.all()
    return render(request, 'quotes/add_quote.html', {'authors': authors})
