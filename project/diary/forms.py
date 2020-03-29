from django import forms
from .models import Day

class DayCreateForm(forms.ModelForm):
    """docstring forDayCreateForm."""

    class Meta:
        model = Day
        fields = '__all__'   #('text', 'title', 'date')　特定のフィードだけ指定したい場合はタプルで記述
