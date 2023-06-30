from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("index/",views.index,name='index'),
    path("base",views.base,name='base'),
    path("services/",views.services,name='services'),
    path("login/",views.login,name='login'),
    path("signup/",views.signup,name='signup'),
    path("about/",views.about,name='about'),
    path("transaction/",views.transaction,name='transaction'),
    path("contact/",views.contact,name='contact'),
    path("accounts/",views.accounts,name='accounts')
    
]

# from django.contrib import admin
# from django.urls import path
# from home import views
# urlpatterns = [
#     path("", views.index, name='home'),
#     path("index/", views.index, name='index'),
#     path("services/", views.services, name='services'),
#     path("login/", views.login, name='login'),
#     path("signup/", views.signup, name='signup'),
#     path("about/", views.about, name='about'),
#     path("transaction/", views.transaction, name='transaction'),
#     path("contact/", views.Contact, name='contact'),
#     # path('contact/', contact_view, name='contact'),
#     path("accounts/", views.accounts, name='accounts')
# ]
