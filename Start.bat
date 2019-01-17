::  This batch file checks environment and automatically
:: set environment to run python file in Windows command
:: line. Made by jihun Kim(happyh4cking@gmail.com). Made
:: in 2016/05/03.
@echo off
echo Need Python 2.7 to run this program.
echo Checking environment variable..
echo.
path|find "Python27" > nul
if %ERRORLEVEL% == 0 (
python BookManagement.py
exit
) else (
echo Python 2.7 not found in environment variable.
)
if exist "C:\Python27" (
echo Found C:\Python27
setx path "%PATH%;C:\Python27;"
echo Python 2.7 added to environment variable.
pause
python BookManagement.py
exit
) else (
echo Can't find C:\Python27
pause
)