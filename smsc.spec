# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
                     pathex=[],
                     binaries=[('.\\dist\\pydist.dll','.\\dist')],
                     datas=[],
                     hiddenimports=[],
                     hookspath=['.\\dist\pydisthk.py'],
                     runtime_hooks=[],
                     excludes=[],
                     win_no_prefer_redirects=False,
                     win_private_assemblies=False,
                     cipher=block_cipher,
                     noarchive=False
              )
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,        
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='smsc',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True, 
          version='dist\\Resources.rc', 
          icon='.\\smsc.ico')
