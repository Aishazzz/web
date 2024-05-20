from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
   path('about/',views.about,name='about'),
   path('signup/',views.signup,name='signup'),
   path('login/',views.login,name='login'),
   path('edit/<int:book_id>/', views.edit, name='edit'),
   path('homeuser/',views.homeuser,name='homeuser'),
   path('homeadmin/',views.homeadmin,name='homeadmin'),
   path('homeadmin/',views.homeadmin,name='homeadmin'),
   path('bookpg/',views.bookpg,name='bookpg'),
   path('addbook/',views.addbook,name='addbook'),
   path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]
