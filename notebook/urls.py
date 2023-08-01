from django.urls import path
from notebook import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path(
        "notebooks/list/",
        views.NotebookListView.as_view(),
        name="notebooks-list"
    ),
    path(
        "notebooks/create/",
        views.NotebookCreateView.as_view(),
        name="notebooks-create"
    ),
    path(
        "notebooks/<int:pk>/update/",
        views.NotebookUpdateView.as_view(),
        name="notebooks-update"
    ),
    path(
        "notebooks/<int:pk>/detail/",
        views.NotebookDetailView.as_view(),
        name="notebooks-detail"
    ),
    path(
        "notebooks/<int:pk>/delete/",
        views.notebook_delete,
        name="notebooks-delete"
    )
]