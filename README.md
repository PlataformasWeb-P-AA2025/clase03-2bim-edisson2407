# clase03-2bim

## Explicacion
- **_set** permite acceder desde un objeto padre a todos los objetos hijos relacionados.
![image](https://github.com/user-attachments/assets/73bb13d0-92ea-4261-86ee-fd1ead288669)


### 25 Jun 2025 
```python
def __init__(self, estudiante, *args, **kwargs):
    super(NumeroTelefonicoEstudianteForm, self).__init__(*args, **kwargs)
    self.initial['estudiante'] = estudiante
    self.fields["estudiante"].widget = forms.widgets.HiddenInput()
    print(estudiante)

class Meta:
    model = NumeroTelefonico
    fields = ['telefono', 'tipo', 'estudiante']

```
- El formulario sirve para registrar y editar un numero y asociarlo a un estudiante ya creado. cuando se crea el formulario recibe el estudiante y lo guarda de manera oculta, asi no se necesita seleccionarlo de forma manual