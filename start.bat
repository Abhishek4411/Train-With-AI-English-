@echo off
echo Starting English Learning Assistant...
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Check if Ollama is already running
curl -s http://localhost:11434/api/tags >nul 2>&1
if errorlevel 1 (
    echo Starting Ollama service...
    start /B ollama serve
    echo Waiting for Ollama to start...
    timeout /t 5 /nobreak >nul
) else (
    echo Ollama is already running!
)

REM Start the application
echo Opening your browser at http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

start http://localhost:5000
python main.py