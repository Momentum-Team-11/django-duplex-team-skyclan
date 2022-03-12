from django import forms
from .models import Deck, Card


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = [
            'title',
            'description',
        ]


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = [
            'word',
            'definition',
            'deck',
        ]