@echo off
REM run flake8 on nadeo_api modules
REM E266 is the "too many leading '#'" error
REM E501 is the "line too long" error
flake8 --extend-ignore=E266,E501 ../src/nadeo_api
pause
