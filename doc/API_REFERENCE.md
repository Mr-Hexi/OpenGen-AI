# API Reference

OpenGen AI supports the typical OpenAI format. Below are the specific routes implemented.

---

### `POST /api/v1/api-keys/`
Generates a new, cryptographically secure API key that acts as the access token across the system. 

#### Headers
- `x-admin-key`: `your-secret-configured-admin-key` (Required)

#### Response Details
**201 Created**
```json
{
  "api_key": "sk-opengen-abc123xyz"
}
```

---

### `POST /api/v1/chat/completions/`
Initializes a new conversational output based on the provided messages.

#### Headers
- `Authorization`: `Bearer sk-opengen-...` (Required)
- `Content-Type`: `application/json`

#### Request Body
```json
{
  "model": "phi",                     // (Optional) Hardcoded exclusively to "phi" behind the scenes
  "messages": [                       // (Required) List of context objects
    {
      "role": "user",
      "content": "Explain gravity simply"
    }
  ]
}
```

#### Response Details
**200 OK**
```json
{
  "id": "chatcmpl-1b9197ff4556",
  "object": "chat.completion",
  "created": 1773997781,
  "model": "phi",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": " Hello! How can I assist you today?\n"
      },
      "finish_reason": "stop"
    }
  ]
}
```

---

### `GET /api/v1/health/`
Performs a check assessing whether the HTTP workers are active and properly receiving context. (Note: does not verify Ollama status).

#### Headers
None required. Auth bypass is enabled here.

#### Response Details
**200 OK**
```json
{
  "status": "ok"
}
```

---

### Understanding the Error Formats
OpenGen AI adheres stringently to typical OpenAI error formats, generally looking like:

```json
{
  "error": {
    "message": "AI backend unavailable",
    "type": "service_unavailable"
  }
}
```

*Status Code Glossary:*
- `400 Bad Request`: When payloads represent malformed structures (i.e missing "messages").
- `401 Unauthorized`: Bad or invalid `sk-opengen-...` tokens.
- `429 Too Many Requests`: Triggered seamlessly by `APIKeyRateThrottle` scoped dynamically per API Key.
- `503 Service Unavailable`: Received securely when the internal model response times out or the backend AI cluster disconnects midway.
