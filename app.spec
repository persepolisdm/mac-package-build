# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['persepolis/persepolis/__main__.py'],
    pathex=['persepolis/persepolis'],
    binaries=[],
    datas=[],
    hiddenimports=['pkg_resources.py2_warn'],
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
    name='Persepolis Download Manager',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.icns'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Persepolis Download Manager',
)
app = BUNDLE(
    coll,
    name='Persepolis Download Manager.app',
    icon='icon.icns',
    bundle_identifier=None,
    version='5.1.1',
    info_plist={
        'NSPrincipalClass': 'NSApplication',
        'NSAppleScriptEnabled': False,
        'NSHighResolutionCapable': True,
        'CFBundleName': 'Persepolis Download Manager',
        'CFBundleDisplayName': 'Persepolis Download Manager',
        'CFBundleExecutable': 'Persepolis Download Manager',
        'CFBundleIdentifier': 'Persepolis Download Manager',
        'CFBundleIconFile': 'icon.icns',
        'CFBundleInfoDictionaryVersion': '6.0',
        'CFBundlePackageType': 'APPL',
        'CFBundleShortVersionString': '5.1.1'
        },
)
