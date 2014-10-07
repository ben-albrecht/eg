# -*- coding: utf-8 -*-
"""setup -- setuptools setup file for kytten.
GUI Framework for Pyglet
"""

__author__ = "Conrad 'Lynx' Wong(originator) Raymond Chandler III(forker)"
__author_email__ = "raymondchandleriii@gmail.com"
__version__ = "6.0.0"
__date__ = "2011 07 31"

try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

from setuptools import setup, find_packages

f = open('README','rU')
long_description = f.read()
f.close()

setup(
    name = "kytten",
    version = __version__,
    author = "Conrad 'Lynx' Wong(originator) Raymond Chandler III(fork)",
    license="BSD",
    description = "GUI Framework for Pyglet",
    long_description=long_description,
    url = "https://github.com/kitanata/kytten",
    download_url = "https://github.com/kitanata/kytten/tarball/master",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        ("Topic :: Software Development :: Libraries :: Python Modules"),
        ("Topic :: Games/Entertainment"),
        ],
 
    packages = find_packages(),

    install_requires=['pyglet>=1.1.4'],

    dependency_links=['http://code.google.com/p/pyglet/downloads/list'],

    include_package_data = True,
    zip_safe = False,
)
