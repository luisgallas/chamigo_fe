import requests
import frappe


MOCK_API_URL = "http://host.docker.internal:5001/factura-electronica"


def obtener_facturas_pendientes():
    return frappe.get_all(
        "Factura Electronica",
        filters={"estado": "Pendiente"},
        fields=[
            "name",
            "factura_erp",
            "cliente",
            "fecha_factura",
            "total",
            "moneda",
            "estado"
        ]
    )


def enviar_a_mock_api(factura):
    payload = {
        "id_fe": factura.name,
        "factura_erp": factura.factura_erp,
        "cliente": factura.cliente,
        "fecha_factura": str(factura.fecha_factura),
        "total": float(factura.total),
        "moneda": factura.moneda
    }

    response = requests.post(MOCK_API_URL, json=payload, timeout=10)
    response.raise_for_status()
    return response.json()


def actualizar_estado_factura(nombre_fe, respuesta):
    estado_api = respuesta.get("estado", "").lower()

    if estado_api == "aceptado":
        estado = "Aceptado"
    elif estado_api == "rechazado":
        estado = "Rechazado"
    else:
        estado = "Enviado"

    doc = frappe.get_doc("Factura Electronica", nombre_fe)
    doc.estado = estado
    doc.respuesta_api = frappe.as_json(respuesta)
    doc.fecha_envio = frappe.utils.now_datetime()
    doc.save(ignore_permissions=True)


def marcar_error(nombre_fe, error):
    doc = frappe.get_doc("Factura Electronica", nombre_fe)
    doc.estado = "Error"
    doc.error = str(error)
    doc.fecha_envio = frappe.utils.now_datetime()
    doc.save(ignore_permissions=True)


def sincronizar_facturas():
    facturas = obtener_facturas_pendientes()

    for factura in facturas:
        try:
            respuesta = enviar_a_mock_api(factura)
            actualizar_estado_factura(factura.name, respuesta)
            frappe.db.commit()
            print(f"Factura Electronica {factura.name} sincronizada correctamente.")
        except Exception as e:
            marcar_error(factura.name, e)
            frappe.db.commit()
            print(f"Error al sincronizar {factura.name}: {e}")


if __name__ == "__main__":
    sincronizar_facturas()
