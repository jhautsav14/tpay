from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name ="home"),
    path('login/', login_page, name ="login"),
    path('logout/', logout_page, name ="logout"),
    path('register/', register_page, name ="register"),
    path('change_db/', change_db, name ="change_dbp"),
    path('payment/', payment, name='payment'),
    path('orders/', orders, name="orders")

]
