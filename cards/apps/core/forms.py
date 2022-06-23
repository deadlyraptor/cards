from django import forms

CATEGORY_CHOICES = [
    ('Dining', 'Dining'),
    ('Entertainment', 'Entertainment'),
    ('Gas', 'Gas'),
    ('Groceries', 'Groceries'),
    ('Online', 'Online'),
    ('Streaming', 'Streaming'),
    ('Travel', 'Travel'),
    ('Transit', 'Transit'),
]


class ExpenseForm(forms.Form):

    amount = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        widget=forms.TextInput(attrs={'class': 'input'}),
    )
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
