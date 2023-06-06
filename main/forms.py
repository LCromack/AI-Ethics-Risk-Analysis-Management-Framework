from django import forms


class CreateNewFramework(forms.Form):
    name = forms.CharField(label="Name: ", max_length=200)
    check = forms.BooleanField(required=False)


class SearchChatGPT(forms.Form):
    searchPrompt = forms.CharField(label="Search ", max_length=300)
