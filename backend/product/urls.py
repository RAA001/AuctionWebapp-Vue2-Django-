from django.urls import path, include

from product import views

urlpatterns = [
    path('l-products/', views.ProductsList),
    path('products/', views.ProductsList1),
    path('questions123/', views.qs),
    path('answers/', views.answ),
    path('bids/', views.Bidsview),
    path('profile/', views.ProfileList),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
    path('', views.login_v, name="login"),
    path('signup/', views.signup_v, name="signup"),
    path('logout/', views.logout_v, name='logout'),
    path('profiledet/', views.Profile_detail),
    path('profileimage/', views.Profileimage),
    path('emailspage/', views.Emailpage),
]