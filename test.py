import requests
import sys

# Change this if you customized your .env variable!
BASE_URL = "http://localhost:8080/api/v1"
ADMIN_SECRET = "default-admin-secret-replace-me"

def run_tests():
    print("=========================================")
    print("🔑 STEP 1: Generating a New API Key...")
    print("=========================================")
    
    key_response = requests.post(f"{BASE_URL}/api-keys/", headers={
        "x-admin-key": ADMIN_SECRET
    })
    
    if key_response.status_code != 201:
        print(f"❌ Failed to generate API Key! (Status: {key_response.status_code})")
        print("Response:", key_response.text)
        print("\nMake sure your Django server is running via `python manage.py runserver 8080` in another terminal.")
        sys.exit(1)
        
    api_key = key_response.json().get("api_key")
    print(f"✅ Success! Generated Key: {api_key}")
    
    print("\n=========================================")
    print("🤖 STEP 2: Testing Chat Completion...")
    print("=========================================")
    print(f"Sending a prompt using `{api_key}` to Ollama...\n")
    
    chat_response = requests.post(
        f"{BASE_URL}/chat/completions/",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "messages": [
                {"role": "user", "content": "Just say the exact phrase 'End to end flow is working!'"}
            ]
        }
    )
    
    if chat_response.status_code == 200:
        data = chat_response.json()
        print("✅ Received STATUS 200 OK from AI")
        print("Model Response:")
        print("-----------------------------------------")
        print(data["choices"][0]["message"]["content"].strip())
        print("-----------------------------------------")
        print(f"Request ID: {data['id']}")
    else:
        print(f"❌ Chat Completion Failed! (Status: {chat_response.status_code})")
        print("Response:", chat_response.text)

if __name__ == "__main__":
    run_tests()
