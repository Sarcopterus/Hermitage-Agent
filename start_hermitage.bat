@echo off
setlocal

:menu
cls
echo =====================================
echo        🧠 HERMlTAGE IA LAUNCHER
echo =====================================
echo.
echo 1. Ejecutar agentes (main.py)
echo 2. Analizar logs y generar CSV
echo 3. Abrir dashboard interactivo
echo 4. Limpiar logs antiguos
echo 5. Regenerar base vectorial
echo 6. Salir
echo.

set /p choice="Selecciona una opción (1-6): "

if "%choice%"=="1" goto agents
if "%choice%"=="2" goto analyze
if "%choice%"=="3" goto dashboard
if "%choice%"=="4" goto clean_logs
if "%choice%"=="5" goto rebuild_vector
if "%choice%"=="6" exit

goto menu

:agents
call venv\Scripts\activate.bat
python Hermitage\main.py
pause
goto menu

:analyze
call venv\Scripts\activate.bat
python Hermitage\analyze_logs.py
pause
goto menu

:dashboard
call venv\Scripts\activate.bat
streamlit run Hermitage\dashboard.py
goto menu

:clean_logs
echo 🧹 Limpiando carpeta de logs...
del /Q /F Hermitage\logs\*.log
echo ✅ Logs eliminados.
pause
goto menu

:rebuild_vector
call venv\Scripts\activate.bat
python Hermitage\Agents\build_vector_db.py
pause
goto menu
