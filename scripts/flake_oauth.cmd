@echo off
REM run flake8 on nadeo_api.oauth
REM E501 is the "line too long" error
flake8 --extend-ignore=E501 ../src/nadeo_api/oauth.py
pause
