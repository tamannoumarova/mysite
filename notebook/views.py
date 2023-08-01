from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DetailView
)
from notebook.models import Notebook, Brand
from notebook.forms import NotebookForm


class IndexView(TemplateView):
    template_name = "index.html"


class NotebookListView(ListView):
    model = Notebook
    template_name = "list.html"
    context_object_name = "notebooks"

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get("search")
        brand = self.request.GET.get("brand")
        group_id = self.request.GET.get("group_id")

        if search:
            queryset = queryset.filter(
                Q(name__contains=search) | Q(brand__contains=search)
            )
        if brand:
            queryset = queryset.filter(gender=brand)
        if group_id:
            queryset = queryset.filter(group_id=group_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["groups"] = Brand.objects.all()

        context["search"] = self.request.GET.get("search", "")
        context["brand"] = self.request.GET.get("brand")
        group_id = self.request.GET.get("group_id", "")
        if group_id:
            group_id = int(group_id)
        else:
            group_id = 0
        context["group_id"] = group_id
        return context


class NotebookCreateView(CreateView):
    model = Notebook
    form_class = NotebookForm
    success_url = "/notebooks/list/"
    template_name = "form.html"


class NotebookUpdateView(UpdateView):
    model = Notebook
    form_class = NotebookForm
    success_url = "/notebooks/list/"
    template_name = "form.html"


class NotebookDetailView(DetailView):
    model = Notebook
    template_name = "detail.html"
    context_object_name = "notebook"


def notebook_delete(request, pk):
    notebook = get_object_or_404(Notebook, pk=pk)
    notebook.delete()
    return redirect("notebooks-list")
