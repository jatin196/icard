from django.urls import path
from .views import home, thankyou, ClientList

app_name = 'icard'
urlpatterns = [
    path('', home, name='home'),
    path('list/', ClientList.as_view(), name='list'),

    path('Info-saved/', thankyou, name='thanks'),


]