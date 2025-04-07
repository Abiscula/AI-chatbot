# 🤖 Chatbot com LLaMA 3 via Groq + Flet

Este é um projeto de chatbot em Python que utiliza o modelo **LLaMA 3** da Groq para manter conversas em linguagem natural, com interface criada usando **Flet**, permitindo transformar a aplicação em um app desktop ou até mobile com estilo nativo.

---

## 🚀 Funcionalidades

- Comunicação com modelo LLaMA 3 (70B)
- Interface moderna com Flet
- Suporte a contexto de conversa (mensagens anteriores são mantidas)
- Organizado para fácil manutenção e expansão

---

## 📦 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/chatbot-groq-flet.git
cd chatbot-groq-flet
```

### 2. Crie um ambiente virtual

python -m venv venv

### 3. Ative o ambiente virtual

#### (win) venv\Scripts\activate
#### (linux/mac) source venv/bin/activate

### 4. Instale as dependências

pip install -r requirements.txt

## 🔑 Variáveis de ambiente

Crie um arquivo .env na raiz do projeto com sua chave de API do Groq:

```bash
GROQ_API_KEY=sua_api_key_aqui
```
