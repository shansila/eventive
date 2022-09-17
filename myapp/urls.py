from django.urls import path
from . import views
app_name = 'user'
urlpatterns =[
  path('home/', views.home, name='user_home'),
  path('signup/',views.signup, name='user_signup'),
  path('display/',views.getusers,name='user_display'),
  path('update/<int:userid>',views.update,name='user_update'),
  path('delete/<int:userid>',views.delete,name='user_delete'),
  path('about/',views.about,name='user_about'),
  path('contact/',views.contact,name='user_contact'),
  path('login/',views.login,name='user_login'),
  path('userhome/',views.userhome,name='user_userhome'),
  path('user/',views.user,name='user_user'),
  path('simplebday/',views.birthday1,name='user_simplebday'),
  path('wedding/',views.wedding,name='user_wedding'),
  path('cart',views.cart,name='user_cart'),
  path('checkout',views.checkout,name='user_checkout'),
  path('logout/',views.logout,name='logout')
]
