from django.shortcuts import render
from service import serializers
# Create your views here.
from service import models
def home(request):
    products = models.Product.objects.all()
    categories = models.Category.objects.all()
    products_data = serializers.ProductSerializer(products,many=True).data
    category_data = serializers.CategorySerializer(categories,many=True).data
    offers = models.Offer.objects.filter(is_active=True).all()
    print(offers)
    return render(request,'index.html',{'products':products_data,'category':category_data,"offers":offers})