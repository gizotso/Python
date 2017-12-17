# Python Setup

## Env
* PATH
PATH : C:\Python34\;C:\Python34\Scripts;

### Windows File association
add .py |.pyw to %PATHEXT%
* http://stackoverflow.com/questions/9037346/making-python-scripts-run-on-windows-without-specifying-py-extension

```
assoc .py=Python.File
ftype Python.File=c:\Python27\python.exe "%1" %*

ftype Python.File="C:\Windows\py.exe" "%1" %*
```

cf utility in windows to set file association
* http://defaultprogramseditor.com/

## Python Startup

PySCripter  /PyScripter/python_init.py
```
from python
from __future__ import print_function
```

set PYTHONSTARTUP PYTHONSTARTUP=/path/to/init.py (works for interactive sessions)

- T:\PortableApps\Python\Python2.7.6.1\App\Lib\site-packages\site.py
   - sitecustomize.py
   - usercustomize.py
- T:\PortableApps\Python\WinPython-32bit-2.7.10.2\python-2.7.10\Lib\site.py
- %WINPYDIR%\WinPython-32bit-3.4.3.5\settings\.ipython\profile_default\startup

```
This is the IPython startup directory

.py and .ipy files in this directory will be run *prior* to any code or files specified
via the exec_lines or exec_files configurables whenever you load this profile.

Files will be run in lexicographical order, so you can control the execution order of files
with a prefix, e.g.::

    00-first.py
    50-middle.py
    99-last.ipy
```

* https://docs.python.org/3.3/tutorial/interpreter.html#the-interactive-startup-file
* https://docs.python.org/3/library/site.html
* http://stackoverflow.com/questions/11404165/python-startup-script


## Python IDE

Komodo, NetBeans, Python Tools for Visual Studio – an add-on for Microsoft Visual Studio, PyStudio, PyDev – an open-source plug-in for Eclipse

### Python IDLE (Integrated DevLopment  Env)
![IDLE](./img/PythonIDLE.png)
Pour ouvrir IDLE, distribué dans la distribution standart de Python, il suffit d'exécuter le fichier <PYTHONHOME>/lib/idlelib/idle.pyw
See alsopython2.7.6.1/App/Lib/dlelib/dle.bat
```
set CURRDIR=%~dp0
start "IDLE" "%CURRDIR%..\..\pythonw.exe" "%CURRDIR%idle.pyw" %1 %2 %3 %4 %5 %6 %7 %8 %9
```

IDLE can be launched from the python prompt
```{python}
>>> import idlelib.PyShell
>>>idlelib.PyShell.main()
```
* http://stackoverflow.com/questions/118260/how-to-start-idle-python-editor-without-using-the-shortcut-on-windows-vista
*	http://stackoverflow.com/questions/2345607/starting-python-idle-from-command-line-to-edit-scripts
*	http://askubuntu.com/questions/337395/open-python-file-with-idle-using-terminal-on-ubuntu-12-04

# Python Package Mgmt
https://packaging.python.org/tutorials/installing-packages/

## pip
a command-line package management system
The executable is located under <%PYTHONHOME%>/Scripts : pip.exe
* https://pip.pypa.io/
* download : https://pypi.python.org/pypi/pip#downloads
* https://pip.pypa.io/en/latest/installing.html
* http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows

```
pip list
pip install [package-name]

pip uninstall [package-name]
```
o	intall pip using : $ python get-pip.py

### pip on windows
* http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows
Python 3.4 (released March 2014) and Python 2.7.9 (released December 2014) ship with Pip
* https://reformatcode.com/code/python/how-to-install-pip-on-windows

### pip-win
tiny Python Package manager that is super easy to install. It automatically installs pip and virtualenv on Windows /pydatalog/python/pip-for-windows
https://sites.google.com/site/pydatalog/python/pip-for-windows

### using pip to list installed packages
```
import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)

sorted(["%s==%s" % (i.key, i.version) for i in pip.get_installed_distributions()])
```
```
['lxml==2.3', 'matplotlib==1.2.1', 'numpy==1.7.1', 'pandas==0.11.0', 'py2exe==0.6.9', 'pycairo==1.8.10', 'pygame==1.9.1', 'pygobject==2.28.3', 'pygoocanvas==0.14.2', 'pygtk==2.24.0', 'pygtksourceview==2.10.1', 'pyodbc==3.0.6', 'pyrsvg==2.32.1', 'pywin32==218', 'scipy==0.12.0']
```

- http://stackoverflow.com/questions/12939975/how-to-list-all-installed-packages-and-their-versions-in-python
- http://stackoverflow.com/questions/739993/how-can-i-get-a-list-of-locally-installed-python-modules

## Setup Tools and Package Manager
**Setuptools** : Easily download, build, install, upgrade, and uninstall Python packages.
Note : distribute is a fork of setuptools (now merged back). setuptools is an enhancement of distutils
- https://pypi.python.org/pypi/setuptools
- [setuptools @wikipedia](http://en.wikipedia.org/wiki/Setuptools)
- [setuptools doc](https://pythonhosted.org/setuptools/index.html)

EasyInstall : Easy Install is a python module (easy_install) bundled with setuptools that lets you automatically download, build, install, and manage Python packages.

```
# install
pip install -U setuptools
pip install git+https://bitbucket.org/pypy/numpy.git
```  

## virtualenv
https://virtualenv.pypa.io/en/latest/
