from django.urls import path

from .models import *
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    
    path("home/", views.home, name="home"),
    
    path("ingredient/list", views.IngredientListView.as_view(), name='ingredients'),
    path("ingredient/create/", views.IngredientCreateView.as_view(), name='add_ingredient'),
    path("ingredient/update/<int:pk>", views.IngredientUpdateView.as_view(), name="update_ingredient"),
    
    path('recipe/', views.RecipeRequirementListView.as_view(), name="recipe"),
    path('recipe/create/', views.RecipeRequirementCreateView.as_view(), name='add_recipe_requirement'),
    
    path("menu/list", views.MenuItemListView.as_view(), name='menu'),
    path("menu/create/", views.MenuItemCreateView.as_view(), name="add_menu_item"),
    
    path("purchases/list", views.PurchaseListView.as_view(), name='purchases'),
    path("purchase/create/", views.PurchaseCreateView.as_view(), name='add_purchase'),
    path("reports/", views.ReportsView.as_view(), name='reports'),
]
