@echo off
chcp 65001 >nul
echo === Сборка AmirLauncher.exe ===
python -m pip install -r requirements.txt pyinstaller==6.22.3 || goto :err
python -m PyInstaller --noconfirm --clean AmirLauncher.spec || goto :err
echo.
echo Готово: dist\AmirLauncher.exe
pause
exit /b 0
:err
echo.
echo Сборка не удалась — посмотри сообщения выше.
pause
exit /b 1
