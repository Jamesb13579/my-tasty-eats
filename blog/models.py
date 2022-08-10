from django.db import models

from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

STATUS = (
    (0, "Draft"),
    (1, "Published")
    )
DIFFICULTY = (
    (0, "Beginner"),
    (1, "Regular"),
    (2, "Hard")
    )
TIME = (
    (1, "5 Minutes"),
    (2, "10 Minutes"),
    (3, "15 Minutes"),
    (4, "20 Minutes"),
    (5, "25 Minutes"),
    (6, "30 Minutes"),
    (7, "40 Minutes"),
    (8, "50 Minutes"),
    (9, "60 Minutes"),
    )
SERVES = (
    (1, "1 Person"),
    (2, "2 People"),
    (3, "3 People"),
    (4, "4 People"),
    (5, "5 People"),
    (6, "6 People"),
    (7, "7 People"),
    (8, "8 People"),
    )

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Recipe(models.Model):
    """
    Model for the Recipe
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes")
    excerpt = models.TextField(blank=True,
                               help_text="Write a short summary of the recipe")
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=1)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    time_to_prepare = models.IntegerField(choices=TIME, default=1)
    difficulty = models.IntegerField(choices=DIFFICULTY, default=1)
    serves = models.IntegerField(choices=SERVES, default=1)
    time_to_cook = models.IntegerField(choices=TIME, default=1)
    ingredients = models.TextField()
    method = models.TextField()
    likes = models.ManyToManyField(
        User, related_name='user_recipe_likes', blank=True
    )

    class Meta:
        """
        Order the recipes in descending order.
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string showing the title.
        """
        return str(self.title)

    def amount_of_likes(self):
        """
        See number of likes on a recipe.
        """
        return self.likes.count()

    def can_edit(self, request, slug):
        """
        Allows author to edit recipe.
        """
        if self.author:
            return True
        else:
            return False

    def can_delete(self, request, slug):
        """
        Allows author to delete recipe.
        """
        if self.author:
            return True
        else:
            return False

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments", null=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
