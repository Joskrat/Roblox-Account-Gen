@echo off & cls
title Run Roblox Gen
set /p action= Install Requirements (y/n):
if '%action%'=='y' goto requests
of '%action%'=='n' goto start

:requirements
title Installing Requirements
python -m pip install colorama requests wget selenium exrex typing maxminddb ipaddress loguru faker pypresence PySocks psutil bs4 tqdm plyer
start


:start
python main.py
pause