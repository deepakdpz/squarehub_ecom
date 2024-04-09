from django.urls import path
from shop import views

urlpatterns=[
    
    path("register/",views.SignUpView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name="signin"),
    path("logout/",views.LogoutView.as_view(),name="logout"),
    path("home/",views.HomeView.as_view(),name="home"),
    path("products/<int:pk>",views.DetailView.as_view(),name="detail"),
    path("products/<int:pk>/carts/add/",views.AddToCartView.as_view(),name="add-to-cart"),
    path("carts/all",views.CartItemListView.as_view(),name="cart-list"),
    path("basket/items/<int:pk>/remove",views.CartItemDeleteView.as_view(),name="basketitem-delete"),
    path("basket/item/<int:pk>/quantity/change",views.CartItemUpdateQuantityView.as_view(),name="basket-item-qty-update"),
    path("checkout/",views.CheckOutView.as_view(),name="checkout"),
    path("orders/all",views.MyOrderView.as_view(),name="orders"),
    path("verify/",views.PaymenntVerificationView.as_view(),name="verification"),
    
]