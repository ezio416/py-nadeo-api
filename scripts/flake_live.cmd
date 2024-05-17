@echo off
REM run flake8 on nadeo_api.live
REM E501 is the "line too long" error
flake8 --extend-ignore=E501 ../src/nadeo_api/live.py
pause
