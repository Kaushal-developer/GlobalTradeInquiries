from django.urls import path
from service import views
app_name='service'

urlpatterns = [
    path("",views.home,name='home'),
    path("filtered-products/", views.filtered_products, name="filtered_products"),

]
