# 🚀 LinkedIn Post Automation
Automação de postagens no LinkedIn usando a API oficial com OAuth2. Desenvolvido em Python com Flask para o fluxo de autenticação.

## 📦 Tecnologias usadas
- Python 3.10+
- Flask
- Requests
- python-dotenv
- Gunicorn (para deploy em produção)

## 🚀 Como rodar localmente
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/linkedin-automation.git
   cd linkedin-automation
   ```
2. Crie o arquivo `.env` com base no `.env.example`:
   ```ini
   NEWS_API_KEY=your_news_api_key
   OPENAI_API_KEY=your_openai_api_key
   LINKEDIN_CLIENT_ID=your_linkedin_client_id
   LINKEDIN_CLIENT_SECRET=your_linkedin_client_secret
   LINKEDIN_REDIRECT_URI=http://localhost:8000/callback
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute a aplicação:
   ```bash
   python main.py
   ```
5. Acesse [http://localhost:8000](http://localhost:8000) e autorize o app no LinkedIn.

---

## ☁️ Deploy no Railway
1. Faça login no [Railway](https://railway.app/).
2. Crie um novo projeto e conecte seu repositório GitHub.
3. Adicione as variáveis de ambiente conforme o `.env.example`.
4. Certifique-se de que o `Procfile` esteja presente com:
   ```
   web: gunicorn main:app --bind 0.0.0.0:$PORT
   ```
5. Faça o deploy e acesse a URL gerada para autorizar o LinkedIn.

---

## 🛡️ Boas práticas
✅ Nunca comite o arquivo `.env`.  
✅ Use o arquivo `.env.example` para demonstrar variáveis de ambiente.  
✅ Utilize variáveis seguras no Railway/Heroku.  

---

## 💻 Resultado
✅ Postagens automáticas no LinkedIn com segurança e facilidade!  
📢 [Veja a documentação oficial da API do LinkedIn](https://learn.microsoft.com/en-us/linkedin/)
```
"# linkedin_automation_ex" 
"# linkedin_automation_ex" 
"# linkedin_automation_ex" 
