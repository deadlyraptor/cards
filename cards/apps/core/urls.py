from django.urls import path

from cards.apps.core import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cards/', views.CardListView.as_view(), name='card-list'),
    path('cards/<int:pk>', views.CardDetailView.as_view(), name='card-detail'),
    path('expense/', views.ExpenseFormView.as_view(), name='expense-form'),
    path('expense/result', views.ExpenseResultsView.as_view(), name='expense-result'),
]
