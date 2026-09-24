from django.urls import path
from .views import *
urlpatterns=[
    path('',index_view, name='index_page'),
    path('courses/',courses_view, name='courses_page'),
    path('login/',login_view, name='login_page'),
    path('register/',register_view, name='register_page'),
    path('logout/',Logout_view,name='logout_page'),
    path('forget/',forget_pass_view,name='forget_pass_page'),
    path('add_to_cart/<int:product_id>/',add_to_cart_view,name='add_to_cart'),
    path('cart_count/',cart_count,name='cart_count'),
    path('cartItems/',cart_items,name='cartItems'),
    path('update_cart_item/<int:product_id>/<str:action>/', update_cart_item, name='update_cart_item'),


    path('viewdetails/<int:product_id>/',view_details,name='view_details'),
]