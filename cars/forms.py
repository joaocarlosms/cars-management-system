from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')

        if value < 18000:
            self.add_error('value', 'Só é possível cadastrar carros com valor acima de R$-18.000')
        else:
            return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')

        if factory_year < 1980:
            self.add_error('factory_year', 'Só é possivel cadastrar carros com ano de fabricação acima de 1980')
        else:
            return factory_year