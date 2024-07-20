from django.shortcuts import render, redirect
from django.core.validators import ValidationError
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import (
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
)
from django.forms import inlineformset_factory
from catalog.models import Category, Product, Contacts, Version
from .forms import CreateProduct, VersionForm

# Create your views here.


class ContactPageView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            admin_contact = Contacts.objects.get(pk=1).__dict__
            admin_data = {
                "name": admin_contact["name"],
                "address": admin_contact["address"],
                "phone": admin_contact["phone"],
            }
            context["admin_data"] = admin_data
        except Contacts.DoesNotExist:
            return JsonResponse({"error": "Contact not found"}, status=404)
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST["name"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        print({"name": name, "phone": phone, "message": message})
        return self.get(request, *args, **kwargs)


class HomePageView(TemplateView):
    template_name = "catalog/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all().order_by("id")
        paginator = Paginator(products, 3)  # 3 products per page
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context["page_obj"] = page_obj
        return context


class ProdcutDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"


class CreateProductView(CreateView):
    form_class = CreateProduct
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:products_list")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1
        )

        if self.request.method == "POST":
            context_data["formset"] = VersionFormset(self.request.POST)

        else:
            context_data["formset"] = VersionFormset()

        return context_data

    def form_valid(self, form):
        """Метод для проверки валидации формы и формсета"""
        context_data = self.get_context_data()
        formset = context_data["formset"]
        # Задаем условие, при котором д.б. валидными и форма и формсет
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            # save() данная функция сохраняет внесенные изменения
            formset.save()
            return super().form_valid(form)

        else:
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "catalog/product_form.html"
    form_class = CreateProduct

    def get_success_url(self):
        """Метод для определения пути, куда будет совершен переход после редактирования продкута"""
        return reverse_lazy(
            "catalog:product_detail", args=[self.get_object().pk]
        )

    def get_context_data(self, **kwargs):
        """Метод для создания Формсета и настройки его работы"""
        context_data = super().get_context_data(**kwargs)

        VersionFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1
        )

        if self.request.method == "POST":
            context_data["formset"] = VersionFormset(
                self.request.POST, instance=self.object
            )

        else:
            context_data["formset"] = VersionFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        """Метод для проверки валидации формы и формсета"""
        context_data = self.get_context_data()
        formset = context_data["formset"]

        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object

            current_versions = 0
            for version_form in formset:
                if version_form.cleaned_data.get("is_current"):
                    current_versions += 1

            if current_versions > 1:
                form.add_error(
                    None, "Только одна версия может быть помечана как активная."
                )
                return self.render_to_response(
                    self.get_context_data(form=form, formset=formset)
                )
            formset.save()
            return super().form_valid(form)

        else:
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )
