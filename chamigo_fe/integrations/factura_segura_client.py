import os
import requests

BASE_URL = "https://apitest.facturasegura.com.py"
ESI_URL = f"{BASE_URL}/misife00/v1/esi"


def login():
    email = os.environ.get("FS_EMAIL")
    password = os.environ.get("FS_PASSWORD")

    if not email or not password:
        raise Exception("Faltan variables FS_EMAIL o FS_PASSWORD")

    response = requests.post(
        f"{BASE_URL}/login?include_auth_token",
        json={"email": email, "password": password},
        timeout=30
    )

    response.raise_for_status()
    data = response.json()
    return data["response"]["user"]["authentication_token"]


def llamar_esi(operation, params):
    token = os.environ.get("FS_TOKEN") or login()

    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authentication-Token": token
    }

    response = requests.post(
        ESI_URL,
        headers=headers,
        json={
            "operation": operation,
            "params": params
        },
        timeout=60
    )

    response.raise_for_status()
    return response.json()


def calcular_de(de_resumido):
    return llamar_esi("calcular_de", {"DE": de_resumido})


def generar_de(de):
    return llamar_esi("generar_de", {"DE": de})


def consultar_estado(cdc):
    return llamar_esi(
        "get_estado_sifen",
        {
            "CDC": cdc,
            "dRucEm": "964343"
        }
    )
