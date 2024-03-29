from django.shortcuts import render, get_object_or_404

from catalog.models import Item


def item_list(request):
    template = 'catalog/list.html'
    items = Item.objects.published()
    context = {
        'items': items,
    }
    return render(request, template, context)


def item_detail(request, pk):
    template = 'catalog/detail.html'
    item = get_object_or_404(Item.objects.published(), pk=pk)
    context = {
        'item': item,
    }
    return render(request, template, context)
