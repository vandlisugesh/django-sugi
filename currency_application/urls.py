from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.welcome, name="welcome"),
    url(r'^', views.form_data, name="form_data"),
]