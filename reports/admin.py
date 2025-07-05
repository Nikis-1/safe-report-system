from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'user',
        'get_decrypted_description',
        'location',
        'sentiment_score',
        'created_at',
        'status',
    )
    list_filter = ('status', 'created_at',)
    search_fields = ('title', 'user__username', 'location')

    readonly_fields = ('get_decrypted_description',)

    def get_decrypted_description(self, obj):
        return obj.get_description()
    get_decrypted_description.short_description = 'Decrypted Description'

    # Allow editing status directly in the list view
    list_editable = ('status',)
