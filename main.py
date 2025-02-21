import os
import requests
from flask import Flask, redirect, request, jsonify
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

# Carrega as variáveis do arquivo .env
load_dotenv()

CLIENT_ID = os.getenv("LINKEDIN_CLIENT_ID")
CLIENT_SECRET = os.getenv("LINKEDIN_CLIENT_SECRET")
REDIRECT_URI = os.getenv("LINKEDIN_REDIRECT_URI")

app = Flask(__name__)

# URL para autorização do usuário
AUTH_URL = (
    f"https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={CLIENT_ID}"
    f"&redirect_uri={REDIRECT_URI}&scope=w_member_social%20r_liteprofile"
)

@app.route("/")
def login():
    return redirect(AUTH_URL)

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return "Código de autorização não encontrado.", 400

    response = requests.post(
        "https://www.linkedin.com/oauth/v2/accessToken",
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )

    if response.status_code == 200:
        access_token = response.json().get("access_token")
        with open("access_token.txt", "w") as token_file:
            token_file.write(access_token)
        return jsonify({"access_token": access_token})
    else:
        return f"Erro ao obter token: {response.text}", response.status_code

# Função para publicar um post no LinkedIn
def post_on_linkedin():
    if not os.path.exists("access_token.txt"):
        print("⚠️ Token de acesso não encontrado. Autorize o aplicativo primeiro.")
        return

    with open("access_token.txt", "r") as token_file:
        access_token = token_file.read().strip()

    headers = {
        "Authorization": f"Bearer {access_token}",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json",
    }

    profile_response = requests.get("https://api.linkedin.com/v2/me", headers=headers)
    if profile_response.status_code != 200:
        print(f"❌ Erro ao obter perfil: {profile_response.text}")
        return

    profile_id = profile_response.json().get("id")
    message = "🚀 Postagem automática programada com sucesso às 12h!"

    post_data = {
        "author": f"urn:li:person:{profile_id}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": message},
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
    }

    post_response = requests.post("https://api.linkedin.com/v2/ugcPosts", headers=headers, json=post_data)

    if post_response.status_code == 201:
        print(f"✅ [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Postagem publicada com sucesso!")
    else:
        print(f"❌ Erro ao publicar: {post_response.text}")

# Configura o agendador para postar às 12h todos os dias
scheduler = BackgroundScheduler()
scheduler.add_job(post_on_linkedin, 'cron', hour=12, minute=0)
scheduler.start()

if __name__ == "__main__":
    print("➡️ Servidor iniciado. Acesse http://localhost:8000 para autorizar o LinkedIn.")
    app.run(port=8000)
