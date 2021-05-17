from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scope, ArticleScope


class ArticleScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            if main_count > 1:
                raise ValidationError('Можно указать только один основной раздел')
            if form.cleaned_data and form.cleaned_data['is_main']:
                main_count += 1
        if main_count == 0:
            raise ValidationError('Добавьте основной раздел')
        return super().clean()

class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    extra = 3
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
