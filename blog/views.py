from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Recipe
from .forms import CommentForm, RecipeForm


# class PostList(generic.ListView):
#     model = Post
#     queryset = Post.objects.filter(status=1).order_by("-created_on")
#     template_name = "index.html"
#     paginate_by = 6


class RecipeList(generic.ListView):
    model = Recipe()
    queryset = Recipe.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


def create_recipe(request):
    """
    renders a recipe page
    """
    recipe_form = RecipeForm(request.POST or None, request.FILES or None)
    context = {
        'recipe_form': recipe_form,
    }

    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe_form = recipe_form.save(commit=False)
            recipe_form.author = request.user
            recipe_form.status = 1
            recipe_form.save()
            return redirect('home')
    else:
        recipe_form = RecipeForm()
    return render(request, "create_recipe.html", context)


def delete_recipe(request, slug):
    """
    Recipe delete view
    """
    recipe = Recipe.objects.get(slug=slug)
    recipe.delete()
    return redirect('home')   


def edit_recipe(request, slug):
    """
    Recipe update view
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    recipe_form = RecipeForm(request.POST or None, instance=recipe)
    context = {
        "recipe_form": recipe_form,
        "recipe": recipe
    }
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('home')
    else:
        recipe_form = RecipeForm(instance=recipe)
    return render(request, "edit_recipe.html", context)

class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        recipe = get_object_or_404(Recipe, slug=slug)
        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
