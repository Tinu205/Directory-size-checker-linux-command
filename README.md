# Directory-size-checker-linux-command
Directory size checker is a simple command line tool that allows user to get the size of the given directory. With this tool user can obtain the size of the directory rigth from the command line. This tool is written in python and uses [sys](https://docs.python.org/3/library/sys.html) and [os](https://docs.python.org/3/library/os.html) libraries. The tool is easy to use, the user must simply type the command followed by the path to the directory.
## Creating the command

Open your terminam and type
```bash
nano get_size
```

Now copy the code from the repository and paste it in the terminal, then save it and close it.
Get your current working directory by the command

```bash
pwd
```

Copy your current working directory, open termianal and type 
```bash
nano .bashrc
```

Go to the end of the file and type the command (replace /path/of/diretory with what you have copied)
```bash
export PATH = $PATH :/path/to/direcotry
```

Save it and close it !

Now refresh the bashrc by the command
```bash
source ~/.bashrc
```

Now give the file the executable permission by typing
```bash
chmod +x get_size
```
And now everything is went well and command is created 

## Using the command 

Just type
```bash
get_size /path/to/directory
```
