# PEP 8
![pep8-guide-real-python](https://realpython.com/cdn-cgi/image/width=960,format=auto/https://files.realpython.com/media/PEP-8-Tutorial-Python-Code-Formatting-Guide_Watermarked.9103cf7be328.jpg)
> based on [How to Write Beautiful Python Code With PEP 8](https://realpython.com/python-pep8/#:~:text=PEP%208%2C%20sometimes%20spelled%20PEP8,and%20consistency%20of%20Python%20code.) from Real Python.

## Index
1. [What is PEP8?](#whatispep8)
2. [Naming conventions](#namingconventions)
3. [Code layout](#codelayout)
4. [Indentation](#indentation)
5. [Comments](#comments)
6. [Whitespaces in Expressions and Statements.](#whitespaces)
7. [Progamming recomendations.](#programmingreco)
8. [When to Ignore PEP-8.](#whenignorepep8)
9. [Tips and Tricks to help ensure your code follows PEP8.](#tipspep8)

###  1. What is PEP8? <a name="whatispep8"></a>
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

###  2. Naming conventions <a name="namingconventions"></a>
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

###  3. Code layout <a name="codelayout"></a>
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

#### Maximum Line Length and Line Breaking
- PEP 8 suggests lines should be limited to 79 characters. _Example in `code_layout.py` Line: 93 - 100._
- If it’s impossible to use implied continuation, then you can use backslashes (\) to break lines instead.  _Example in `code_layout.py` Line: 102 - 108._
- If you need to break a line around binary operators, like + and *, then you should do so before the operator. This rule stems from mathematics.  _Example in `code_layout.py` Line: 110 - 122._

###  4. Indentation <a name="indentation"></a>
> “There should be one—and preferably only one—obvious way to do it.”
>
>  -- The Zen of Python

The indentation level of lines of code in Python determines how Python groups statements together.
- The key indentation rules laid out by PEP 8 are the following:
    - Use four consecutive spaces to indicate indentation.
    - Prefer spaces over tabs.
- In visual studio code, you can download and install the extension [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent)

#### Indentation Following Line Breaks

- There are two styles of indentation you can use:
    - Alignment with the opening delimiter
    ```python
    def function(arg_one, arg_two,
             arg_three, arg_four):
    return arg_one
    ```
    - Hanging indent
    ```python
    def function(
        arg_one, arg_two,
        arg_three, arg_four):
    return arg_one
    ```
#### Where to Put the Closing Bracket

- PEP 8 provides two options for the position of the closing bracket in implied line continuations:
    - Line up the closing bracket with the first non-whitespace character of the previous line:
    ```python
    list_of_numbers = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9
        ]
    ```
    - Line up the closing bracket with the first character of the line that starts the construct:
    ```python
    list_of_numbers = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9
    ]
    ```
###  5. Comments <a name="comments"></a>
> “If the implementation is hard to explain, it’s a bad idea.”
>
>  -- The Zen of Python

When you or someone else reads a comment, they should be able to easily understand the code that the comment applies to and know how it fits in with the rest of your code.
- Here are some key points to remember when adding comments to your code:
    - Limit the line length of comments and docstrings to 72 characters.
    - Use complete sentences, starting with a capital letter.
    - Make sure to update comments if you change your code.
#### Block comments
Use block comments to document a small section of code. 
- PEP 8 provides the following rules for writing block comments:

    - Indent block comments to the same level as the code that they describe.  _Example in `comments.py` Line: 09 - 29._
    - Start each line with a # followed by a single space.
    - Separate paragraphs by a line containing a single #.
    - if the code is very technical, then it’s necessary to use more than one paragraph in a block comment _Example in `comments.py` Line: 31 - 44._
#### Inline comment
Inline comments explain a single statement in a piece of code.
- Here’s what PEP 8 has to say about them:
    - Use inline comments sparingly. _Example in `comments.py` Line: 45 - 49._
    - Write inline comments on the same line as the statement they refer to.
    - Separate inline comments from the statement by two or more spaces.
    - Start inline comments with a # and a single space, like block comments.
    - Don’t use them to explain the obvious.

    **NOTE:** You should write your code so that it’s self-explanatory whenever possible, and reserve comments for situations where additional explanation is necessary. For example, you might need comments to explain why you wrote your code in a certain way.'
#### Documentation Strings
- You use docstrings to explain and document a specific block of code. _Example in `comments.py` Line: 51 - 79._
- You can access the docstring of an object using its .__doc__ attribute or the help() function.

###  6. Whitespace in Expressions and Statements <a name="whitespaces"></a>
> “Sparse is better than dense.”
>
>  -- The Zen of Python

Whitespace can be very helpful in expressions and statements—when you use it properly.
#### Whitespace Around Binary Operators

- For best readability according to PEP 8, surround the following binary operators with a single space on either side _Example in `whitespace.py` Line: 09 - 18._:

    - **Assignment operators:** =, +=, -=, and so forth

    - **Comparisons:** ==, !=, >, <. >=, <=, is, is not, in, and not in

    - **Booleans:** and, not, and or

- Avoiding whitespace for indicating default values for arguments keeps function and method definitions more concise _Example in `whitespace.py` Line: 20 - 51._
- PEP 8 also outlines some other cases where you should avoid whitespace:
    - Immediately inside parentheses, brackets, or braces:
    ```python
    # ✅ Recommended
    numbers = [1, 2, 3]

    # ❌ Not recommended
    numbers = [ 1, 2, 3, ]
    ```
    - Before a comma, semicolon, or colon:
    ```python
    x = 5
    y = 6

    # ✅ Recommended
    print(x, y)

    # ❌ Not recommended
    print(x , y)
    ```
    - Before the opening parenthesis that starts the argument list of a function call:
    ```python
    def double(x):
        return x * 2

    # ✅ Recommended
    double(3)

    # ❌ Not recommended
    double (3)
    ```
    - Before the open bracket that starts an index or slice:
    ```python
    # ✅ Recommended
    a_list[3]

    # ❌ Not recommended
    a_list [3]
    ```
    - Between a trailing comma and a closing parenthesis:
    ```python
    # ✅ Recommended
    a_tuple = (1,)

    # ❌ Not recommended
    a_tuple = (1, )
    ```
    - To align assignment operators:
    ```python
    # ✅ Recommended
    var1 = 5
    var2 = 6
    some_long_var = 7

    # ❌ Not recommended
    var1          = 5
    var2          = 6
    some_long_var = 7
    ```
###  7. Programming Recommendations <a name="programmingreco"></a>
> “Simple is better than complex.”
>
>  -- The Zen of Python

Suggestions that PEP 8 provides to remove that ambiguity and preserve consistency:
- Don’t compare Boolean values to True or False using the equivalence operator. _Example in `programming_recommendations.py` Line: 10 - 20._
- Use the fact that empty sequences are falsy in if statements. _Example in `programming_recommendations.py` Line: 22 - 32._
- Use is not rather than not ... is in if statements. _Example in `programming_recommendations.py` Line: 34 - 44._
- Don’t use if x: when you mean if x is not None _Example in `programming_recommendations.py` Line: 46 - 56._
- Use .startswith() and .endswith() instead of slicing. _Example in `programming_recommendations.py` Line: 58 - 74._

###  8. When to Ignore PEP 8  <a name="whenignorepep8"></a>
The short answer to this question **is never**. If you follow PEP 8 to the letter, you can _guarantee_ that you’ll have clean, professional, and readable code. This will benefit you as well as collaborators and potential employers.

However, some guidelines in PEP 8 are inconvenient in the following instances:
    - If complying with PEP 8 would break compatibility with existing software
    - If code surrounding what you’re working on is inconsistent with PEP 8
    - If code needs to remain compatible with older versions of Python

###  9. Tips and Tricks to Help Ensure Your Code Follows PEP 8 <a name="tipspep8"></a>
There’s a lot to remember to make sure your code follows the style guide for Python code. It can be a tall order to remember all these rules when you’re developing code. It’s particularly time-consuming to update past projects to be PEP 8 compliant. Luckily, there are tools that can help speed up this process. There are two classes of tools that can help you enforce these style rules: _linters_ and _autoformatters_.
#### Linters
Linters are programs that analyze code and flag errors. They provide suggestions on how to fix each error. Linters are particularly useful when installed as extensions to your text editor, as they flag errors and stylistic problems while you write your code.

Some good linters for Python code are **pycodestyle**, **flake8**, and **ruff**. Example:
-  Try them out with the following code snippet that contains formatting that isn’t compliant with PEP 8:
    ```python
    import math

    numbers = [1,2,\ 
    3,4]

    def add_all_numbers_from_collection(
        number_one, number_two, number_three,
        number_four):
        return number_one+number_two + number_three +number_four

    print (add_all_numbers_from_collection( *numbers ))
    ```
    - Analyze this with **pycodestyle**:
        - Install __pycodestyle__ using _pip_:
            ```shell
            $ python -m pip install pycodestyle
            ```
        - Run _pycodestyle_ from the terminal, passing it the Python file that you want to check as an argument:
            ```shell
            PS C:\Users\***\Data-Structures-Python\content\Section00_PEP-8> pycodestyle unfashionable.py
            unfashionable.py:3:13: E231 missing whitespace after ','
            unfashionable.py:3:15: E231 missing whitespace after ','
            unfashionable.py:3:16: E502 the backslash is redundant between brackets
            unfashionable.py:4:5: E128 continuation line under-indented for visual indent
            unfashionable.py:4:6: E231 missing whitespace after ','
            unfashionable.py:6:1: E302 expected 2 blank lines, found 1
            unfashionable.py:8:5: E125 continuation line with same indent as next logical line
            unfashionable.py:9:50: E225 missing whitespace around operator
            unfashionable.py:11:1: E305 expected 2 blank lines after class or function definition, found 1
            unfashionable.py:11:6: E211 whitespace before '('
            unfashionable.py:11:40: E201 whitespace after '('
            unfashionable.py:11:49: E202 whitespace before ')'
            unfashionable.py:11:52: W292 no newline at end of file
            ```
#### Autoformatters
Autoformatters are programs that refactor your code to conform with PEP 8 automatically.
Once such program is **black**, which autoformats code following most of the rules in PEP 8. One big difference is that it limits line length to **88 characters**, rather than **79**
```shell
PS C:\Users\***\Data-Structures-Python\content\Section00_PEP-8> black --line-length=79 .\autoformatter_example.py
reformatted autoformatter_example.py

All done! ✨ 🍰 ✨
1 file reformatted.
```
#### Combined Tooling
[Ruff](https://realpython.com/python-pep8/#whitespace-in-expressions-and-statements:~:text=Ruff%20is%20a%20popular%20tool%20in%20the%20Python%20community%20that%20can%20act%20as%20both%20a%20linter%20and%20an%20autoformatter.%20It%E2%80%99s%20a%20command%2Dline%20tool%20that%E2%80%99s%20written%20in%20Rust%20and%20therefore%20manages%20to%20execute%20very%20fast.) is a popular tool in the Python community that can act as both a linter and an autoformatter. It’s a command-line tool that’s written in Rust and therefore manages to execute very fast.
 - Install _Ruff_ using pip
    ```shell
    pip install ruff
    ```
 - Use Ruff both for linting and for formatting your code: 
    ```shell
    PS C:\Users\***\Data-Structures-Python\content\Section00_PEP-8> ruff check .\autoformatter_example.py
    autoformatter_example.py:1:8: F401 [*] `math` imported but unused
    |
    1 | import math
    |        ^^^^ F401
    |
    = help: Remove unused import: `math`

    Found 1 error.
    [*] 1 fixable with the `--fix` option.
    ```
 - Use Ruff for fix and formatting your code: 
    ```shell
    PS C:\Users\***\Data-Structures-Python\content\Section00_PEP-8> ruff format .\autoformatter_example.py
    Found 1 error (1 fixed, 0 remaining).
    ```
