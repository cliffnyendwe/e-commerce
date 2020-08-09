from django.urls import path
from django.urls import path, include
from . import views
from .views import (
    ItemDetailView,
    CheckoutView,

    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView
)

app_name = 'ecommerce'

urlpatterns = [
    path('', views.home, name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('mpesa/', include('mpesa_api.core.urls', 'mpesa')),
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('bags', views.bags, name='bags'),
    path('location/(\d+)', views.location, name='location')
]
