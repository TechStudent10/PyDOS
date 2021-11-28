# PyDOS Commands
This is the commands folder for PyDOS.

## Purpose?
This folder contains all of the internal commands for PyDOS.

## How can I add one?
1. Fork this repository
2. Create a folder in this folder which is called the name of the command.
3. Add an `__init__.py` file.
4. There should be a function called `command` and it takes in some arguments. Copy and paste this onto line 1: `def command(os, config, args, kwargs):` and then press enter.
   1. Now, you can code out your command! The `os` arg is just the OS module so things like `os.path.join()` work. There is no need to import `os`.
   2. The config is essentially the environment variables for PyDOS. You can modify and use the values as you see fit.
   3. `args` and `kwargs` are the command arguments and keyword arguments. Currently, `args` is the only one that works. It's a list of command-line arguments.