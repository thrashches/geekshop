from django.shortcuts import get_object_or_404, HttpResponseRedirect, render
from .models import Basket
from mainapp.models import Product
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.conf import settings
#from django.views.generic import ListView


# Create your views here.
'''
class View(ListView):
    model = Basket
    template_name = 'basket.html'
'''


@login_required
def view(request):
    basket = Basket.objects.filter(user=request.user)
    context = {
        "basket": basket
    }
    pass
    return render(request, 'basket.html', context)


@login_required
def add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove(request, pk):
    item = get_object_or_404(Basket, pk=pk)
    item.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required
def edit(request, pk, quantity):
    if request.is_ajax():
        print(pk, quantity)
        basket_item = Basket.objects.get(pk=int(pk))

        if quantity > 0:
            basket_item.quantity = quantity
            basket_item.save()
        else:
            basket_item.delete()

        items = Basket.objects.filter(user=request.user)
        content = {'basket': items, 'media_url': settings.MEDIA_URL}
        result = render_to_string('includes/inc_prod_list.html', content)
        return JsonResponse({"result": result})
