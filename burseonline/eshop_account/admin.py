from django.contrib import admin

from .models import Profile, Ticket, Answer, Wallet, Factor, Question, ContactUs

admin.site.register(Profile)
admin.site.register(Ticket)
admin.site.register(Answer)
admin.site.register(Wallet)
admin.site.register(Factor)
admin.site.register(Question)
admin.site.register(ContactUs)


# Register your models here.
