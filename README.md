# OpenGen AI

**OpenGen AI** is a lightweight, OpenAI-compatible AI API powered by open-source models.

It allows developers to integrate AI into their applications using a simple HTTP API — no setup, no model management, no infrastructure required.

---

## 🚀 Quick Start

### Endpoint

```text
https://api.opengen.ai/api/v1/chat/completions/
```

---

### Authentication

Use your API key:

```text
Authorization: Bearer sk-opengen-xxxxxxxx
```

---

## 💡 Example Request

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

### Python Example

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

Common status codes:

* `401` → Invalid API key
* `429` → Rate limit exceeded
* `503` → AI service unavailable
* `400` → Bad request

---

## ⚡ Limits

* Max request size: 10,000 characters
* Rate limit: 10 requests/minute per API key

---

## 🧠 Notes

* Fully compatible with OpenAI-style APIs
* Powered by open-source models
* Designed for fast, low-cost inference

---

## 🔑 Create API Key

```bash
curl https://api.opengen.ai/api/v1/api-keys/ -X POST \
  -H "x-admin-key: opengen-admin-secret-key-123"
```

**Response:**
```json
{
  "api_key": "sk-opengen-xxxxxxxx"
}
```

---

## 📚 More

See full documentation in the `doc/` directory.
