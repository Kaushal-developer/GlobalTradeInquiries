from django.urls import path
from service import views
app_name='service'

urlpatterns = [
    path("",views.home,name='home')

]
