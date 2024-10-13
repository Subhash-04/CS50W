from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
import re
from .models import Recipe, Profile
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseForbidden

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        help_text='Required. 8-30 characters. Letters, digits and @/./+/-/_ only.'
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 8:
            raise forms.ValidationError('Username must be at least 8 characters long.')
        if not re.match(r'^[a-zA-Z0-9@./+/-/_]+$', username):
            raise forms.ValidationError('Username can only contain letters, digits and @/./+/-/_ characters.')
        return username

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user)  # Ensure profile is created
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        # Ensure profile is created if it doesn't exist
        user = form.get_user()
        Profile.objects.get_or_create(user=user)
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'app/index.html', {'recipes': recipes})

@login_required
def submit_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('index')
    else:
        form = RecipeForm()
    return render(request, 'app/submit_recipe.html', {'form': form})

def view_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'app/view_recipe.html', {'recipe': recipe})

@login_required
def like_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.likes.filter(id=request.user.id).exists():
        recipe.likes.remove(request.user)
    else:
        recipe.likes.add(request.user)
    return HttpResponseRedirect(reverse('view_recipe', args=[recipe.id]))

@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    Profile.objects.get_or_create(user=user_to_follow)  # Ensure profile exists
    if request.user.profile.follows.filter(id=user_to_follow.profile.id).exists():
        request.user.profile.follows.remove(user_to_follow.profile)
    else:
        request.user.profile.follows.add(user_to_follow.profile)
    return HttpResponseRedirect(reverse('view_user', args=[user_to_follow.id]))

def view_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    recipes = Recipe.objects.filter(author=user)
    Profile.objects.get_or_create(user=user)  # Ensure profile exists
    return render(request, 'app/view_user.html', {'user': user, 'recipes': recipes})

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this recipe.")
    recipe.delete()
    return redirect('index')
