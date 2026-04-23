@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo Проверяю библиотеки...

python -c "import requests" >nul 2>&1
if errorlevel 1 (
    echo Устанавливаю requests...
    python -m pip install requests
) else (
    echo [OK] requests
)

python -c "import dotenv" >nul 2>&1
if errorlevel 1 (
    echo Устанавливаю python-dotenv...
    python -m pip install python-dotenv
) else (
    echo [OK] python-dotenv
)

echo.
echo Запускаю программу...
echo.
python weather.py
pause
