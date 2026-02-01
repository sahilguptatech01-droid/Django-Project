from django.urls import path ,include
from  .import views



app_name="coursera"

urlpatterns=[
    path('',views.home_page,name="home"),
    path('detail/<int:id>',views.detail ,name="detail"),
    path('add/',views.add_course,name="add"),
    path('buy/',views.buy,name='buy'),
    path('delete/<int:id>',views.delete_course,name='delete'),
   
   

]