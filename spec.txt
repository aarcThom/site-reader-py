# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['sr.py'],
    pathex=['.\site_reader'],
    binaries=[],
    datas=[
        ('venv\Lib\site-packages\osgeo\gdalplugins\gdal_ECW_JP2ECW.dll', 'osgeo\gdalplugins'),
        ('venv\Lib\site-packages\osgeo\gdalplugins\gdal_MrSID.dll', 'osgeo\gdalplugins'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='SiteReader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='SiteReader',
)