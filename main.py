from flask import Flask, render_template, request, jsonify, Response
import requests
import json
import os
from datetime import datetime

app = Flask(__name__)

# Ollama configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3:mini"

# System prompt for English teaching
SYSTEM_PROMPT = """You are a friendly and patient English teacher from India. Your role is to help students improve their spoken and written English, particularly Indian English.

Guidelines:
- Be warm, encouraging, and positive
- Correct mistakes gently and explain why
- Use simple, clear language
- Provide examples when explaining
- Celebrate progress and effort
- Focus on practical, everyday English
- Be culturally aware of Indian context
- Keep responses concise (2-3 sentences max for conversations)
- If asked to explain grammar, be brief but clear"""

def stream_ollama_response(prompt):
    """Stream response from Ollama"""
    try:
        full_prompt = f"{SYSTEM_PROMPT}\n\nStudent: {prompt}\n\nTeacher:"
        
        payload = {
            "model": MODEL_NAME,
            "prompt": full_prompt,
            "stream": True,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9,
                "max_tokens": 200
            }
        }
        
        response = requests.post(OLLAMA_URL, json=payload, stream=True)
        
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line)
                    if 'response' in data:
                        yield f"data: {json.dumps({'text': data['response']})}\n\n"
                    if data.get('done', False):
                        yield f"data: {json.dumps({'done': True})}\n\n"
                except json.JSONDecodeError:
                    continue
                    
    except Exception as e:
        yield f"data: {json.dumps({'error': str(e)})}\n\n"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    return Response(
        stream_ollama_response(user_message),
        mimetype='text/event-stream',
        headers={
            'Cache-Control': 'no-cache',
            'X-Accel-Buffering': 'no'
        }
    )

@app.route('/health', methods=['GET'])
def health():
    """Check if Ollama is running"""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        if response.status_code == 200:
            return jsonify({'status': 'healthy', 'message': 'System ready'})
    except:
        pass
    return jsonify({'status': 'error', 'message': 'Ollama not running'}), 503

if __name__ == '__main__':
    print("\n" + "="*50)
    print("English Learning Voice Assistant")
    print("="*50)
    print("\nServer starting at: http://localhost:5000")
    print("\nPress Ctrl+C to stop\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)