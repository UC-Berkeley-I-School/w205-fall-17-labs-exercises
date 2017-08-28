# MIDS W205

##Lab #              0     (In Development)

## A Brief Introduction to Linux and Debugging

In this optional lab we will go over some basics of a Linux system and coding in python and applications based on Java such as Hadoop and Spark. It is highly recommended if you don't use Linux in your day-to-day work that you review this lab.

## Some Definitions

Here's just a few definitions and some links to expose you to some of the language we'll use. 


| What | Definition | Resource | 
| ------------- |:-------------| :-----------------------------------------------------------------|
| Linux | Linux is an operating system similar to Windows or MacOS which is typically used for mission-critical applications or programming. | [https://www.linux.com/what-is-linux/](https://www.linux.com/what-is-linux) |
| GUI | A graphical user interface (GUI) is the typical frontend human-computer interface involving windows, icons, browsers, etc. | [http://www.linfo.org/gui.html](http://www.linfo.org/gui.html) |
| CLI | A command line interface (CLI) is a text only environment accessed solely by a keyboard | [http://askubuntu.com/questions/506510/what-is-the-difference-between-terminal-console-shell-and-command-line](http://askubuntu.com/questions/506510/what-is-the-difference-between-terminal-console-shell-and-command-line) | 
| stdin | Is the default datastream going into an application. stdin for a command line is what you type | [http://stackoverflow.com/questions/3385201/confused-about-stdin-stdout-and-stderr](http://stackoverflow.com/questions/3385201/confused-about-stdin-stdout-and-stderr) |
| stdout | Is the default datastream leaving the application. stdout is typicall what gets sent back to you after running a command in the command line | [http://stackoverflow.com/questions/3385201/confused-about-stdin-stdout-and-stderr](http://stackoverflow.com/questions/3385201/confused-about-stdin-stdout-and-stderr) |
| stderr | Is the default datastream for errors in the application. This is seperated from stdout so that you know why your program broke.  | [http://stackoverflow.com/questions/3385201/confused-about-stdin-stdout-and-stderr](http://stackoverflow.com/questions/3385201/confused-about-stdin-stdout-and-stderr) |
| Java | Java is a programming language that is typically used to develop applications that are large long running projects. Because of how the the underlying technology works it helps keep the application organized and maintainable. | [https://www.quora.com/Why-do-large-corporations-use-Java-or-C-over-Python-Ruby-and-PHP](https://www.quora.com/Why-do-large-corporations-use-Java-or-C-over-Python-Ruby-and-PHP) |
| Python | Python is a programming language that is very easy to pick up and allows several different styles of development. Python also lends itself to small-scale applications, but has uses in large-scale applications as well | [http://www.linuxjournal.com/content/python-scripts-replacement-bash-utility-scripts](http://www.linuxjournal.com/content/python-scripts-replacement-bash-utility-scripts)  |
| Runtimes | Runtimes are a library of functions used by a programming language so it knows what you're talking about. | [http://stackoverflow.com/questions/3900549/what-is-runtime](http://stackoverflow.com/questions/3900549/what-is-runtime) |
| PEPs | Python Enhancement Proposals (PEPs) are a group of language changes made to Python to make it more reliable. If you're having a problem with your code and you're following a post from 5 years ago, chances are there's been a change in Python since then | [https://www.python.org/dev/peps/](https://www.python.org/dev/peps/) |
| Python 2 vs Python 3 | Sometime ago the developers of Python decided they made some mistakes with how the language was initially designed and decided to make breaking changes in an update. This led to a split since people relied on their code for the older version. It is good to be aware that Python 2 and Python 3 are different, but mostly the same and most mainstream modules have been updated to serve both.  | [https://wiki.python.org/moin/Python2orPython3](https://wiki.python.org/moin/Python2orPython3) |
| Python Virtual Environment | Since Python has many different versions/runtimes we sometimes want to make sure we run it using a particular set of functions so we know the behavior to avoid it breaking. Python has virtual environments which isolate the runtimes so you can choose exactly what libraries are used in your code | [https://www.quora.com/What-are-the-differences-between-a-Virtual-Machine-Interpreter-Compiler-Executable-Runtime-Library-and-Runtime-system-program-wise](https://www.quora.com/What-are-the-differences-between-a-Virtual-Machine-Interpreter-Compiler-Executable-Runtime-Library-and-Runtime-system-program-wise) |


## GUI vs Command Line

With great power comes great responsibility. A GUI limits your ability to really do things with your application since someone designed the GUI to let you make those changes. However in a CLI environment you can control the exact details of what you're doing and how you're doing it.

Windows is typicall only used from the GUI; however, you could open a command prompt or powershell console to access the low-level environmen that the GUI is built on.

Linux also has a GUI for some desktop environmnets, but is usually only a CLI in practice. In this class we will be using Amazon Web Service EC2 instances which do not have GUIs.

## Types of CLI shells

CLIs come in many different flavors just like operating systems. Some people have preferences. The default shell for most CLIs is Bash, but there are a few others. We will use Bash for the rest of the lab Here's just a list and a reference if you're interested make sure you dive deeper!

- Bash
- tcsh
- zsh
- fish
- xonsh

[https://wiki.archlinux.org/index.php/Command-line_shell](https://wiki.archlinux.org/index.php/Command-line_shell)

## Getting help!

The best way to find help in this class is using the #w205 Slack channel in the UCB iSchool Slack (reference link here), your professor, and stackoverflow. You should always try to solve the problem yourself first using resources avaliable to you, but asking questions is how we learn!

## Getting to a shell (Need a better option)

If you're running Linux or MacOS you have a bash terminal readily avaliable.

Linux [http://www.howtogeek.com/howto/22283/four-ways-to-get-instant-access-to-a-terminal-in-linux/](http://www.howtogeek.com/howto/22283/four-ways-to-get-instant-access-to-a-terminal-in-linux/)

MacOS [http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line](http://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line)

If you're running Windows you might have a few issues since it doesn't have an included bash shell. If you know how to get to a bash shell, use an environment you're familiar with; however, if you don't there is an emulated shell avaliable at [http://www.tutorialspoint.com/execute_bash_online.php](http://www.tutorialspoint.com/execute_bash_online.php). It won't work for all commands, but it's a good first step. The shell is avaliable at the bottom of the page (the green area). We'll talk about how to access remote computers later in this lab and you'll actually connect to one for lab 2.

## Basic commands and questions

### First pass

Try asking yourself some basic questions and running these in the shell. Sometimes you'll be surprised at just how simple a lot of this is.

#### Where am I? (Present working directory)

`pwd`

#### What's in here? (List contents of present working directory)

`ls`

#### Can I move around?

`cd /where/I/want/to/be`

Let's also note that `.` is here and `..` is one level down.

#### Who am I?

`whoami`

#### What is this thing? (Can pass variables and strings to get values)

`echo bob`

#### How does this program work? (What's the manual say?)

`man ls`

You can press q to quit out of the manual

### Command flags

Were you wondering if you could do thing's a little bit differently? What if I want to have a list. Well turns out someone did that for us most of the time for simple things. We do this by passing flags to the command using `-`. You can see a list of these flags in the man page for the program.

#### Extending ls

- Can I get a list instead of a table? `ls -l` 
- Can I list all files including hidden files? (files prepended with a . like .bashrc) `ls -a`
- Can I do both? `ls -la`

### Variables in bash

What if you have something you want to use a lot but don't want to type it 100 times. Why not just store it somewhere? Bash has variables and you can create them using the `=` symbol and read them out using `echo`. Varialbes are called through the `$` symbol and are conventially all capitalized.

Try running these commands:
- `BOB=bob`
- `echo $BOB`


### What can I run?

I really wish I knew how bash knew what I was able to run. I wonder how it knows where to look? I guess it has to look down a path to find it. Let's see if there is a PATH variable.

`echo $PATH$`

This is the list of directories that your shell know's where to look for applications.

## Editing files

There are a few applications for editing files.

- nano
- vim
- emacs

As far as learning curve nano is the simplest with a basic interface and a few commands for saving and moving throguh the file. If you're not familiar with vim or emacs I'd recommend nano.

`nano bob.txt`

Notice at the bottom there is several command shortcuts listed. The `^` indicates ctrl, so ctrl+x is exit. If changes have been made it will ask if you want to save.

Type `Merry had a little lamb. Jimmy did not.` then save and close.

Now running `ls` you should see `bob.txt` in your directory. Run `nano bob.txt` again and you should see what you initially wrote in. 

Let's add a line to `bob.txt`. Add a new line with `Joe was sad. Moe was hungry.` and save. Close out and now we'll work on how to do things with the file.

## File handling

#### What if we want to output the file instead of edit it?

`cat file` or `cat bob.txt`

#### I want to move the file?

`mv bob.txt joe.txt`
`ls`

#### Copy the file?

`cp joe.txt bob.txt`
`ls`

#### Remove the file?

`rm joe.txt`
`ls`

#### How many words in a file?

`wc -w bob.txt`

#### How many lines in a file?

`wc -l bob.txt`

#### Top lines in a file?

`head -1 bob.txt`
`head -2 bob.txt`

#### Bottom lines in a file?
`tail -1 bob.txt`
`tail -2 bob.txt`

## Parsing data

Linux has some great tools for parsing data that are extremely versitile and can't be taught 100% in this lab. A great example of how to use some of these tools is avaliable here: [Command-line tools can be 235x faster than your Hadoop cluster](https://web.archive.org/web/20161227191842/http://aadrake.com/command-line-tools-can-be-235x-faster-than-your-hadoop-cluster.html). This acticle is a great example of right tool for the right job. Not all problems can be attacked this way and thus we use technologies such as Hadoop and Spark.

`awk` is one of the most verstile tools with lots of references avaliable online. I'm just going to do a basic example and provide some reference for examples below. 

Let's just say I want to split the lines of my file on the sentences and print the first sentence of each line. I would need to specify a field seperator using the `-F` flag and print out the first element while also specifying which file. 

`awk -F. '{print $1}' bob.txt`

Merry had a little lamb

Joe was sad

`awk -F. '{print $2}' bob.txt`

 Jimmy did not
 
 Moe was hungry

#### Referenes

[https://www.tutorialspoint.com/awk/awk_basic_examples.htm](https://www.tutorialspoint.com/awk/awk_basic_examples.htm)
[https://www.ibm.com/developerworks/library/l-awk1/](https://www.ibm.com/developerworks/library/l-awk1/)
[http://www.folkstalk.com/2011/12/good-examples-of-awk-command-in-unix.html](http://www.folkstalk.com/2011/12/good-examples-of-awk-command-in-unix.html)

## Chaining commands

What happens if I want to use some of these tools together and parse the output of another output? Bash handles these using pipes `|` which tells it to take the stdout and "pipe" it to stdin of the next command. Let's look at a few examples. Let's figure out the number of files in my folder which have the .txt extention. I can use the wildcard `*` to specify all things that match a given string using `*.txt`. Use `ls *.txt` to determine what the count should be by eye. Let's put what we've learned together to figure this out.

Steps:
1. List all files that have the txt extention
2. Count the number of lines using wc

`ls *.txt | wc -l`

Let's assume we were less industrious and didn't realize wordcount would work in this instance and I used the awk hammer.

`ls *.txt | awk 'BEGIN{i=0}{i++;}END{print i}'`

Add a few .txt files and try both of these commands again.

## Redirection

## Security

## File Privledges

## Firewalls

## SSH

## Webservers

## Version Control

GitHub has put a lot of effort into building a tutorial that will let you use their platform effectively. Let's not recreate the wheel and use theirs [https://try.github.io/](https://try.github.io/)

## Debugging

## Accessing remotely

## Python

## Python 2 vs 3

## Python Runtimes

## Python Environments

