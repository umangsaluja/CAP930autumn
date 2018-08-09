Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> A=10
>>> A
10
>>> 
========= RESTART: C:/Users/HP/Desktop/CAP930autumn/firstprogram.py =========
HELLO WORLD 10
>>> help()

Welcome to Python 3.6's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.6/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> def
Function definitions
********************

A function definition defines a user-defined function object (see
section The standard type hierarchy):

   funcdef                 ::= [decorators] "def" funcname "(" [parameter_list] ")" ["->" expression] ":" suite
   decorators              ::= decorator+
   decorator               ::= "@" dotted_name ["(" [argument_list [","]] ")"] NEWLINE
   dotted_name             ::= identifier ("." identifier)*
   parameter_list          ::= defparameter ("," defparameter)* ["," [parameter_list_starargs]]
                      | parameter_list_starargs
   parameter_list_starargs ::= "*" [parameter] ("," defparameter)* ["," ["**" parameter [","]]]
                               | "**" parameter [","]
   parameter               ::= identifier [":" expression]
   defparameter            ::= parameter ["=" expression]
   funcname                ::= identifier

A function definition is an executable statement.  Its execution binds
the function name in the current local namespace to a function object
(a wrapper around the executable code for the function).  This
function object contains a reference to the current global namespace
as the global namespace to be used when the function is called.

The function definition does not execute the function body; this gets
executed only when the function is called. [3]

A function definition may be wrapped by one or more *decorator*
expressions. Decorator expressions are evaluated when the function is
defined, in the scope that contains the function definition.  The
result must be a callable, which is invoked with the function object
as the only argument. The returned value is bound to the function name
instead of the function object.  Multiple decorators are applied in
nested fashion. For example, the following code

   @f1(arg)
   @f2
   def func(): pass

is roughly equivalent to

   def func(): pass
   func = f1(arg)(f2(func))

except that the original function is not temporarily bound to the name
"func".

When one or more *parameters* have the form *parameter* "="
*expression*, the function is said to have "default parameter values."
For a parameter with a default value, the corresponding *argument* may
be omitted from a call, in which case the parameter's default value is
substituted.  If a parameter has a default value, all following
parameters up until the ""*"" must also have a default value --- this
is a syntactic restriction that is not expressed by the grammar.

**Default parameter values are evaluated from left to right when the
function definition is executed.** This means that the expression is
evaluated once, when the function is defined, and that the same "pre-
computed" value is used for each call.  This is especially important
to understand when a default parameter is a mutable object, such as a
list or a dictionary: if the function modifies the object (e.g. by
appending an item to a list), the default value is in effect modified.
This is generally not what was intended.  A way around this is to use
"None" as the default, and explicitly test for it in the body of the
function, e.g.:

   def whats_on_the_telly(penguin=None):
       if penguin is None:
           penguin = []
       penguin.append("property of the zoo")
       return penguin

Function call semantics are described in more detail in section Calls.
A function call always assigns values to all parameters mentioned in
the parameter list, either from position arguments, from keyword
arguments, or from default values.  If the form ""*identifier"" is
present, it is initialized to a tuple receiving any excess positional
parameters, defaulting to the empty tuple. If the form
""**identifier"" is present, it is initialized to a new ordered
mapping receiving any excess keyword arguments, defaulting to a new
empty mapping of the same type.  Parameters after ""*"" or
""*identifier"" are keyword-only parameters and may only be passed
used keyword arguments.

Parameters may have annotations of the form "": expression"" following
the parameter name.  Any parameter may have an annotation even those
of the form "*identifier" or "**identifier".  Functions may have
"return" annotation of the form ""-> expression"" after the parameter
list.  These annotations can be any valid Python expression and are
evaluated when the function definition is executed.  Annotations may
be evaluated in a different order than they appear in the source code.
The presence of annotations does not change the semantics of a
function.  The annotation values are available as values of a
dictionary keyed by the parameters' names in the "__annotations__"
attribute of the function object.

It is also possible to create anonymous functions (functions not bound
to a name), for immediate use in expressions.  This uses lambda
expressions, described in section Lambdas.  Note that the lambda
expression is merely a shorthand for a simplified function definition;
a function defined in a ""def"" statement can be passed around or
assigned to another name just like a function defined by a lambda
expression.  The ""def"" form is actually more powerful since it
allows the execution of multiple statements and annotations.

**Programmer's note:** Functions are first-class objects.  A ""def""
statement executed inside a function definition defines a local
function that can be returned or passed around.  Free variables used
in the nested function can access the local variables of the function
containing the def.  See section Naming and binding for details.

See also:

  **PEP 3107** - Function Annotations
     The original specification for function annotations.

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> import os
>>> os.system('cls')
0
>>> 
