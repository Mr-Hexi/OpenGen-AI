import requests
import time
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

class OllamaServiceError(Exception):
    pass

class OllamaTimeoutError(OllamaServiceError):
    pass

class OllamaConnectionError(OllamaServiceError):
    pass

def generate_chat_completion(messages):
    prompt = "\n".join([f"{msg.get('role', 'user').title()}: {msg.get('content', '').strip()}" for msg in messages]) + "\nAssistant:"
    
    payload = {
        "model": "phi",
        "prompt": prompt,
        "stream": False
    }
    
    start_time = time.time()
    try:
        response = requests.post(settings.OLLAMA_URL, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        duration = time.time() - start_time
        logger.info(f"Ollama request completed in {duration:.3f}s")
        return data.get('response', '')
    except requests.exceptions.Timeout:
        duration = time.time() - start_time
        logger.error(f"Ollama request timed out after {duration:.3f}s")
        raise OllamaTimeoutError("Model response timeout")
    except requests.exceptions.ConnectionError:
        logger.error("Failed to connect to Ollama")
        raise OllamaConnectionError("AI backend unavailable")
    except requests.exceptions.RequestException as e:
        logger.error(f"Ollama request failed: {str(e)}")
        raise OllamaServiceError(f"Failed to connect to Ollama or timed out: {str(e)}")
