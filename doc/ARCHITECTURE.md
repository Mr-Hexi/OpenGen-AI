# Architecture & Design

This document details the critical components of OpenGen AI and the reasoning behind its architectural choices to stay fully optimized for **low-resource VPS execution**.

## Technical Stack
- **Django 5.0**: Provides robust ORMs and a great administrative backend with negligible overhead.
- **Django REST Framework (DRF)**: Powers the strict serialization schemas and enforces automated handling of 401s, 429s, etc.
- **Local SQLite / MySQL**: Stores `APIKeys` and `ChatLogs`. Since this isn't globally distributed, SQLite functions flawlessly for lightweight caching and validation.
- **Ollama (`phi` model)**: Replaces cloud APIs with an optimized minimal binary model running efficiently without a GPU.

## Key Design Principles

### 1. Security First (Hashes, not Keys)
Normally, providing API keys directly stores raw tokens in full vulnerability within standard startup apps. OpenGen AI resolves this by:
- Operating on `secrets.token_urlsafe(32)` to generate keys natively.
- Using `hashlib.sha256()` hashing out of the gate.
- The DB only retains the `key_hash`.

### 2. Guarding the Model Queue
Language models can get easily throttled or hung by large generation texts. OpenGen prevents resource saturation by:
- Validating the size payload (capped strictly at 10,000 length).
- Adding custom Throttle parameters to the Django configuration limiting usage exclusively (10 req/min currently).

### 3. Graceful Client Errors
A robust API should not return 500 tracebacks. An integral `custom_exception_handler` translates typical backend errors into seamless REST standards:
- *Ollama down*: `service_unavailable` (503 HTTP)
- *Too Many Requests*: `rate_limit_error` (429 HTTP)
- *Invalid API Key*: `authentication_error` (401 HTTP)

## Directory Composition
- `/api/` : Contains payload views, serializers, throttles, and formatting tools.
- `/authentication/` : Houses the logic to authorize, securely hash, and manage local models keys natively.
- `/services/ollama_client.py` : Abstracts requests logic parsing the prompt list and enforcing timeouts so Django workers don't hang indefinitely.
