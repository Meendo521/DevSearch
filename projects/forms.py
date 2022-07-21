from django.forms import ModelForm
from django import forms
from .models import Project, Review


# Project Form
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ["vote_ratio", "vote_total", "owner"]
        widgets = {"tags": forms.CheckboxSelectMultiple}

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "input",
                }
            )

        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add title'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["value", "body"]

        labels = {"value": "Place your vote", "body": "Add a comment with your vote"}

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
