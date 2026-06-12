import re
import frappe

from chamigo_fe.integrations.factura_segura_client import (
    calcular_de,
    generar_de,
    consultar_estado,
)


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
            "estado",
        ],
    )


def extraer_numero_documento(nombre_fe):
    numeros = re.findall(r"\d+", nombre_fe or "")
    if not numeros:
        return "1000000"

    numero = int(numeros[-1])
    numero_documento = 1000000 + numero

    return str(numero_documento).zfill(7)


def construir_de_resumido(factura):
    total = int(float(factura.total or 0))
    if total <= 0:
        total = 10000

    numero_documento = extraer_numero_documento(factura.name)

    return {
        "iTipEmi": "1",
        "iTiDE": "1",
        "dNumTim": "00964343",
        "dFeIniT": "2024-04-02",
        "dEst": "001",
        "dPunExp": "001",
        "dNumDoc": numero_documento,
        "dFeEmiDE": frappe.utils.now_datetime().strftime("%Y-%m-%dT%H:%M:%S"),
        "iTipTra": "1",
        "iTImp": "1",
        "cMoneOpe": "PYG",
        "dCondTiCam": "1",
        "dTiCam": "1",

        "dRucEm": "964343",
        "dDVEmi": "5",
        "iTipCont": "1",
        "dNomEmi": "ALE WILFRIDO FELTES QUENHAN",
        "dDirEmi": "Direccion de prueba",
        "dNumCas": "0",
        "cDepEmi": "1",
        "dDesDepEmi": "CAPITAL",
        "cCiuEmi": "1",
        "dDesCiuEmi": "ASUNCION (DISTRITO)",
        "dTelEmi": "000000",
        "dEmailE": "alefeltes@gmail.com",

        "gActEco": [
            {
                "cActEco": "62010",
                "dDesActEco": "Actividades de programación informática",
            },
            {
                "cActEco": "62020",
                "dDesActEco": "Actividades de consultoría y gestión de servicios informáticos",
            },
            {
                "cActEco": "74909",
                "dDesActEco": "Otras actividades profesionales, científicas y técnicas n.c.p.",
            },
            {
                "cActEco": "99999",
                "dDesActEco": "Sin código equivalente",
            },
        ],

        "iNatRec": "1",
        "iTiOpe": "1",
        "cPaisRec": "PRY",
        "iTiContRec": "1",
        "dRucRec": "2595733",
        "dDVRec": "3",
        "iTipIDRec": "0",
        "dNumIDRec": "0",
        "dNomRec": factura.cliente or "CLIENTE DE PRUEBA",
        "dEmailRec": "receptor@test.com",

        "iIndPres": "1",
        "iCondOpe": "1",

        "gPaConEIni": [
            {
                "iTiPago": "1",
                "dMonTiPag": str(total),
                "cMoneTiPag": "PYG",
                "dTiCamTiPag": "1",
            }
        ],

        "iCondCred": "1",
        "dPlazoCre": "0",

        "gCamItem": [
            {
                "dCodInt": "SERV001",
                "dDesProSer": f"Factura ERPNext {factura.factura_erp}",
                "cUniMed": "77",
                "dCantProSer": "1",
                "dPUniProSer": str(total),
                "dDescItem": "0",
                "dDescGloItem": "0",
                "dAntPreUniIt": "0",
                "dAntGloPreUniIt": "0",
                "iAfecIVA": "1",
                "dPropIVA": "100",
                "dTasaIVA": "10",
            }
        ],

        "CDC": "0",
        "dCodSeg": "0",
        "dDVId": "0",
        "dSisFact": "1",
        "dInfAdic": "Integracion ERPNext Chamigo - Factura Segura",
    }


def enviar_a_factura_segura(factura):
    de_resumido = construir_de_resumido(factura)

    respuesta_calculo = calcular_de(de_resumido)
    if respuesta_calculo.get("code") != 0:
        return {
            "estado": "Error",
            "etapa": "calcular_de",
            "respuesta": respuesta_calculo,
        }

    de_calculado = respuesta_calculo["results"][0]["DE"]

    respuesta_generacion = generar_de(de_calculado)
    if respuesta_generacion.get("code") != 0:
        return {
            "estado": "Error",
            "etapa": "generar_de",
            "respuesta": respuesta_generacion,
        }

    cdc = respuesta_generacion["results"][0].get("CDC")

    respuesta_estado = consultar_estado(cdc)

    return {
        "estado": "Enviado",
        "cdc": cdc,
        "calcular_de": respuesta_calculo,
        "generar_de": respuesta_generacion,
        "estado_sifen": respuesta_estado,
    }


def actualizar_estado_factura(nombre_fe, resultado):
    doc = frappe.get_doc("Factura Electronica", nombre_fe)

    estado_sifen = (
        resultado.get("estado_sifen", {})
        .get("results", [{}])[0]
        .get("estado_sifen", "")
    )

    if estado_sifen == "Aprobado":
        doc.estado = "Aceptado"
    elif estado_sifen == "Rechazado":
        doc.estado = "Rechazado"
    elif resultado.get("estado") == "Error":
        doc.estado = "Error"
    else:
        doc.estado = "Enviado"

    doc.cdc = resultado.get("cdc")
    doc.estado_sifen = estado_sifen
    doc.respuesta_api = frappe.as_json(resultado)
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
            resultado = enviar_a_factura_segura(factura)
            actualizar_estado_factura(factura.name, resultado)
            frappe.db.commit()
            print(f"Factura Electronica {factura.name} enviada a Factura Segura.")
        except Exception as e:
            marcar_error(factura.name, e)
            frappe.db.commit()
            print(f"Error al sincronizar {factura.name}: {e}")


if __name__ == "__main__":
    sincronizar_facturas()
