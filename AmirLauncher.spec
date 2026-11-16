# -*- mode: python ; coding: utf-8 -*-
# Сборка в один .exe:  pyinstaller AmirLauncher.spec   (или просто запусти build_exe.bat)
# Готовый файл появится в папке dist/.

a = Analysis(
    ["AmirLauncher.py"],
    pathex=[],
    datas=[("assets", "assets")],  # картинки вшиваются внутрь exe
    hiddenimports=["PySide6.QtMultimedia"],
    excludes=["tkinter", "pytest"],
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="AmirLauncher",
    icon="assets/logo.ico",
    console=False,  # без чёрного окна консоли
    upx=False,
)
