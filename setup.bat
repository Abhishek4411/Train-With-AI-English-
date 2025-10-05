@echo off
echo ====================================
echo English Learning Assistant Setup
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed!
    echo Please install Python 3.8 or higher from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [1/5] Python found!
echo.

REM Create virtual environment
echo [2/5] Creating virtual environment...
python -m venv venv
call venv\Scripts\activate.bat

REM Install requirements
echo [3/5] Installing Python packages...
pip install --upgrade pip
pip install -r requirements.txt

REM Check if Ollama is installed
where ollama >nul 2>&1
if errorlevel 1 (
    echo.
    echo [4/5] Ollama not found. Installing Ollama...
    echo Downloading Ollama installer...
    curl -L https://ollama.com/download/OllamaSetup.exe -o OllamaSetup.exe
    echo Please run OllamaSetup.exe and complete the installation
    echo After installation, run this setup script again
    start OllamaSetup.exe
    pause
    exit /b 0
) else (
    echo [4/5] Ollama is already installed!
)

REM Download the AI model
echo.
echo [5/5] Downloading AI model (this may take a few minutes)...
ollama pull phi3:mini

echo.
echo ====================================
echo Setup Complete!
echo ====================================
echo.
echo To start the English Learning Assistant:
echo 1. Run: start.bat
echo.
pause