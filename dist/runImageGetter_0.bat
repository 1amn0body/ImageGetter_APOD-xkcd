@echo off
if exist imgs (
    rmdir /q /s imgs
)

mkdir imgs
cd imgs

..\runImageGetter_0.exe
