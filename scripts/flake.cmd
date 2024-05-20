@echo off
REM run flake8 on nadeo_api modules
REM E501 is the "line too long" error
flake8 --extend-ignore=E501 ../src/nadeo_api/__init__.py
flake8 --extend-ignore=E501 ../src/nadeo_api/auth.py
flake8 --extend-ignore=E501 ../src/nadeo_api/core.py
flake8 --extend-ignore=E501 ../src/nadeo_api/live.py
flake8 --extend-ignore=E501 ../src/nadeo_api/meet.py
flake8 --extend-ignore=E501 ../src/nadeo_api/oauth.py
flake8 --extend-ignore=E501 ../src/nadeo_api/util.py
pause
