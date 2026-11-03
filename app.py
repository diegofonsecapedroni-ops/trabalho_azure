from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MinhaAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/health"):
            resposta = {
                "mensagem": "Minha primeira API Python está funcionando!",
                "status": "ok"
            }
            self.send_response(200)
        else:
            resposta = {"erro": "Rota não encontrada"}
            self.send_response(404)

        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(resposta, ensure_ascii=False).encode("utf-8"))


if __name__ == "__main__":
    servidor = HTTPServer(("0.0.0.0", 8000), MinhaAPI)
    print("API disponível em http://localhost:8000")
    print("Pressione Ctrl+C para encerrar.")

    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
        servidor.server_close()
