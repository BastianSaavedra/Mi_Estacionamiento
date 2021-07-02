from django.urls import path
from . import views

urlpatterns = [
    path('owner-register/', views.owner_register, name="owner-register"),
    path('user-profile/', views.sidebar, name="user-profile"),

    # CARDS URLS
    path('cards-list/', views.CardInformationListView.as_view(), name="cards-list"),
    path('add-card/', views.add_card, name="add-card"),
    path('update-card/<id>/', views.update_card, name="update-card"),
    path('delete-card/<id>/', views.delete_card, name="delete-card"),

    # CARS URLS
    path('cars-list/', views.CarsInformationListView.as_view(), name="cars-list"),
    path('add-car/', views.add_card, name="add-car"),
    path('update-car/<id>/', views.update_car, name="update-car"),
    path('delete-car/<id>/', views.delete_car, name="delete-car")
] 
