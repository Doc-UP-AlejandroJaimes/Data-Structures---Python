# PEP 8
![pep8-guide-real-python](https://realpython.com/cdn-cgi/image/width=960,format=auto/https://files.realpython.com/media/PEP-8-Tutorial-Python-Code-Formatting-Guide_Watermarked.9103cf7be328.jpg)
> based on [How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/#:~:text=PEP%208%2C%20sometimes%20spelled%20PEP8,and%20consistency%20of%20Python%20code.) from Real Python.

## Index
1. What is PEP8?
2. Naming conventions
3. Code layout
4. Indentation
5. Comments
6. Whitespaces in Expressions and Statements.
7. Progamming recomendations.
8. When to Ignore PEP-8.
9. Tips and Tricks to help ensure your code follows PEP8.

###  What is PEP8?
PEP 8, sometimes spelled PEP8 or PEP-8, is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Alyssa Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.

In python philosofy, exist a humorous poem called [`Zen of python`](https://realpython.com/zen-of-python/#:~:text=The%20Zen%20of%20Python%20consists,Simple%20is%20better%20than%20complex.) this poem is composed by 19 aphorisms. Their main propouse of this, is listing of python principles and philosophies that are helpul in understanding and using the lenguage.

> To see it, just typing “import this” at the interactive prompt. 
```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
considering the above, the `PEP-8` was written following the zen of python aphorisms.

###  Naming conventions
> “Explicit is better than implicit.”
>
>  -- The Zen of Python

#### Tips
 + Choosing sensible names will save you time and energy later.
 + Never use the characters ‘l’ (lowercase letter el), ‘O’ (uppercase letter oh), or ‘I’ (uppercase letter eye) as single character variable names.
#### Naming Styles

|Type|Naming Convention|Examples|
|--|--|--|
|Function	|Use a lowercase word or words. Separate words by underscores to improve readability.	|function, python_function
|Variable	|Use a lowercase single letter, word, or words. Separate words with underscores to improve readability.	|x, var, python_variable
|Class	|Start each word with a capital letter. Don’t separate words with underscores. This style is called camel case or Pascal case.	|Model, PythonClass
|Method	|Use a lowercase word or words. Separate words with underscores to improve readability.	|class_method, method
|Constant	|Use an uppercase single letter, word, or words. Separate words with underscores to improve readability.	|CONSTANT, PYTHON_CONSTANT, PYTHON_LONG_CONSTANT
|Module	|Use a short, lowercase word or words. Separate words with underscores to improve readability.	module.py, python_module.py
|Package	|Use a short, lowercase word or words. Don’t separate words with underscores.	|package, pythonpackage

_Example in `naming_conventions.py` module:<br>Line: 6 - 61._

#### How to Choose Names

The best way to name your objects in Python is to use descriptive names to make it clear what the object represents.

_Example in `naming_conventions.py` module:<br>Line: 78 - 86._

###  Code layout
> “Beautiful is better than ugly.”
>
>  -- The Zen of Python
How you lay out your code has a huge role in how readable it is.
#### Blank Lines
- Top-level functions and classes should be fairly self-contained and handle separate functionality
-  PEP 8 suggests surrounding top-level functions and class definitions with two blank lines. _Example in `code_layout.py` Line: 09 - 30._
- Surround method definitions inside classes with a single blank line. _Example in `code_layout.py` Line: 32 - 63._
- Use blank lines sparingly inside functions to show clear steps.  _Example in `code_layout.py` Line: 65 - 89._
    - Sometimes, a complicated function has to complete several steps before the return statement. To help the reader understand the logic inside the function, you can leave a blank line between each logical step.