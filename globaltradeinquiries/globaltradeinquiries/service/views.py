from django.shortcuts import render
from service import serializers
# Create your views here.
from service import models
from django.core.paginator import Paginator


def home(request):
    products = models.Product.objects.all()
    categories = models.Category.objects.all()
    products_data = serializers.ProductSerializer(products,many=True).data
    category_data = serializers.CategorySerializer(categories,many=True).data
    offers = models.Offer.objects.filter(is_active=True).all()
    print(offers)
    return render(request,'index.html',{'products':products_data,'categories':category_data,"offers":offers})


def filtered_products(request):
    page_number = int(request.GET.get('page', 1))
    category = request.GET.get('category')

    products = models.Product.objects.all()

    if category:
        products = products.filter(category=category)

    paginator = Paginator(products, 12)  # Show 12 products per page
    page_obj = paginator.get_page(page_number)

    return render(request, 'filtered_products.html', {'page_obj': page_obj})