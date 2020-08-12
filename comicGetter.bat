@echo on
if exist imgs (
    rmdir /q /s imgs
)

mkdir imgs
cd imgs

python ..\getImage.py
rem ..\getImage.exe
