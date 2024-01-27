from django.urls import path
from. import views
app_name='auth'
urlpatterns = [
   
    path('userregister/',views.userregister ,name='userregister'),
    path('login/',views.login ,name='login'),
    path('logout/',views.logout ,name='logout')

]
