from django.shortcuts import render, HttpResponse
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def home(request):
    ingredients = Ingredient.objects.all()
    menu_items = MenuItem.objects.all()
    recipe_requirements = Ingredient.objects.all()
    purchases = Purchase.objects.all()
    
    context = {
        "ingredients" : ingredients,
        "menu_items" : menu_items,
        "recipe_requirements" :recipe_requirements,
        "purchases" : purchases
    }
    return render(request, 'inventory/home.html', context)

def login_view(request):
    context = {
        "login_view" : "active"
    }
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("home"))
        else:
            HttpResponse("Invalid login and password")        
    return render(request, "registration/login.html", context)
    
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

class IngredientListView(ListView, LoginRequiredMixin):
    model = Ingredient
    template_name = "inventory/ingredients_list.html"
    
    
class IngredientCreateView(CreateView, LoginRequiredMixin):
    model = Ingredient
    template_name = "inventory/add_ingredient.html"
    form_class = IngredientForm

class IngredientUpdateView(UpdateView, LoginRequiredMixin):
    model = Ingredient
    template_name = "inventory/update_ingredient.html"
    form_class = IngredientForm

class IngredientDeleteView(DeleteView, LoginRequiredMixin):
    model = Ingredient
    template_name = "inventory/delete_ingredient.html"
    form_class = IngredientForm
    
class MenuItemListView(ListView):
    model = MenuItem
    template_name = "inventory/menu_list.html"
    
class MenuItemCreateView(CreateView, LoginRequiredMixin):
    model = MenuItem
    template_name = "inventory/add_menu_item.html"
    form_class = MenuItemForm
    
class MenuItemUpdateView(UpdateView, LoginRequiredMixin):
    model = MenuItem
    template_name = "inventory/update_menu_item.html"
    form_class = MenuItem
    
class MenuItemDeleteView(DeleteView, LoginRequiredMixin):
    model = MenuItem
    template_name = "inventory/delete_menu_item.html"
    form_class = MenuItem
    
class RecipeRequirementListView(ListView, LoginRequiredMixin):
    model = RecipeRequirementForm
    
    
class RecipeRequirementCreateView(CreateView, LoginRequiredMixin):
    model = RecipeRequirement
    template_name = "inventory/add_recipe_requirement.html"
    form_class = RecipeRequirementForm
    
class RecipeRequirementUpdateView(UpdateView, LoginRequiredMixin):
    model = RecipeRequirement
    template_name = "inventory/update_reciperequirement.html"
    form_class = RecipeRequirementForm
    
class RecipeRequirementDeleteView(DeleteView, LoginRequiredMixin):
    model = RecipeRequirement
    template_name = "inventory/delete_reciperequirement.html"
    form_class = RecipeRequirementForm
    
class PurchaseListView(ListView):
    model = Purchase
    
class PurchaseCreateView(CreateView, LoginRequiredMixin):
    model = Purchase
    template_name = "inventory/add_purchase.html"
    form_class = PurchaseForm
    
class PurchaseUpdateView(UpdateView, LoginRequiredMixin):
    model = Purchase
    template_name = "inventory/update_purchase.html"
    form_class = PurchaseForm
    
class PurchaseDeleteView(DeleteView, LoginRequiredMixin):
    model = Purchase
    template_name = "inventory/delete_purchase.html"
    form_class = PurchaseForm
    
class ReportsView(TemplateView):
    template_name = "inventory/reports.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        total_revenue = Purchase.objects.aggregate(total_revenue=Sum('menu_item__price'))
        context['revenue'] = total_revenue['total_revenue'] or 0
        
        total_cost = RecipeRequirement.objects.aggregate(total_cost=Sum('ingredient__unit_price'))
        context['total_cost'] = total_cost['total_cost'] or 0
        
        context['profit'] = context['revenue'] - context ['total_cost']
        
        return context
