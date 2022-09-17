from django.urls import path
from . import views
app_name = 'event'
urlpatterns =[
      path('home/', views.home, name='event_homead'),
      path('about/',views.about,name='event_aboutad'),
      path('profile/',views.profile,name='event_profilead'),
      path('birthday/',views.birthday,name='event_birthday'),
      path('wedding/',views.wedding,name='event_wedding')

]