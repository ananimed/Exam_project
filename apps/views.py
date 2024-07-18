from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import FormView, ListView

from apps.forms import RegisterForm, ProfileForm
from apps.models import Product, Category, User


class RegisterFormView(FormView):
    form_class = RegisterForm
    template_name = 'auth/register.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return redirect('login')


class ProfileFormView(LoginRequiredMixin,FormView):
    form_class = ProfileForm
    template_name = 'auth/profile.html'

    def form_valid(self, form):
        if form.is_valid():
            User.objects.filter(pk=self.request.user.pk).update(**form.cleaned_data)
        return redirect('profile')


class ProductListView(LoginRequiredMixin, ListView):
    queryset = Product.objects.all()
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        cat_slug = self.request.GET.get("category")
        query = super().get_queryset()
        if cat_slug:
            query = query.filter(category__slug=cat_slug)
        return query

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = Category.objects.all()
        return data
