from django.contrib import admin
from noteblog.models import *

admin.site.register(Noteblog,NoteblogAdmin)
admin.site.register(Replay)
admin.site.register(Category)
admin.site.register(Registration,RegistrationAdmin)
