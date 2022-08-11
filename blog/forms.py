from .models import Comment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form to add comment
    """
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """
    Form to add a recipe
    """
    class Meta:
        model = Recipe
        fields = [
            'title',
            'excerpt',
            'time_to_prepare',
            'difficulty',
            'serves',
            'time_to_cook',
            'ingredients',
            'method',
            'featured_image',
        ]

        prepopulated_fields = {'slug': ('title',)}

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
