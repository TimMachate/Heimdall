#--------------------------------------------------------------------------------
# Import necessary Moduls
#--------------------------------------------------------------------------------
from django.contrib import admin
from django.utils import timezone
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Models
#--------------------------------------------------------------------------------
from documentationmanagement.document.models import Document
from documentationmanagement.file.models import File, DocumentProxy
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Import necessary Admins
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# Admin
#--------------------------------------------------------------------------------
class DocumentInlineAdmin(admin.StackedInline):
    model = Document
    max_num = 1
    fieldsets = (
        (None,{"fields":(
            "content",
        )}),
    )

@admin.register(DocumentProxy)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['reference_number','name','version_prefix','version_suffix']
    search_fields = ['name']
    list_filter = []
    list_editable = []
    ordering = ['name',]
    fieldsets = (
        (None, {'fields':(
            'name',
            'version_prefix',
            )}),
        (None, {'fields':(
            'file',
            )}),
        ('Beschreibung', {'fields':(
            'keywords',
        )}),
    )

    inlines = [DocumentInlineAdmin]
    filter_horizontal = []
    radio_fields = {}
    def save_model(self, request, instance, form, change):
        user = request.user
        instance.type=instance.Types.DOCUMENT
        instance = form.save(commit=False)
        if not change or not instance.create_user_id:
            instance.create_user_id = user
        instance.update_user_id = user
        instance.update_datetime = timezone.now()
        instance.save()
        form.save_m2m()
        return instance
#--------------------------------------------------------------------------------