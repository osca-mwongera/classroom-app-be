from django.contrib import admin

from payments.models import LNMOnline, PaymentType, Payment


class LNMOnlineAdmin(admin.ModelAdmin):
    list_display = [
    	'mpesa_receipt_number',
    	'phone_number',
    	'amount',
    	'timestamp',
    	'result_desc'
    ]


class PaymentTypeAdmin(admin.ModelAdmin):
	list_display = ['pk', 'name', 'amount', 'created', 'updated']


class PaymentAdmin(admin.ModelAdmin):
	list_display = [
		'pk',
		'payment_type',
		'property_item',
		'client',
		'status',
		'valid_until'
	]


admin.site.register(LNMOnline, LNMOnlineAdmin)
admin.site.register(PaymentType, PaymentTypeAdmin)
admin.site.register(Payment, PaymentAdmin)
