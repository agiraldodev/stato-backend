# backend/shared/resources.py
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Departamento, Municipio, Eapb, CIE10

class DepartamentoResource(resources.ModelResource):
    class Meta:
        model = Departamento
        import_id_fields = ('codigo',)
        fields = ('codigo', 'nombre')


class MunicipioResource(resources.ModelResource):
    departamento = fields.Field(
        column_name='departamento',
        attribute='departamento',
        widget=ForeignKeyWidget(Departamento, field='codigo')
    )

    class Meta:
        model = Municipio
        import_id_fields = ('codigo',)
        fields = ('codigo', 'nombre', 'departamento')

class EapbResource(resources.ModelResource):
    class Meta:
        model = Eapb
        import_id_fields = ('codigo',)
        fields = ('codigo', 'nombre')

class CIE10Resource(resources.ModelResource):
    class Meta:
        model = CIE10
        import_id_fields = ('codigo',)
        fields = ('codigo', 'nombre')

        widgets = {
            'import_format': {'delimiter': ';'}
        }