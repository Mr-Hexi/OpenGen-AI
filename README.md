# OpenGen AI

**OpenGen AI** is a lightweight AI API powered by open-source models, designed to be simple, fast, and easy to use.

It allows developers to integrate AI into their applications using a clean HTTP API — no setup, no model management, no infrastructure required.

---

## 🌐 Base URL

```text
https://opengen-ai.duckdns.org/api/v1/
```

---

## 🔐 Authentication

All requests require an API key:

```text
Authorization: Bearer sk-opengen-xxxxxxxx
```

---

## 🔑 Create API Key

To generate an API key:

```bash
curl -X POST https://opengen-ai.duckdns.org/api/v1/api-keys/ \
  -H "x-admin-key: YOUR_ADMIN_SECRET"
```

### Response

```json
{
  "api_key": "sk-opengen-xxxxxxxx"
}
```

> ⚠️ Keep your API key secure. It will not be shown again.

---

## 💡 Example Usage

### cURL

```bash
curl https://opengen-ai.duckdns.org/api/v1/chat/completions/ \
  -H "Authorization: Bearer sk-opengen-your-key" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Explain gravity simply"}
    ]
  }'
```

---

### Python

```python
import requests

response = requests.post(
    "https://opengen-ai.duckdns.org/api/v1/chat/completions/",
    headers={
        "Authorization": "Bearer sk-opengen-your-key"
    },
    json={
        "messages": [
            {"role": "user", "content": "Hello"}
        ]
    }
)

print(response.json())
```

---

## 📥 Request Format

```json
{
  "messages": [
    {"role": "user", "content": "Hello"}
  ]
}
```

---

## 📤 Response Format

```json
{
  "id": "chatcmpl-xxxx",
  "object": "chat.completion",
  "created": 1710000000,
  "model": "phi",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I assist you?"
      },
      "finish_reason": "stop"
    }
  ]
}
```

---

## ⚠️ Errors

All errors follow this format:

```json
{
  "error": {
    "message": "Invalid API key",
    "type": "authentication_error"
  }
}
```

### Common Status Codes

* `401` → Invalid API key
* `429` → Rate limit exceeded
* `503` → AI service unavailable
* `400` → Bad request

---

## ⚡ Limits

* Max request size: 10,000 characters
* Rate limit: 10 requests per minute per API key

---

## 🧠 Notes

* Powered by open-source AI models
* Designed for low-resource environments
* Runs on your own infrastructure

---

## 🚀 Deployment

OpenGen AI is deployed on a cloud VM with:

* Django REST API
* Gunicorn
* Nginx (reverse proxy)
* HTTPS (SSL)
* Automated deployment via GitHub Actions

---

## 📚 More

See additional documentation in the `doc/` directory.
