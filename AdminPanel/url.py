
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="Home"),
    path('Login/', views.login,name="Login"),
    path('AdminHome/', views.adminhome,name="AdminHome"),
    path('STS_Placement/', views.placementDetails,name="PlacementDetails"),
    path('Login/login', views.login),
    
    path('AddPlacement/',views.addPlacement,name='AddPlacement'),
    path('AddPlacement/addPlacement',views.addPlacement,name='addPlacement'),
]
