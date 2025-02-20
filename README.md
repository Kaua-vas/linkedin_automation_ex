# 🚀 LinkedIn Post Automation

Este projeto permite a **automação de postagens no LinkedIn** usando a **API oficial com OAuth2**. O código foi projetado para ser simples, seguro e fácil de configurar, funcionando tanto localmente quanto em plataformas de deploy como Railway.

---

## 📝 **Visão geral do projeto**
O projeto realiza as seguintes funções:
- Autenticação no LinkedIn via OAuth2.
- Publicação automática de postagens no perfil do usuário.
- Facilidade de configuração através de variáveis de ambiente.
- Possibilidade de rodar localmente ou em produção (Railway).

---

## 🛠️ **Arquivos e estrutura do projeto**
```
linkedin-automation/
├── .env.example           # Exemplo de variáveis de ambiente
├── .gitignore             # Arquivos a serem ignorados pelo Git
├── main.py                # Código principal da aplicação
├── Procfile               # Comando de inicialização para deploy em produção
├── README.md              # Guia de uso e configuração
└── requirements.txt       # Dependências do projeto
```

---

## ⚙️ **Como configurar e rodar o projeto**

### 1️⃣ Instale as dependências
Certifique-se de que você tem o **Python 3.10+** instalado. Em seguida, execute:
```bash
pip install -r requirements.txt
```

---

### 2️⃣ Configure as variáveis de ambiente
O projeto utiliza variáveis de ambiente para armazenar chaves e credenciais. Para configurar:
1. Faça uma cópia do arquivo de exemplo:
   ```bash
   cp .env.example .env
   ```
2. No arquivo `.env`, preencha os seguintes campos com seus dados:
```ini
# Chaves das APIs (substitua pelos seus próprios valores)
NEWS_API_KEY=your_news_api_key
OPENAI_API_KEY=your_openai_api_key

# Credenciais OAuth2 do LinkedIn
LINKEDIN_CLIENT_ID=your_linkedin_client_id
LINKEDIN_CLIENT_SECRET=your_linkedin_client_secret
LINKEDIN_REDIRECT_URI=http://localhost:8000/callback
```
🔒 **Importante:** Nunca compartilhe ou comite seu arquivo `.env`.

---

### 3️⃣ Execute a aplicação localmente
Para rodar a aplicação localmente:
```bash
python main.py
```
O terminal exibirá:
```
➡️ Servidor iniciado. Acesse http://localhost:8000 para autorizar o LinkedIn.
```
✅ Acesse o link fornecido, autorize a aplicação e copie o `access_token` exibido.

---

### 4️⃣ Faça uma postagem no LinkedIn
Depois de obter o `access_token`, utilize a função `post_on_linkedin` no `main.py`:
```python
access_token = "your_access_token"
post_on_linkedin(access_token, "🚀 Postagem automatizada via API do LinkedIn!")
```
Rodando o script, sua postagem será publicada no LinkedIn.

---

## ☁️ **Como rodar em produção (Railway)**
Se desejar rodar 24/7 em produção:

### 1️⃣ Configuração do Railway
1. Crie um novo projeto no [Railway](https://railway.app/).
2. Adicione as variáveis de ambiente do arquivo `.env.example` no painel de **Settings → Variables**.
3. Certifique-se de que o projeto contém um arquivo `Procfile` com o conteúdo:
   ```procfile
   web: gunicorn main:app --bind 0.0.0.0:$PORT
   ```
4. Clique em **Deploy**. O Railway gerará uma URL pública.
5. Acesse essa URL e autorize a aplicação para obter o `access_token`.

🔑 O Railway mantém a aplicação rodando em segundo plano, permitindo que a automação seja executada continuamente.

---

## 🚨 **O que precisa ser alterado para funcionar**
✅ Preencha as variáveis no arquivo `.env` com suas próprias credenciais.  
✅ Ajuste a variável `LINKEDIN_REDIRECT_URI` com a URL correta (localmente ou fornecida pelo Railway).  
✅ Utilize um `access_token` válido para realizar postagens.  
✅ Se for usar em produção, garanta que todas as variáveis estejam definidas no ambiente do Railway.  

---

## 💻 **Resultado esperado**
- Obtenção do token OAuth2 via LinkedIn.  
- Postagens automáticas publicadas diretamente no seu perfil.  
- Rodando localmente para testes ou em produção para operação contínua.  

---

## 🛑 **Dicas de segurança**
- Sempre adicione `.env` ao `.gitignore` para evitar vazamento de chaves.  
- Utilize o arquivo `.env.example` apenas como referência para configuração.  
- Nunca compartilhe seu `access_token` ou outras credenciais publicamente.  

---

🚀 **Com esses passos, qualquer pessoa poderá rodar e configurar o projeto com facilidade e segurança!** 😊
