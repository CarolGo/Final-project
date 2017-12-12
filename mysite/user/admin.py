from django.contrib import admin
from .models import user, invest, user_invest, question, myindex
admin.site.register(user)
admin.site.register(invest)
admin.site.register(user_invest)
admin.site.register(question)
