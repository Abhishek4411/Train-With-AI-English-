# English Learning Voice Assistant

A lightweight, offline English learning application that helps you practice spoken and written English with AI assistance.

## Features

- 🎤 **Voice Input**: Speak naturally and get instant responses
- 🔊 **Voice Output**: Hear responses in natural-sounding voices
- 💬 **Text Chat**: Type messages if you prefer
- 🤖 **AI-Powered**: Uses local AI (runs on your computer)
- 🌐 **Completely Offline**: No internet needed after setup
- 🇮🇳 **Indian English Support**: Optimized for Indian English learners
- ⚡ **Fast & Lightweight**: Runs on CPU, ~1B parameter model

## Requirements

- Windows 10/11
- Python 3.8 or higher
- At least 4GB RAM
- 2GB free disk space

## Installation (Automatic)

### Step 1: Download Files
Download all the files and place them in a folder.

### Step 2: Run Setup
Double-click `setup.bat` and wait for installation to complete.

This will:
- Install Python dependencies
- Install Ollama (AI runtime)
- Download the AI model (~800MB)

**Note**: If Ollama installer opens, complete the installation and then run `setup.bat` again.

### Step 3: Start the Application
Double-click `start.bat` to launch the application.

Your browser will open automatically at http://localhost:5000

## Manual Installation (Advanced Users)

```bash
# 1. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 2. Install Python packages
pip install -r requirements.txt

# 3. Install Ollama
# Download from: https://ollama.com/download
# Run the installer

# 4. Download AI model
ollama pull phi3:mini

# 5. Start the application
python main.py
```

## Usage

1. **Voice Mode**: Click "Start Speaking" button and speak in English
2. **Text Mode**: Type your message and press Enter or click Send
3. **Voice Selection**: Choose your preferred voice from the dropdown
4. **Practice Topics**: 
   - General conversation
   - Grammar questions
   - Pronunciation practice
   - Writing improvement

## Tips

- Speak clearly and at a moderate pace
- The AI is designed to be patient and encouraging
- Ask for explanations if you don't understand
- Practice regularly for best results

## Troubleshooting

**"Ollama not running" error**:
- Open Command Prompt and run: `ollama serve`
- Then start the app again

**Voice input not working**:
- Check microphone permissions in browser
- Try using Chrome or Edge browser

**AI responses slow**:
- First response may take a few seconds
- Subsequent responses will be faster
- Close other heavy applications

**Model download failed**:
- Check internet connection
- Run: `ollama pull phi3:mini` manually

## File Structure

```
english-learning-assistant/
├── main.py           # Main application
├── setup.bat         # Automatic setup script
├── start.bat         # Application launcher
├── requirements.txt  # Python dependencies
├── README.md         # This file
└── templates/
    └── index.html    # Web interface
```

## Privacy

- All processing happens locally on your computer
- No data is sent to external servers
- Your conversations are not stored
- Completely private and secure

## Credits

Built with:
- Flask (Web framework)
- Ollama (Local AI runtime)
- Phi-3 Mini (Microsoft's small language model)
- Web Speech API (Browser voice features)

## License

Free to use for personal learning purposes.

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Make sure all files are in the same folder
3. Try running setup.bat again

Happy learning! 🎓