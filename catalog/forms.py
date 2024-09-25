from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField
from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ("views_counter", "created_at", "updated_at",)

    def clean_product_name(self):
        product_name = self.cleaned_data["product_name"]

        banned_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

        for word in product_name.split():
            if word in banned_words:
                raise ValidationError("Название продукта содержит запрещенные слова.")
        return product_name

    def clean_product_description(self):
        product_description = self.cleaned_data["product_description"]

        banned_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]

        for word in product_description.split():
            if word in banned_words:
                raise ValidationError("Описание продукта содержит запрещенные слова.")
        return product_description


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
