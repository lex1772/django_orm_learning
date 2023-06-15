from django import forms

from main.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "is_active":
                pass
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ("product_name", "description", "category", "price",)

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']

        words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

        if cleaned_data.lower() in words:
            raise forms.ValidationError('Запрещенный продукт')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

        if cleaned_data.lower() in words:
            raise forms.ValidationError('Запрещенный продукт')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = ("number", "title", "is_active")

