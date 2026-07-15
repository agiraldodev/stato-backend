# riamp/tests.py
from django.test import TestCase
from django.db.models import ProtectedError

from shared.models import Paciente, Municipio, Departamento
from riamp.models import Evento


class EventoModelTest(TestCase):
    def setUp(self):
        self.departamento = Departamento.objects.create(
            codigo="19",
            nombre="Cauca",
        )
        self.municipio = Municipio.objects.create(
            codigo="19001",
            nombre="Popayán",
            departamento=self.departamento,
        )
        self.paciente = Paciente.objects.create(
            tipo_documento=Paciente.TipoDocumento.CC,
            numero_documento="123456",
            primer_apellido="Pérez",
            primer_nombre="Juan",
            fecha_nacimiento="1990-05-10",
            sexo=Paciente.Sexo.M,
        )

    def test_crear_evento_correctamente(self):
        evento = Evento.objects.create(
            fecha_evento="2026-07-14T10:00:00Z",
            paciente=self.paciente,
            municipio=self.municipio,
        )
        self.assertEqual(evento.paciente, self.paciente)
        self.assertEqual(evento.municipio, self.municipio)
        self.assertIsNotNone(evento.fecha_registro)

    def test_relacion_related_name_paciente(self):
        Evento.objects.create(
            fecha_evento="2026-07-14T10:00:00Z",
            paciente=self.paciente,
            municipio=self.municipio,
        )
        self.assertEqual(self.paciente.eventos.count(), 1)
        self.assertEqual(self.paciente.eventos.first().municipio, self.municipio)

    def test_paciente_puede_tener_varios_eventos(self):
        otro_municipio = Municipio.objects.create(
            codigo="19100",
            nombre="Puerto Tejada",
            departamento=self.departamento,
        )

        Evento.objects.create(
            fecha_evento="2026-06-14T10:00:00Z",
            paciente=self.paciente,
            municipio=self.municipio,
        )
        Evento.objects.create(
            fecha_evento="2026-07-14T10:00:00Z",
            paciente=self.paciente,
            municipio=otro_municipio,
        )

        self.assertEqual(self.paciente.eventos.count(), 2)
        municipios = list(
            self.paciente.eventos.values_list("municipio__nombre", flat=True)
        )
        self.assertIn("Popayán", municipios)
        self.assertIn("Puerto Tejada", municipios)

    def test_no_permite_borrar_paciente_con_eventos(self):
        Evento.objects.create(
            fecha_evento="2026-07-14T10:00:00Z",
            paciente=self.paciente,
            municipio=self.municipio,
        )
        with self.assertRaises(ProtectedError):
            self.paciente.delete()

    def test_no_permite_borrar_municipio_con_eventos(self):
        Evento.objects.create(
            fecha_evento="2026-07-14T10:00:00Z",
            paciente=self.paciente,
            municipio=self.municipio,
        )
        with self.assertRaises(ProtectedError):
            self.municipio.delete()
