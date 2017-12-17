
# Starting Python
From the cmd line : `python`
* from any directory, this requires to add python.exe binary's directory to the PATH
   * `set PATH=%PATH%;C:\python32`
* from the directory that contain the python.exe binary.
* or with the binary with the full path `C:\Python\WinPython-64bit-3.5.3.0Qt5\python-3.5.3.amd64\python`

```
> python
Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```

- `Ctrl+Z+Enter` or `exit()` to exit

# Execute a python script

`> python ./myprogram.py`

You can make a python file executable by adding python binary location as the first line of the file : `#!/usr/bin/python`
<br>To make the file executable on Unix : `$ chmod +x ./myprogram.py`
<br>Then the script can be executed directly: `> ./myprogram.py`

scipt.py
```
print('Hello world')
x = [0,1,2]
y = range(0, 10, 2)
pi = 3.1415926
```

To run a script in interactive mode: script is executed and the interpreter is left open
 `> python -i script.py`
```
Hello world
>>> x
[0, 1, 2]
>>>
```
## Command line arguments
```
import sys
print len(sys.argv) # NOT argc
# Print all arguments:
print sys.argv
# Print all arguments but the program
# or module name:
print sys.argv[1:]  # "array slice"
```

##	Change your current directory
```
>>> import os
>>> os.getcwd()
# 'C:\\Users\\family'

>>> os.chdir("G:\\SW Dev\\Python\\Projects\\Hanoi")
>>> os.chdir("T:\SW Dev\Python\code")
>>> os.chdir()'cd c:\mydir')
```
another option is to add the folder that contains the script to the syspath : `sys.path.append('/my/new/path')`


# Run a python script from the python interpreter (python prompt)
## Using import
Assuming there is a script.py file within the current dir)
`% python`

```
>>>
>>> import script # DO NOT add the .py suffix.  Script is a module here
>>> x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined

>>> script.x   # to make use of x, we need to let Python know which 		    
               # module it came from, i.e. give Python its context
   [0,1,2]
>>> script
>>> <module 'script' from 'T:\\SW Dev\\Python\\code\\script.py'>
>>>
>>> from script import x
>>> x
[0,1,2]
```


```
# promote pi to the top level context
>>> from script import pi
>>> pi
>>> 3.1415926

# Promote all quantities in script.py to the top level context
>>> from script import *
```

## Example
```
# factorial.py
#    Program to compute the factorial of a number
#    Illustrates for loop with an accumulator

def factorial():
    n = eval(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n,1,-1):
       fact = fact * factor
    print("The factorial of", n, "is", fact)

# when importing nothing will be executed but if run from cmd line main() will be executed
if __name__ == '__main__': factorial()
```

`python factorial.py`
>Please enter a whole number: 10
<br>The factorial of 10 is 3628800

`python`
```
>>> from factorial import factorial
>>> factorial()
Please enter a whole number: 10
The factorial of 10 is 3628800
```

```
if __name__ == '__main__': main()
if __name__ == '__main__': main( sys.argv[1:])
```

## execfile (pyton2)
`>>> execfile('script.py')`

## exec (python3)
`>>>exec(open("fact.py").read())`

execute a script and put all it's global variables in the interpreter's global scope
```
exec(open("./fact.py").read(), globals())
exec(compile(open(file).read(), file, 'exec'))
```

```
>>> variables= {}
>>> execfile( "someFile.py", variables )
>>> print variables # globals from the someFile module
```

## runpy: Locating and executing Python modules (without importing them 1st)
https://docs.python.org/3/library/runpy.html#runpy.run_path

```
import runpy
file_globals = runpy.run_path("file.py")
```
There are subtle differences to execfile:
-	`run_path` always creates a new namespace. It executes the code as a module, so there is no difference between globals and locals (which is why there is only a `init_globals` argument). The globals are returned.
<br>`execfile` executed in the current namespace or the given namespace. The semantics of locals and globals, if given, were similar to locals and globals inside a class definition.
-	`run_path` can not only execute files, but also eggs and directories (refer to its documentation for details).


* http://stackoverflow.com/questions/436198/what-is-an-alternative-to-execfile-in-python-3-0
* http://stackoverflow.com/questions/7420937/run-program-in-python-shell
* http://stackoverflow.com/questions/436198/what-is-an-alternative-to-execfile-in-python-3-0
* http://stackoverflow.com/questions/1027714/how-to-execute-a-file-within-the-python-interpreter

```{python}
class python3Execfile(object):
    def _get_file_encoding(self, filename):
        with open(filename, 'rb') as fp:
            try:
                return tokenize.detect_encoding(fp.readline)[0]
            except SyntaxError:
                return "utf-8"

    def my_execfile(filename):
        globals['__file__'] = filename
        with open(filename, 'r', encoding=self._get_file_encoding(filename)) as fp:
            contents = fp.read()
        if not contents.endswith("\n"):
            # http://bugs.python.org/issue10204
            contents += "\n"
        exec(contents, globals, globals)
```

```{python}
subprocess.call(['./abc.py', arg1, arg2])

import sys
sys.argv = ['abc.py','arg1', 'arg2']
execfile('abc.py')

import sys
import subprocess

subprocess.call([sys.executable, 'abc.py', 'argument1', 'argument2'])
```

# py2exe
http://www.py2exe.org/  
https://pypi.python.org/pypi/py2exe#downloads  
pip install py2exe


# help
help()
help> modules / keywords / topics

help("modules")

# Pypedia : Python env on a wiki “Python sandbox”
http://www.pypedia.com/
Collaborative programming web env for the open science. Each article is a python function or class !
