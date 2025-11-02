# blog/forms.py
from django import forms
from .models import Post

BANNED_WORDS = {"spam", "clickbait", "scam", "test123"}  # example list

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter a clear, descriptive title",
                "aria-describedby": "titleHelp",
            }),
            "body": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 8,
                "placeholder": "Write your post here…",
                "aria-describedby": "bodyHelp",
            }),
        }

    def clean_title(self):
        title = (self.cleaned_data.get("title") or "").strip()
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters.")
        lowered = title.lower()
        if any(bad in lowered for bad in BANNED_WORDS):
            raise forms.ValidationError("Please use a professional, non-spammy title.")
        return title

    def clean_body(self):
        body = (self.cleaned_data.get("body") or "").strip()
        if len(body) < 20:
            raise forms.ValidationError("Body must be at least 20 characters.")
        return body


class CommentForm(forms.Form):
    text = forms.CharField(
        label="Your comment",
        max_length=2000,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 3,
            "placeholder": "Write your comment…",
            "aria-describedby": "commentHelp",
        })
    )

    def clean_text(self):
        txt = (self.cleaned_data.get("text") or "").strip()
        if len(txt) < 2:
            raise forms.ValidationError("Comment is too short.")
        lowered = txt.lower()
        if any(bad in lowered for bad in BANNED_WORDS):
            raise forms.ValidationError("Please avoid spammy language.")
        return txt

