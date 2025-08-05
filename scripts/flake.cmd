@echo off
REM run flake8 on nadeo_api modules
REM E266 is "multiple spaces before operator"
REM E266 is "too many leading '#'"
REM E501 is "line too long"
flake8 --extend-ignore=E221,E266,E501 ../src/nadeo_api
pause
