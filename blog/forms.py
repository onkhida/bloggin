from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','thumbnail','content')

    def __init__(self, *args, **kwargs):
        super(PostCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'uk-input','type':'text','placeholder':'Title'})
        self.fields['content'].widget.attrs.update({'class':'uk-textarea','rows':'20','placeholder':'Content','cols':'160'})
            # <textarea class="uk-textarea" rows="5" placeholder="Textarea"></textarea>
