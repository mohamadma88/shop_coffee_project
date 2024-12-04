from django.urls import path
from .views import contactview ,aboutus,question

app_name = 'contact'
urlpatterns = [
    path('contact', contactview, name='contact'),
    path('aboutus', aboutus, name='aboutus'),
    path('question', question, name='question'),
]
