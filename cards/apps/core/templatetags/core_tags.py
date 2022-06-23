from django import template

register = template.Library()


@register.simple_tag
def base_cashback(card, amount):
    return card.base_cashback(amount)


@register.simple_tag
def category_cashback(card, category, amount):
    return card.category_cashback(category, amount)
