from django.shortcuts import render
from catalog.models import Item


def home(request):
    template = 'homepage/index.html'
    MAX_TEXT_WORDS = 10
    items = Item.objects.filter(is_on_main=True).order_by('name')
    # ' '.join(text.split(' ', MAX_TEXT_WORDS))[:-1]
    context = {
        'MAX_TEXT_WORDS': MAX_TEXT_WORDS,
        'items': items
    }
    return render(request, template, context)
