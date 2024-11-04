from django.urls import path

from .views import UserListView, UserDetailView

app_name = "accouns"
urlpatterns = [
    path("users", UserListView.as_view(), name="user_list"),
    path("user/<str:username>", UserDetailView.as_view(), name="user_detail")
]
