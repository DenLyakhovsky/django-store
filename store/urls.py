from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('categories/', CategoryView.as_view(), name='categories_page'),
    path('category/<int:category_id>/', CategoriesView.as_view(), name='category'),
    path('clothes/<int:pk>', DetailViews.as_view(), name='detail_page'),
    path('payment/', PaymentForm.as_view(), name='payment_page'),
]
