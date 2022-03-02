
from django.urls import path

from djapp import views  # function based views

from .views import Productreg ,ProductList, ProductDetail , ProductUpdate ,ProductDelete              #Class Based views

urlpatterns = [
    path('home/', views.home, name = "home"),
    path('product/', views.product, name = "product"),
    path('service/', views.service, name = "service"),
    path('contact/', views.contact, name = "contact"),
    path('aboutus/', views.aboutus, name = "aboutus"),
#FBV
    path('get_product/', views.get_product, name = "get_product"),
    path('detail_product/<pk>', views.detail_product, name = "detail_product"),
    path('update_product/<pk>', views.update_product, name = "update_product"),
     path('delete_product/<pk>', views.delete_product, name = "delete_product"),

# CBV

 path('Productreg/', Productreg.as_view(), name = 'Productreg'),
 path('', ProductList.as_view(), name = 'ProductList'),
 path('<pk>/ProductDetail/', ProductDetail.as_view(), name = 'ProductDetail'),
 path('<pk>/ProductUpdate/', ProductUpdate.as_view(), name = 'ProductUpdate'),
path('<pk>/ProductDelete/', ProductDelete.as_view(), name = 'ProductDelete'),
      
    
]
