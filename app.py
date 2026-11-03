
import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

import mysql.connector


class MinhaAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        caminho = self.path.split("?")[0]

        if caminho in ("/", "/health"):
            resposta = {
                "mensagem": "Minha primeira API Python está funcionando!",
                "status": "ok"
            }

            self.enviar_json(200, resposta)

        elif caminho == "/db":
            try:
                conexao = mysql.connector.connect(
                    host=os.getenv("DB_HOST", "mysql"),
                    user=os.getenv("DB_USER", "api_user"),
                    password=os.getenv("DB_PASSWORD"),
                    database=os.getenv("DB_NAME", "trabalho_azure")
                )

                conexao.close()

                self.enviar_json(200, {
                    "status": "ok",
                    "banco": "MySQL conectado"
                })

            except Exception as erro:
                self.enviar_json(503, {
                    "status": "erro",
                    "mensagem": str(erro)
                })

        else:
            self.enviar_json(404, {"erro": "Rota nao encontrada"})

    def enviar_json(self, codigo, dados):
        conteudo = json.dumps(dados, ensure_ascii=False).encode("utf-8")

        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(conteudo)))
        self.end_headers()
        self.wfile.write(conteudo)


servidor = HTTPServer(("0.0.0.0", 8000), MinhaAPI)
print("API rodando na porta 8000")
servidor.serve_forever()
