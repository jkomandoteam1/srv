from flask import Flask, request, jsonify

app = Flask(__name__)  # <- именно это имя подхватывает Gunicorn

# Простая "база данных" в памяти для токенов
TOKENS = {
    "TEST_TOKEN": "PC_001"
}

@app.route("/auth", methods=["POST"])
def auth():
    data = request.json
    token = data.get("token")
    pc_id = data.get("pc_id")

    if token in TOKENS and TOKENS[token] == pc_id:
        return jsonify({"status": "ok"})
    else:
        return jsonify({"status": "denied"})


@app.route("/register", methods=["POST"])
def register():
    data = request.json
    token = data.get("token")
    pc_id = data.get("pc_id")

    TOKENS[token] = pc_id
    return jsonify({"status": "registered"})


# Важно: для продакшена с Gunicorn НЕ вызываем app.run()
# Gunicorn сам подхватит объект `app`
