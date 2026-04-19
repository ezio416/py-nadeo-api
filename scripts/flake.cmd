@echo off

REM E221: multiple spaces before operator
REM E266: too many leading '#'
REM E501: line too long
flake8 --extend-ignore=E221,E266,E501 ../src/nadeo_api
