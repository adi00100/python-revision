#Module 2: Fundamentals of Python 

##Interpreter and compilers
- Interpreter reads the code excutes it line by line by translating it to machine code while compiler converts the whole code to machine code at once.
- Interpreter may need to re-translate the same line again and again depending on the condition like in a loop.
- C++,C are compiled languages which uses compiler while python is a interpreted language using compiler.  

####Steps in executing a python program by a interpreter
- Lexical Analysis:Interpreter reads the code and breaks it into tokens suh as keyword,operator,identifier,etc.
- Parsing: Using the tokens from lexical analysis it forms Abstract Syntax Tree(AST).
- Compilation: Converts the AST to bytecode. This is also cached as .pyc file.
- Execution: Executes the bytecode in Python VM.
- Memory Management: Handles the job of managing,allocating and deallocating memory.

##Semantics, Syntax, and Lexing
- Semantics:It defines what the program does on execution.
- Syntax:It defines how to use keywords,variables,operators and operands to create a executable program.
- Lexing: Process of breaking down codes to tokens.Same as in Lexical Analysis in interpreter section.
##Keywords
- Keywords: Set of reserved words that have specific meaning and purpose in language. eg: in,and,not,from,is,with etc
##Intro to REPL(Read-Evaluate-Print-Loop)
- It is a type of interactive shell that allows to enter python code in real time.
- In windows open a command prompt and enter the command "py" or "python" to start a REPL shell.
- One needs to enter each code line by line and may evaluate the output.
- However since its real time and interactive the code enetered is not saved for future purpose. So it should be used only to test some logic or for some simple purpose. 
##Virtual Environments in python
- It is a self contained environment to manage package seperately from global packages.
- It is generally used so that dependencies can be managed,similar enviornment can be reproduced so that the project can function similarly in different systems and isolates the packages so that it doesn't affect the  global environment or other projects environment.
- Python Language has a built in module calle venv wich features the creation of virtual environment in python.
###Steps to create and activate virtual environment using venv
- Open a terminal in desired project folder.
- Insert the command `python -m venv env`.
- Activavte the virtual environment using the `./env/Scripts/activate` for windows and `source './env/bin/activate'` for linux.
- Only the packaged installed within the above terminal session are managed in python virtual envirronment.