from django.urls import path
from .views import Signin, signout, CheckOtp,AddAddress , delete_address , edit_address

app_name = 'account'
urlpatterns = [
    path('signout', signout, name='signout'),
    path('signin', Signin.as_view(), name='signin'),
    path('check', CheckOtp.as_view(), name='check'),
    path('address', AddAddress.as_view(), name='address'),
    path('address/edit/<int:pk>', edit_address, name='edit_address'),
    path('address/delete/<int:pk>', delete_address, name='delete_address'),


]
