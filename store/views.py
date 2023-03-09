from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, FormView
from .forms import *
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Clothes
    template_name = 'store/Home_View.html'
    context_object_name = 'home'


class CategoriesView(ListView):
    model = Clothes
    template_name = 'store/Categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Clothes.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class CategoryView(ListView):
    paginate_by = 6
    model = Clothes
    template_name = 'store/Category_View.html'
    context_object_name = 'category'


class DetailViews(DetailView):
    model = Clothes
    template_name = 'store/Detail_View.html'
    context_object_name = 'detail_category'


class PaymentForm(FormView):
    form_class = ClothesForm
    template_name = 'store/payment.html'
    success_url = reverse_lazy('detail_page')




"""
def categories(request, category_id):
    clothes = Clothes.objects.filter(category_id=category_id)
    categories_item = Category.objects.all()
    category = Category.objects.get(pk=category_id)

    context = {'clothes': clothes, 'categories_item': categories_item, 'category': category, 'title': "List of Clothes"}

    return render(request, template_name='store/category.html', context=context)
"""
