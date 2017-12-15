from distutils.core import setup, Extension
from Cython.Build import cythonize
from shutil import move
import os

# build and move cythonized files manually
# easier than trying to fit everything into a module distutils style
to_build = []
to_move = {}
for root, dirs, files in os.walk(".", topdown=False):
    for fname in files:
        if ".pyx" in fname:
            name = fname.split(".")[0]
            fpath = os.path.join(root, fname)
            to_build.append([name, fpath])
            to_move[name] = root


extensions = [Extension(name, [fpath]) for name, fpath in to_build]
setup(
    ext_modules = cythonize(extensions)
)

for fname in os.listdir("."):
    if ".so" in fname:
        name = fname.split(".")[0]
        move(fname, os.path.join(to_move[name], fname))