# OpenGen AI

**OpenGen AI** is a simple AI API that lets you generate responses using open-source models.

You don’t need to install anything or manage models — just send a request and get a response.

---

## 🚀 Quick Start

### Endpoint

```text
https://api.opengen.ai/api/v1/chat/completions/
```

---

### Authentication

Every request requires an API key:

```text
Authorization: Bearer sk-opengen-xxxxxxxx
```

---

## 💡 Example

### cURL

```bash
curl https://api.opengen.ai/api/v1/chat/completions/ \
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
    "https://api.opengen.ai/api/v1/chat/completions/",
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
        "content": "Hello! How can I help you?"
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

## 🔑 Create API Key

```bash
curl https://api.opengen.ai/api/v1/api-keys/ -X POST \
  -H "x-admin-key: opengen-admin-secret-key-123"
```

### Response

```json
{
  "api_key": "sk-opengen-xxxxxxxx"
}
```

> Save your API key securely. It will not be shown again.

---

## 🧠 Notes

* Uses open-source AI models
* Designed to be fast and lightweight
* Works with simple HTTP requests

---

## 📚 More

See additional documentation in the `doc/` directory :).
