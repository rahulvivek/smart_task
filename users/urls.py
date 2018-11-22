from django.conf.urls import include, url

from .views import CustomLoginView

urlpatterns = [
    url(r'^login/$', CustomLoginView.as_view(), name="login_view"),
]