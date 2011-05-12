from django.db import models
import tinymce.models
import tinymce.widgets

# Create your models here.
class Decision(models.Model):
    short_name = models.CharField(max_length=255, verbose_name='Decision')
    decided_date = models.DateField(null=True, blank=True,
        verbose_name='Decided date')
    effective_date = models.DateField(null=True, blank=True,
        verbose_name='Effective date')
    review_date = models.DateField(null=True, blank=True,
        verbose_name='Review date')
    expiry_date = models.DateField(null=True, blank=True,
        verbose_name='Expiry date')
    budget = models.TextField(blank=True,
        verbose_name='Budget')
    people = models.TextField(blank=True,
        verbose_name='People')
    description = tinymce.models.HTMLField(blank=True,
        verbose_name='Description')
    concerns = models.TextField(blank=True,
        verbose_name='Concerns')
    
    def concerns_yesno(self):
        if self.concerns:
            return "Yes"
        else:
            return "No"