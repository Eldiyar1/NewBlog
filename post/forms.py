from django import forms

from .models import Product, Comment, Category


class ProductCreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)
    rate = forms.IntegerField(min_value=1, max_value=5)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if len(title) < 10:
            raise forms.ValidationError("Title to short!")
        return cleaned_data

    def clean_content(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        if len(content) < 40:
            raise forms.ValidationError("content to short!")
        if not content:
            raise forms.ValidationError("content is required!")
        return cleaned_data

class ProductCreateForm2(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'content', 'image', 'rate')


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)
