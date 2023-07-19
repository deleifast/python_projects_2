#setup.py
from cx_Freeze import setup, Executable
setup(
    name = "Pdvcoral",
    version = "1.1.0",
    options = {"build_exe": {
        'packages': ["os","sys","ctypes","win32con"],
        'include_files': ['icon1.ico'],
        'include_msvcr': True,
    }},
    executables = [Executable("Pdvcoral-LOJA14.py",base="Win32GUI")]
    )
