#Module 1: Introduction 

##Python Language
- Python is high level interpreted language.
- CPython interpreter is the default interpreter used for the python language.Some other interpreters are Jython,IronPython,PyPy etc.

##Phases in execution of python program using python interprer
- Lexical Analysis:Interpreter reads the code and breaks it into tokens suh as keyword,operator,identifier,etc.
- Parsing: Using the tokens from lexical analysis it forms Abstract Syntax Tree(AST).
- Compilation: Converts the AST to bytecode. This is also cached as .pyc file.
- Execution: Executes the bytecode in Python VM.
- Memory Management: Handles the job of managing,allocating and deallocating memory.

##Python2 vs Python3
- The python statement of python2 is replaced by print() function in python3.
- By default python3 strings are stored as unicode but in python2 it needs to be explicitly defined with u"<unicode_string>"
- in python3 '/' operator performs floating point division by default but in python2 it performs absolute division if both operands are integers however if any one is float operand it performs floating point division.'//' is used to perform absolute division in python3.
- in python2 range() returned a list of sequence and xrange() returned a generator. In python3 range returns a generator and there is no xrange().