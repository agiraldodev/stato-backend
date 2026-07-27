# riamp/api.py
from ninja import Router
from django.http import JsonResponse
from .models import Evento

router = Router(tags=["RIAMP"])


@router.get("")
def listar_eventos(request):
    """
    Lista los eventos registrados con todos sus campos, incluyendo la
    información del paciente desagregada. Requiere el permiso
    riamp.view_evento (heredado normalmente desde el grupo RIAMP).
    """
    if not request.user.is_authenticated:
        return JsonResponse({"detail": "No autenticado"}, status=401)

    if not request.user.has_perm("riamp.view_evento"):
        return JsonResponse({"detail": "No tienes permiso para ver eventos"}, status=403)

    eventos = Evento.objects.select_related(
        "paciente",
        "municipio",
        "eapb",
        "cie10",
        "destino_madre",
        "tipo_terminacion_gestacion",
        "metodo_anticonceptivo",
        "observacion_anticoncepcion",
    ).order_by("-fecha_evento")

    data = [
        {
            "id": evento.id,
            "fecha_evento": evento.fecha_evento,
            "hora_evento": evento.hora_evento,
            "fecha_registro": evento.fecha_registro,

            # --- Paciente desagregado ---
            "paciente_tipo_documento": evento.paciente.tipo_documento if evento.paciente_id else None,
            "paciente_numero_documento": evento.paciente.numero_documento if evento.paciente_id else None,
            "paciente_primer_nombre": evento.paciente.primer_nombre if evento.paciente_id else None,
            "paciente_segundo_nombre": evento.paciente.segundo_nombre if evento.paciente_id else None,
            "paciente_primer_apellido": evento.paciente.primer_apellido if evento.paciente_id else None,
            "paciente_segundo_apellido": evento.paciente.segundo_apellido if evento.paciente_id else None,
            "paciente_fecha_nacimiento": evento.paciente.fecha_nacimiento if evento.paciente_id else None,
            "paciente_telefono": evento.paciente.telefono if evento.paciente_id else None,
            "paciente_zona": evento.paciente.get_zona_display() if evento.paciente_id and evento.paciente.zona else None,
            "paciente_sexo": evento.paciente.get_sexo_display() if evento.paciente_id and evento.paciente.sexo else None,

            "municipio": str(evento.municipio) if evento.municipio_id else None,
            "eapb": str(evento.eapb) if evento.eapb_id else None,
            "cie10": str(evento.cie10) if evento.cie10_id else None,
            "estado_conciencia": evento.estado_conciencia,
            "clasificacion_riesgo_gestacional": evento.clasificacion_riesgo_gestacional,
            "clasificacion_riesgo_preeclampsia": evento.clasificacion_riesgo_preeclampsia,
            "diagnostico_ingreso": evento.diagnostico_ingreso,
            "destino_madre": str(evento.destino_madre) if evento.destino_madre_id else None,
            "fecha_terminacion_gestacion": evento.fecha_terminacion_gestacion,
            "tipo_terminacion_gestacion": str(evento.tipo_terminacion_gestacion) if evento.tipo_terminacion_gestacion_id else None,
            "metodo_anticonceptivo": str(evento.metodo_anticonceptivo) if evento.metodo_anticonceptivo_id else None,
            "fecha_suministro_metodo_anticonceptivo": evento.fecha_suministro_metodo_anticonceptivo,
            "observacion_anticoncepcion": str(evento.observacion_anticoncepcion) if evento.observacion_anticoncepcion_id else None,
            "tamizaje_sifilis": evento.tamizaje_sifilis,
            "fecha_resultado_pr_sifilis": evento.fecha_resultado_pr_sifilis,
            "tamizaje_vih": evento.tamizaje_vih,
            "fecha_resultado_vih": evento.fecha_resultado_vih,
            "fecha_lactancia_materna": evento.fecha_lactancia_materna,
            "numero_nacidos_vivos": evento.numero_nacidos_vivos,
        }
        for evento in eventos
    ]

    return {"status": "success", "eventos": data}