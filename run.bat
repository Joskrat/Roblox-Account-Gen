@echo off & cls
title Installing Requirements
python -m pip install colorama requests wget selenium exrex typing maxminddb ipaddress loguru faker pypresence PySocks psutil bs4 tqdm
cls

type batMenu.py
set /p action= %cd% $
if '%action%' == "y" goto start
if '%action%' == "n" exit

:start
@echo off & cls
python main.py
exit
