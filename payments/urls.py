from django.urls import path

from . import views

app_name = 'payments'

urlpatterns = [

	path('', views.PaymentHistory.as_view(), name='my_payments'),

	path('pay/', views.InitiatePayment.as_view(), name='initiate_payment'),

	path('payment-sent/', views.PaymentSent.as_view(), name='payment_sent'),

	path('payment-successful/', views.PaymentSuccess.as_view(), name='payment_success'),

]
