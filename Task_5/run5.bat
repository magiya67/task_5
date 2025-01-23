@echo off
echo =============================================
echo Jump here http://192.168.0.14:8000/api/users/
echo =============================================
cd /d "C:\Users\zhaka\PycharmProjects\Django-homework\"
call .venv\Scripts\activate.bat
python Task_5\manage.py runserver 192.168.0.14:8000

pause
