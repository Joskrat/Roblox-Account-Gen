@echo off
title Installing Requirements
python -m pip install colorama requests wget selenium exrex typing maxminddb ipaddress loguru faker pypresence 
python main.py
pause