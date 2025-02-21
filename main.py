import os
import requests
from flask import Flask, redirect, request, jsonify
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

CLIENT_ID = os.getenv("LINKEDIN_CLIENT_ID")
CLIENT_SECRET = os.getenv("LINKEDIN_CLIENT_SECRET")
REDIRECT_URI = os.getenv("LINKEDIN_REDIRECT_URI")

app = Flask(__name__)

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
        return jsonify({"access_token": access_token})
    else:
        return f"Erro ao obter token: {response.text}", response.status_code

# Função para publicar um post no LinkedIn
def post_on_linkedin(access_token, message):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json",
    }

    profile_resp = requests.get("https://api.linkedin.com/v2/me", headers=headers)
    if profile_resp.status_code != 200:
        print(f"❌ Erro ao obter perfil: {profile_resp.text}")
        return

    profile_id = profile_resp.json().get("id")

    post_payload = {
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

    post_resp = requests.post("https://api.linkedin.com/v2/ugcPosts", headers=headers, json=post_payload)

    if post_resp.status_code == 201:
        print("✅ Postagem publicada com sucesso!")
    else:
        print(f"❌ Erro ao publicar: {post_resp.text}")

if __name__ == "__main__":
    print("➡️ Servidor iniciado. Acesse http://localhost:8000 para autorizar o LinkedIn.")
    app.run(host="0.0.0.0", port=8000)