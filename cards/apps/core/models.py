from decimal import Decimal
import math

from django.db import models


class Card(models.Model):
    """A model for Cards.

    Savor One
    Netflix
    16.42
    3%
    0.49

    Hulu
    1.05
    3%
    0.03

    """

    issuer = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    base_rate = models.DecimalField(
        max_digits=3,
        decimal_places=2,
    )

    class Meta:
        ordering = ['issuer', 'name']

    def __str__(self):
        return f'{self.issuer} {self.name}'

    def base_cashback(self, amount):
        if self.name == 'Rewards+':
            return (int(math.ceil((self.base_rate * Decimal(amount)) / 10)) * 10) / 100
        else:
            return (self.base_rate * Decimal(amount) / 100)

    def category_cashback(self, category, amount):
        if self.name == 'Rewards+':
            return (int(math.ceil((category.rate * Decimal(amount)) / 10)) * 10) / 100
        else:
            return round((category.rate * Decimal(amount) / 100), 2)


class Category(models.Model):
    """A model card categories and their cashback rate, by card."""

    CATEGORY_CHOICES = [
        ('DIN', 'Dining'),
        ('ENT', 'Entertainment'),
        ('GAS', 'Gas'),
        ('GRO', 'Groceries'),
        ('ONL', 'Online'),
        ('STR', 'Streaming'),
        ('TRA', 'Travel'),
        ('TST', 'Transit'),
    ]

    card = models.ForeignKey(Card,
                             on_delete=models.CASCADE,
                             related_name='category')
    category = models.CharField(
        max_length=3,
        choices=CATEGORY_CHOICES,
    )
    rate = models.DecimalField(
        max_digits=3,
        decimal_places=2,
    )

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['category', 'card']

    def __str__(self):
        return f'{self.rate} {self.category} ({self.card})'
