from django import forms
from .models import Task
from django.db.models import Q
from accounts.models import User, Role

class TaskCreationForm(forms.ModelForm):
    COMPLETION_CHOICES = [
        (True, 'Completed'),
        (False, 'Not Completed'),
    ]

    class Meta:
        model = Task
        fields = ['name','description','assigned_to', 'completed']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Task Name','required':'required'}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter Description','required':'required','rows':'2'}),
            'assigned_to': forms.Select(attrs={'class': 'form-control','placeholder':'Assign a User','required':'required'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Assign the label here instead of in the widget
        self.fields['assigned_to'].label = "Assign To"

        te_role = Role.objects.filter(name = 'Task Executor')
        queryset = User.objects.filter(role__in=te_role)
        
        self.fields['assigned_to'].queryset = queryset