from django import forms
from ejemplo.models import Familiar, Persona, Vuelo

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']

class PersonaForm(forms.ModelForm):
  class Meta:
    model = Persona
    fields = ['nombre', 'apellido', 'numero_documento']

class VueloForm(forms.ModelForm):
  class Meta:
    model = Vuelo
    fields = ['aeropuerto_salida', 'aeropuerto_destino', 'numero_vuelo']