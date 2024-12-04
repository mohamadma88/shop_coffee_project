from django.urls import path
from .views import Signin, signout, CheckOtp,AddAddress

app_name = 'account'
urlpatterns = [
    path('signout', signout, name='signout'),
    path('signin', Signin.as_view(), name='signin'),
    path('check', CheckOtp.as_view(), name='check'),
    path('address', AddAddress.as_view(), name='address'),

]
