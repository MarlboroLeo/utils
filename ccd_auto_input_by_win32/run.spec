# -*- mode: python -*-

block_cipher = None


a = Analysis(['run.py'],
             pathex=['auto_input_ui.py', 'auto_input_win32.py', 'D:\\Leau\\code\\ccd_auto_input_win32'],
             binaries=[],
             datas=[],
             hiddenimports=['auto_input_ui', 'auto_input_win32'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='run',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='favicon.ico')
