@echo off
echo 🚀 Iniciando Hermitage Agent...

REM Verifica si venv existe
if not exist "venv\Scripts\activate.bat" (
    echo 🛠️  Entorno virtual no encontrado. Creándolo...
    python -m venv venv
)

REM Activar entorno
echo ✅ Activando entorno virtual...
call venv\Scripts\activate.bat

REM Instalar dependencias
echo 📦 Instalando requirements...
pip install -r requirements.txt

REM Ejecutar dashboard
echo 📊 Ejecutando dashboard...
streamlit run dashboard.py

pause
