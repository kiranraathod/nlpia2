Python syntax and semantics - Wikipedia

[Jump to content](#bodyContent)

Main menu

Main menu

move to sidebar
hide

Navigation

* [Main page](/wiki/Main_Page "Visit the main page [z]")
* [Contents](/wiki/Wikipedia:Contents "Guides to browsing Wikipedia")
* [Current events](/wiki/Portal:Current_events "Articles related to current events")
* [Random article](/wiki/Special:Random "Visit a randomly selected article [x]")
* [About Wikipedia](/wiki/Wikipedia:About "Learn about Wikipedia and how it works")
* [Contact us](//en.wikipedia.org/wiki/Wikipedia:Contact_us "How to contact Wikipedia")

Contribute

* [Help](/wiki/Help:Contents "Guidance on how to use and edit Wikipedia")
* [Learn to edit](/wiki/Help:Introduction "Learn how to edit Wikipedia")
* [Community portal](/wiki/Wikipedia:Community_portal "The hub for editors")
* [Recent changes](/wiki/Special:RecentChanges "A list of recent changes to Wikipedia [r]")
* [Upload file](/wiki/Wikipedia:File_upload_wizard "Add images or other media for use on Wikipedia")
* [Special pages](/wiki/Special:SpecialPages "A list of all special pages [q]")

[![](/static/images/icons/enwiki-25.svg)

![Wikipedia](/static/images/mobile/copyright/wikipedia-wordmark-en-25.svg)
![The Free Encyclopedia](/static/images/mobile/copyright/wikipedia-tagline-en-25.svg)](/wiki/Main_Page)

[Search](/wiki/Special:Search "Search Wikipedia [f]")

Search

Appearance

* [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
* [Create account](/w/index.php?title=Special:CreateAccount&returnto=Python+syntax+and+semantics "You are encouraged to create an account and log in; however, it is not mandatory")
* [Log in](/w/index.php?title=Special:UserLogin&returnto=Python+syntax+and+semantics "You're encouraged to log in; however, it's not mandatory. [o]")

Personal tools

* [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
* [Create account](/w/index.php?title=Special:CreateAccount&returnto=Python+syntax+and+semantics "You are encouraged to create an account and log in; however, it is not mandatory")
* [Log in](/w/index.php?title=Special:UserLogin&returnto=Python+syntax+and+semantics "You're encouraged to log in; however, it's not mandatory. [o]")

Contents
--------

move to sidebar
hide

* [(Top)](#)
* [1
  Design philosophy](#Design_philosophy)
* [2
  Keywords](#Keywords)
* [3
  Function annotations](#Function_annotations)
* [4
  Modules and import statements](#Modules_and_import_statements)


  Toggle Modules and import statements subsection
  + [4.1
    Entry point](#Entry_point)
* [5
  Indentation](#Indentation)
* [6
  Data structures](#Data_structures)


  Toggle Data structures subsection
  + [6.1
    Base types](#Base_types)
  + [6.2
    Collection types](#Collection_types)
  + [6.3
    Object system](#Object_system)
* [7
  Literals](#Literals)


  Toggle Literals subsection
  + [7.1
    Strings](#Strings)
    - [7.1.1
      Normal string literals](#Normal_string_literals)
    - [7.1.2
      Multi-line string literals](#Multi-line_string_literals)
    - [7.1.3
      Raw strings](#Raw_strings)
    - [7.1.4
      Concatenation of adjacent string literals](#Concatenation_of_adjacent_string_literals)
    - [7.1.5
      Unicode](#Unicode)
  + [7.2
    Numbers](#Numbers)
  + [7.3
    Lists, tuples, sets, dictionaries](#Lists,_tuples,_sets,_dictionaries)
* [8
  Operators](#Operators)


  Toggle Operators subsection
  + [8.1
    Arithmetic](#Arithmetic)
  + [8.2
    Comparison operators](#Comparison_operators)
  + [8.3
    Logical operators](#Logical_operators)
  + [8.4
    Bitwise operators](#Bitwise_operators)
* [9
  Functional programming](#Functional_programming)


  Toggle Functional programming subsection
  + [9.1
    Comprehensions](#Comprehensions)
  + [9.2
    First-class functions](#First-class_functions)
  + [9.3
    Closures](#Closures)
  + [9.4
    Generators](#Generators)
  + [9.5
    Generator expressions](#Generator_expressions)
  + [9.6
    Dictionary and set comprehensions](#Dictionary_and_set_comprehensions)
* [10
  Objects](#Objects)


  Toggle Objects subsection
  + [10.1
    With statement](#With_statement)
  + [10.2
    Properties](#Properties)
  + [10.3
    Descriptors](#Descriptors)
  + [10.4
    Class and static methods](#Class_and_static_methods)
* [11
  Exceptions](#Exceptions)
* [12
  Comments and docstrings](#Comments_and_docstrings)
* [13
  Decorators](#Decorators)
* [14
  Easter eggs](#Easter_eggs)
* [15
  Notes](#Notes)
* [16
  References](#References)
* [17
  External links](#External_links)

Toggle the table of contents

Python syntax and semantics
===========================

5 languages

* [Español](https://es.wikipedia.org/wiki/Sintaxis_y_sem%C3%A1ntica_de_Python "Sintaxis y semántica de Python – Spanish")
* [فارسی](https://fa.wikipedia.org/wiki/%D9%82%D9%88%D8%A7%D8%B9%D8%AF_%D8%B2%D8%A8%D8%A7%D9%86_%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86 "قواعد زبان پایتون – Persian")
* [Português](https://pt.wikipedia.org/wiki/Sintaxe_e_sem%C3%A2ntica_de_Python "Sintaxe e semântica de Python – Portuguese")
* [Српски / srpski](https://sr.wikipedia.org/wiki/%D0%A1%D0%B8%D0%BD%D1%82%D0%B0%D0%BA%D1%81%D0%B0_%D0%B8_%D1%81%D0%B5%D0%BC%D0%B0%D0%BD%D1%82%D0%B8%D0%BA%D0%B0_%D0%9F%D0%B0%D1%98%D1%82%D0%BE%D0%BD%D0%B0 "Синтакса и семантика Пајтона – Serbian")
* [中文](https://zh.wikipedia.org/wiki/Python%E8%AA%9E%E6%B3%95%E5%8F%8A%E8%AA%9E%E7%BE%A9 "Python語法及語義 – Chinese")

[Edit links](https://www.wikidata.org/wiki/Special:EntityPage/Q6553861#sitelinks-wikipedia "Edit interlanguage links")

* [Article](/wiki/Python_syntax_and_semantics "View the content page [c]")
* [Talk](/wiki/Talk:Python_syntax_and_semantics "Discuss improvements to the content page [t]")

English

* [Read](/wiki/Python_syntax_and_semantics)
* [Edit](/w/index.php?title=Python_syntax_and_semantics&action=edit "Edit this page [e]")
* [View history](/w/index.php?title=Python_syntax_and_semantics&action=history "Past revisions of this page [h]")



Tools

Tools

move to sidebar
hide

Actions

* [Read](/wiki/Python_syntax_and_semantics)
* [Edit](/w/index.php?title=Python_syntax_and_semantics&action=edit "Edit this page [e]")
* [View history](/w/index.php?title=Python_syntax_and_semantics&action=history)

General

* [What links here](/wiki/Special:WhatLinksHere/Python_syntax_and_semantics "List of all English Wikipedia pages containing links to this page [j]")
* [Related changes](/wiki/Special:RecentChangesLinked/Python_syntax_and_semantics "Recent changes in pages linked from this page [k]")
* [Upload file](//en.wikipedia.org/wiki/Wikipedia:File_Upload_Wizard "Upload files [u]")
* [Permanent link](/w/index.php?title=Python_syntax_and_semantics&oldid=1350541549 "Permanent link to this revision of this page")
* [Page information](/w/index.php?title=Python_syntax_and_semantics&action=info "More information about this page")
* [Cite this page](/w/index.php?title=Special:CiteThisPage&page=Python_syntax_and_semantics&id=1350541549&wpFormIdentifier=titleform "Information on how to cite this page")
* [Get shortened URL](/w/index.php?title=Special:UrlShortener&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FPython_syntax_and_semantics)

Print/export

* [Download as PDF](/w/index.php?title=Special:DownloadAsPdf&page=Python_syntax_and_semantics&action=show-download-screen "Download this page as a PDF file")
* [Printable version](/w/index.php?title=Python_syntax_and_semantics&printable=yes "Printable version of this page [p]")

In other projects

* [Wikibooks](https://en.wikibooks.org/wiki/Python_Programming/Basic_Syntax)
* [Wikidata item](https://www.wikidata.org/wiki/Special:EntityPage/Q6553861 "Structured data on this page hosted by Wikidata [g]")

Appearance

move to sidebar
hide

From Wikipedia, the free encyclopedia

Set of rules defining correctly structured programs

[![](//upload.wikimedia.org/wikipedia/commons/thumb/6/62/CPT-TheoryOfComp-Binary-Search-Python.png/250px-CPT-TheoryOfComp-Binary-Search-Python.png)](/wiki/File:CPT-TheoryOfComp-Binary-Search-Python.png)

A snippet of Python code demonstrating binary search

The [syntax](/wiki/Syntax_(programming_languages) "Syntax (programming languages)") of the [Python programming language](/wiki/Python_(programming_language) "Python (programming language)") is the set of rules that defines how a Python program will be written and [interpreted](/wiki/Interpreter_(computing) "Interpreter (computing)") (by both the [runtime system](/wiki/Runtime_system "Runtime system") and by human readers). The Python language has many similarities to [Perl](/wiki/Perl "Perl"), [C](/wiki/C_(programming_language) "C (programming language)"), and [Java](/wiki/Java_(programming_language) "Java (programming language)"). However, there are some definite differences between the languages. It supports multiple [programming paradigms](/wiki/Programming_paradigm "Programming paradigm"), including structured, [object-oriented programming](/wiki/Object-oriented_programming "Object-oriented programming"), and [functional programming](/wiki/Functional_programming "Functional programming"), and boasts a dynamic [type system](/wiki/Type_system "Type system") and [automatic memory management](/wiki/Automatic_memory_management "Automatic memory management").

Python's syntax is simple and consistent, adhering to the principle that "There should be one-and preferably only one-obvious way to do it."[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*] The language incorporates built-in [data types](/wiki/Data_type "Data type") and structures, [control flow](/wiki/Control_flow "Control flow") mechanisms, [first-class functions](/wiki/First-class_function "First-class function"), and modules for better [code](/wiki/Code "Code") reusability and organization. Python also uses English keywords where other languages use punctuation, contributing to its uncluttered visual layout.

The language provides robust error handling through exceptions, and includes a [debugger](/wiki/Debugger "Debugger") in the standard library for efficient problem-solving. Python's syntax, designed for readability and ease of use, makes it a popular choice among beginners and professionals alike.

Design philosophy
-----------------

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=1 "Edit section: Design philosophy")]

Python was designed to be a highly [readable](/wiki/Readable_code "Readable code") language.[[1]](#cite_note-1) It has a relatively uncluttered visual layout and uses English keywords frequently where other languages [use punctuation](/wiki/Syntactic_sugar "Syntactic sugar"). Python aims to be simple and consistent in the design of its syntax, encapsulated in the mantra "There should be one— and preferably only one —obvious way to do it", from the [Zen of Python](/wiki/Zen_of_Python "Zen of Python").[[2]](#cite_note-PEP20-2)

This mantra is deliberately opposed to the [Perl](/wiki/Perl "Perl") and [Ruby](/wiki/Ruby_(programming_language) "Ruby (programming language)") mantra, "[there's more than one way to do it](/wiki/There%27s_more_than_one_way_to_do_it "There's more than one way to do it")".

Keywords
--------

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=2 "Edit section: Keywords")]

Python 3 has 35 [keywords](/wiki/Reserved_word "Reserved word") or *reserved words*; they cannot be used as [identifiers](/wiki/Identifier_(computer_languages) "Identifier (computer languages)").[[3]](#cite_note-3)[[4]](#cite_note-4)

* `and`
* `as`
* `assert`
* `async`[[note 1]](#cite_note-keywordIn35-6)
* `await`[[note 1]](#cite_note-keywordIn35-6)
* `break`
* `class`
* `continue`
* `def`
* `del`
* `elif`
* `else`
* `except`
* `False`[[note 2]](#cite_note-becameKeywordIn3-7)
* `finally`
* `for`
* `from`
* `global`
* `if`
* `import`
* `in`
* `is`
* `lambda`
* `None`
* `nonlocal`[[note 3]](#cite_note-keywordIn3-8)
* `not`
* `or`
* `pass`
* `raise`
* `return`
* `True`[[note 2]](#cite_note-becameKeywordIn3-7)
* `try`
* `while`
* `with`
* `yield`

In addition, Python 3 also has 4 *soft keywords*, including `type` added in Python 3.12. Unlike regular *hard keywords*, soft keywords are reserved words only in the limited contexts where interpreting them as keywords would make syntactic sense. These words can be used as identifiers elsewhere, in other words, *match* and *case* are valid names for functions and variables.[[6]](#cite_note-9)[[7]](#cite_note-pep-0622-10)

* `_`[[note 4]](#cite_note-keywordIn310-11)
* `case`[[note 4]](#cite_note-keywordIn310-11)
* `match`[[note 4]](#cite_note-keywordIn310-11)
* `type`

Function annotations
--------------------

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=3 "Edit section: Function annotations")]

Function annotations (type hints) are defined in PEP 3107.[[8]](#cite_note-pep3107-12) They allow attaching data to the arguments and return of a function. The act of annotations is not defined by the language, and is left to third party frameworks. For example, a library could be written to handle static typing:[[8]](#cite_note-pep3107-12)

```
def haul(item: Haulable, *vargs: PackAnimal) -> Distance:
    # implementation here
```

While annotations are optional in Python, the rest of this article will use annotations to provide clarity.

Modules and import statements
-----------------------------

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=4 "Edit section: Modules and import statements")]

In Python, code is organized into files called [modules](/wiki/Modular_programming "Modular programming"), and [namespaces](/wiki/Namespace "Namespace") are defined by the individual modules. Since modules can be contained in hierarchical packages, then namespaces are hierarchical too.[[9]](#cite_note-13)[[10]](#cite_note-14)
In general when a module is imported then the names defined in the module are defined via that module's namespace, and are accessed in from the calling modules by using the fully qualified name.

```
# assume ModuleA defines two functions : func1() and func2() and one class : Class1
import ModuleA

ModuleA.func1()
ModuleA.func2()
a: ModuleA.Class1 = Modulea.Class1()
```

The `from ... import ...` statement can be used to insert the relevant names directly into the calling module's namespace, and those names can be accessed from the calling module without the qualified name:

```
# assume ModuleA defines two functions : func1() and func2() and one class : Class1
from ModuleA import func1

func1()
func2() # this will fail as an undefined name, as will the full name ModuleA.func2()
a: Class1 = Class1() # this will fail as an undefined name, as will the full name ModuleA.Class1()
```

Since this directly imports names (without qualification) it can overwrite existing names with no warnings.

A special form of the statement is `from ... import *` which imports all names defined in the named package directly in the calling module's namespace. Use of this form of import, although supported within the language, is generally discouraged as it pollutes the namespace of the calling module and will cause already defined names to be overwritten in the case of name clashes.[[11]](#cite_note-15) However, this page will present code as if the line "`from typing import *`" were included, for referring to collection types.

The different import statements are demonstrated here:

```
# imports the argument parsing module
import argparse
# imports the Pattern class from the regular expressions module
from re import Pattern
# imports all symbols inside the typing module
from typing import *
```

Using `from import` statements in Python can simplify verbose namespaces, such as nested namespaces.

```
from selenium.webdriver import Firefox
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

if __name__ == "__main__":
    driver: Firefox = Firefox()
    element: WebElement = driver.find_element(By.ID, "myInputField")
    element.send_keys(f"Hello World{Keys.ENTER}")
    action: ActionChains = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
```

Python also supports `import x as y` as a way of providing an alias or alternative name for use by the calling module:

```
import numpy as np
from numpy.typing import NDArray, float32

a: NDArray[float32] = np.arange(1000)
```

When a module is imported, the Python interpreter first checks if it exists in the `sys.modules` cache, and reuses it if it had been imported previously, otherwise it loads it. When loading, it searches it in `sys.path`, and compiles it to bytecode or interprets its contents. All code in the global scope of the module is executed. However, this can be mitigated using an explicit main function, which behaves similarly to an [entry point](/wiki/Entry_point "Entry point") in most compiled languages, using the entry point idiom described as follows.

### Entry point

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=5 "Edit section: Entry point")]

A pseudo-entry point can be created by the following idiom, which relies on the internal variable `__name__` being set to `__main__` when a program is executed, but not when it is imported as a module (in which case it is instead set to the module name); there are many variants of this structure:[[12]](#cite_note-16)[[13]](#cite_note-17)[[14]](#cite_note-18)

```
import sys

def main(argv: list[str]) -> int:
    argc: int = len(argv)  # get length of argv
    n: int = int(argv[1])
    print(n + 1)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

In this idiom, the call to the named entry point `main` is explicit, and the interaction with the [operating system](/wiki/Operating_system "Operating system") (receiving the arguments, calling system exit) are done explicitly by library calls, which are ultimately handled by the Python runtime. This contrasts with C, where these are done *implicitly* by the runtime, based on convention.

Indentation
-----------

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=6 "Edit section: Indentation")]

Python uses [whitespace](/wiki/Whitespace_character "Whitespace character") to delimit [control flow](/wiki/Control_flow "Control flow") blocks (following the [off-side rule](/wiki/Off-side_rule "Off-side rule")). Python borrows this feature from its predecessor [ABC](/wiki/ABC_(programming_language) "ABC (programming language)"): instead of punctuation or keywords, it uses indentation to indicate the run of a [block](/wiki/Block_(programming) "Block (programming)").

In so-called "free-format" languages – that use the block structure derived from [ALGOL](/wiki/ALGOL "ALGOL") – blocks of code are set off with braces (`{ }`) or keywords. In most [coding conventions](/wiki/Coding_conventions "Coding conventions") for these languages, programmers [conventionally indent the code](/wiki/Prettyprint#Programming_code_formatting "Prettyprint") within a block, to visually set it apart from the surrounding code.

A [recursive](/wiki/Recursion_(computer_science) "Recursion (computer science)") [function](/wiki/Function_(computer_science) "Function (computer science)") named `foo`, which is passed a single [parameter](/wiki/Parameter_(computer_programming) "Parameter (computer programming)"), `x`, and if the parameter is 0 will call a different function named `bar` and otherwise will call `baz`, passing `x`, and also call itself recursively, passing `x-1` as the parameter, could be implemented like this in Python:

```
def foo(x: int) -> None:
    if x == 0:
        bar()
    else:
        baz(x)
        foo(x - 1)
```

and could be written like this in [C](/wiki/C_(programming_language) "C (programming language)"):

```
void foo(int x) {
    if (x == 0) {
        bar();
    } else {
        baz(x);
        foo(x - 1);
    }
}
```

Incorrectly indented code could be misread by a human reader differently than it would be interpreted by a [compiler](/wiki/Compiler "Compiler") or interpreter. For example, if the function call `foo(x - 1)` on the last line in the example above was erroneously indented to be outside the `if`/`else` block:

```
def foo(x: int) -> None:
    if x == 0:
        bar()
    else:
        baz(x)
    foo(x - 1)
```

it would cause the last line to always be executed, even when `x` is 0, resulting in an [endless recursion](/wiki/Infinite_loop#Infinite_recursion "Infinite loop").

While both [space](/wiki/Space_(punctuation) "Space (punctuation)") and [tab](/wiki/Tab_key "Tab key") characters are accepted as forms of indentation and any multiple of spaces can be used, spaces are recommended[[15]](#cite_note-19) and four spaces (as in the above examples) are recommended and are by far the most commonly used.[[16]](#cite_note-20)[[17]](#cite_note-21)[*[unreliable source?](/wiki/Wikipedia:Reliable_sources "Wikipedia:Reliable sources")*] Mixing spaces and tabs on consecutive lines is not allowed starting with Python 3[[18]](#cite_note-22) because that can create bugs which are difficult to see, since many text editors do not visually distinguish spaces and tabs.

Data structures
---------------

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=7 "Edit section: Data structures")]

See also: [Python (programming language) § Typing](/wiki/Python_(programming_language)#Typing "Python (programming language)")

Since Python is a [dynamically-typed](/wiki/Dynamically-typed "Dynamically-typed") language, Python *values,* not variables, carry [type](/wiki/Data_type "Data type") information. All [variables](/wiki/Variable_(computer_science) "Variable (computer science)") in Python hold [references](/wiki/Reference_(computer_science) "Reference (computer science)") to [objects](/wiki/Object-oriented_programming "Object-oriented programming"), and these references are passed to functions. Some people (including Python creator [Guido van Rossum](/wiki/Guido_van_Rossum "Guido van Rossum") himself) have called this parameter-passing scheme "call by object reference". An object reference means a name, and the passed reference is an "alias", i.e. a copy of the reference to the same object, just as in C/[C++](/wiki/C%2B%2B "C++"). The object's value may be changed in the called function with the "alias", for example:

```
my_list: list[str] = ["a", "b", "c"]
def my_func(l: list[str]) -> None:
    l.append("x")
    print(l)

print(my_func(my_list))
# prints ['a', 'b', 'c', 'x']
print(my_list)
# prints ['a', 'b', 'c', 'x']
```

Function `my_func` changes the value of `my_list` with the formal argument `l`, which is an alias of `my_list`. However, any attempt to operate (assign a new object reference to) on the alias itself will have no effect on the original object.[*[clarification needed](/wiki/Wikipedia:Please_clarify "Wikipedia:Please clarify")*]

```
my_list: list[str] = ["a", "b", "c"]

def my_func(l: list[str]) -> None:
    # l.append("x")
    l = l + ["x"]  # a new list created and assigned to l means l is no more alias for my_list
    print(l)

print(my_func(my_list))
# prints ['a', 'b', 'c', 'x']
print(my_list)
# prints ['a', 'b', 'c']
```

In Python, non-innermost-local and not-declared-global accessible names are all aliases.

Among dynamically-typed languages, Python is moderately type-checked. Implicit [conversion](/wiki/Type_conversion "Type conversion") is defined for [numeric types](/wiki/Numeric_(data_type) "Numeric (data type)") (as well as [Booleans](/wiki/Boolean_data_type "Boolean data type")), so one may validly multiply a [complex number](/wiki/Complex_number "Complex number") by an [integer](/wiki/Integer_(computer_science) "Integer (computer science)") (for instance) without explicit [casting](/wiki/Type_conversion "Type conversion"). However, there is no implicit conversion between, for example, numbers and [strings](/wiki/String_(computer_science) "String (computer science)"); a string is an invalid argument to a mathematical function expecting a number.

### Base types

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=8 "Edit section: Base types")]

Python has a broad range of basic data types. Alongside conventional integer and [floating-point](/wiki/Floating-point "Floating-point") arithmetic, it transparently supports [arbitrary-precision arithmetic](/wiki/Arbitrary-precision_arithmetic "Arbitrary-precision arithmetic"), [complex numbers](/wiki/Complex_number "Complex number"), and [decimal numbers](/wiki/Decimal_data_type "Decimal data type").

Python supports a wide variety of string operations. Strings in Python are [immutable](/wiki/Immutable_object "Immutable object"), meaning that string operations, such as replacement of [characters](/wiki/Character_(computing) "Character (computing)"), return a new string; in other programming languages the string might be altered [in place](/wiki/In-place_algorithm "In-place algorithm"). Performance considerations sometimes push for using special techniques in programs that modify strings intensively, such as joining character arrays into strings only as needed.

### Collection types

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=9 "Edit section: Collection types")]

One of the very useful aspects of Python is the concept of [*collection*](/wiki/Collection_(abstract_data_type) "Collection (abstract data type)") (or *container*) types. In general a collection is an object that contains other objects in a way that is easily referenced or *indexed*. Collections come in two basic forms: *sequences* and *mappings*.

The ordered sequential types are lists (dynamic [arrays](/wiki/Array_data_type "Array data type")), [tuples](/wiki/Tuple "Tuple"), and strings. All sequences are indexed positionally ([0 through *length* - 1](/wiki/Zero-based_numbering "Zero-based numbering")) and all but strings can contain any type of object, including multiple types in the same sequence. Both strings and tuples are immutable, making them perfect candidates for dictionary keys (see below). Lists, on the other hand, are mutable; elements can be inserted, deleted, modified, appended, or sorted [in-place](/wiki/In-place_algorithm "In-place algorithm").

[Mappings](/wiki/Associative_array "Associative array"), on the other hand, are (often unordered) types implemented in the form of *dictionaries* which "map" a set of immutable keys to corresponding elements (much like a mathematical function). For example, one could define a dictionary having a string `"toast"` mapped to the integer `42` or vice versa. The keys in a dictionary must be of an immutable Python type, such as an integer or a string, because they are implemented via a [hash function](/wiki/Hash_function "Hash function"). This makes for much faster lookup times, but requires keys to remain unchanged.

Dictionaries are central to the internals of Python as they reside at the core of all objects and classes: the mappings between variable names (strings) and the values which the names reference are stored as dictionaries (see [Object system](#Object_system)). Since these dictionaries are directly accessible (via an object's `__dict__` attribute), [metaprogramming](/wiki/Metaprogramming "Metaprogramming") is a straightforward and natural process in Python.

A [set](/wiki/Set_(computer_science) "Set (computer science)") collection type is an unindexed, unordered collection that contains no duplicates, and implements [set theoretic](/wiki/Naive_set_theory "Naive set theory") operations such as [union](/wiki/Union_(set_theory) "Union (set theory)"), [intersection](/wiki/Intersection_(set_theory) "Intersection (set theory)"), [difference](/wiki/Relative_complement "Relative complement"), [symmetric difference](/wiki/Symmetric_difference "Symmetric difference"), and [subset](/wiki/Subset "Subset") testing. There are two types of sets: `set` and `frozenset`, the only difference being that `set` is mutable and `frozenset` is immutable. Elements in a set must be hashable. Thus, for example, a `frozenset` can be an element of a regular `set` whereas the opposite is not true.

Python also provides extensive collection manipulating abilities such as built in containment checking and a generic iteration protocol.

### Object system

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=10 "Edit section: Object system")]

In Python, everything is an object, even classes. Classes, as objects, have a class, which is known as their [metaclass](/wiki/Metaclass "Metaclass"). Python also supports [multiple inheritance](/wiki/Multiple_inheritance "Multiple inheritance") and [mixins](/wiki/Mixin "Mixin").

The language supports extensive [introspection](/wiki/Introspection_(computer_science) "Introspection (computer science)") of types and classes. Types can be read and compared: Types are instances of the object `type`. The attributes of an object can be extracted as a dictionary.

Operators can be [overloaded](/wiki/Operator_overloading "Operator overloading") in Python by defining special member functions – for instance, defining a method named `__add__` on a class permits one to use the `+` operator on objects of that class.

Literals
--------

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=11 "Edit section: Literals")]

### Strings

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=12 "Edit section: Strings")]

Python has various kinds of [string literals](/wiki/String_literal "String literal").

#### Normal string literals

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=13 "Edit section: Normal string literals")]

Either single or double quotes can be used to quote strings. Unlike in Unix shell languages, [Perl](/wiki/Perl "Perl") or Perl-influenced languages such as [Ruby](/wiki/Ruby_(programming_language) "Ruby (programming language)") or [Groovy](/wiki/Groovy_(programming_language) "Groovy (programming language)"), single quotes and double quotes function identically, i.e. there is no string interpolation of *$foo* expressions. However, interpolation can be done in various ways: with "f-strings" (since Python 3.6[[19]](#cite_note-23)), using the `format` method or the old *%* string-format operator.

For instance, all of these Python statements:

```
print(f"I just printed {num} pages to the printer {printer}")

print("I just printed {} pages to the printer {}".format(num, printer))
print("I just printed {0} pages to the printer {1}".format(num, printer))
print("I just printed {a} pages to the printer {b}".format(a=num, b=printer))

print("I just printed %s pages to the printer %s" % (num, printer))
print("I just printed %(a)s pages to the printer %(b)s" % {"a": num, "b": printer})
```

are equivalent to the Perl statement:

```
print "I just printed $num pages to the printer $printer\n"
```

They build a string using the variables `num` and `printer`.

#### Multi-line string literals

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=14 "Edit section: Multi-line string literals")]

There are also multi-line strings, which begin and end with a series of three single or double quotes and function like [here documents](/wiki/Here_document "Here document") in [Perl](/wiki/Perl "Perl") and [Ruby](/wiki/Ruby_(programming_language) "Ruby (programming language)").

A simple example with [variable interpolation](/wiki/String_interpolation "String interpolation") (using the `format` method) is:

```
print('''Dear {recipient},

I wish you to leave Sunnydale and never return.

Not Quite Love,
{sender}
'''.format(sender="Buffy the Vampire Slayer", recipient="Spike"))
```

#### Raw strings

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=15 "Edit section: Raw strings")]

Finally, all of the previously mentioned string types come in "[raw](/wiki/Raw_string "Raw string")" varieties (denoted by placing a literal *r* before the opening quote), which do no backslash-interpolation and hence are very useful for [regular expressions](/wiki/Regular_expression "Regular expression"); compare ["@-quoting"](/wiki/C_Sharp_syntax#Literals "C Sharp syntax") in [C#](/wiki/C_Sharp_(programming_language) "C Sharp (programming language)"). Raw strings were originally included specifically for regular expressions. Due to limitations of the [tokenizer](/wiki/Tokenizer "Tokenizer"), raw strings may not have a trailing [backslash](/wiki/Backslash "Backslash").[[20]](#cite_note-24) Creating a raw string holding a [Windows](/wiki/Windows "Windows") path ending with a backslash requires some variety of workaround (commonly, using forward slashes instead of backslashes, since Windows accepts both).

Examples include:

```
# A Windows path, even raw strings cannot end in a backslash
win_path: str = r"C:\Foo\Bar\Baz\"

# Error:
#  File "<stdin>", line 1
#    win_path: str = r"C:\Foo\Bar\Baz\"
#                                     ^
# SyntaxError: EOL while scanning string literal

dos_path: str = r"C:\Foo\Bar\Baz\ "  # avoids the error by adding
print(dos_path.rstrip()) # and removing trailing space
# prints('C:\\Foo\\Bar\\Baz\\')

quoted_dos_path: str = r'"{}"'.format(dos_path)
print(quoted_dos_path)
# prints '"C:\\Foo\\Bar\\Baz\\ "'

# A regular expression matching a quoted string with possible backslash quoting
print(re.match(r'"(([^"\\]|\\.)*)"', quoted_dos_path).group(1).rstrip())
# prints 'C:\\Foo\\Bar\\Baz\\'

code: str = 'foo(2, bar)'
# Reverse the arguments in a two-arg function call
print(re.sub(r'\(([^,]*?),([^ ,]*?)\)', r'(\2, \1)', code))
# prints 'foo(2, bar)'
# Note that this won't work if either argument has parens or commas in it.
```

#### Concatenation of adjacent string literals

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=16 "Edit section: Concatenation of adjacent string literals")]

String literals appearing contiguously and only separated by whitespace (including new lines using backslashes), are allowed and are aggregated into a single longer string.[[21]](#cite_note-25)
Thus

```
title: str = "One Good Turn: " \
             'A Natural History of the Screwdriver and the Screw'
```

is equivalent to

```
title: str = "One Good Turn: A Natural History of the Screwdriver and the Screw"
```

#### Unicode

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=17 "Edit section: Unicode")]

Since Python 3.0, the default character set is [UTF-8](/wiki/UTF-8 "UTF-8") both for source code and the interpreter. In UTF-8, unicode strings are handled like traditional byte strings. This example will work:

```
s: str = "Γειά"  # Hello in Greek
print(s)
```

### Numbers

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=18 "Edit section: Numbers")]

Numeric literals in Python are of the normal sort, e.g. `0`, `-1`, `3.4`, `3.5e-8`.

Python has arbitrary-length integers and automatically increases their storage size as necessary. Prior to Python 3, there were two kinds of integral numbers: traditional fixed size integers and "long" integers of arbitrary size. The conversion to "long" integers was performed automatically when required, and thus the programmer usually did not have to be aware of the two integral types. In newer language versions the distinction is completely gone and all integers behave like arbitrary-length integers.

Python supports normal [floating point](/wiki/IEEE_754-2008 "IEEE 754-2008") numbers, which are created when a dot is used in a literal (e.g. `1.1`), when an integer and a floating point number are used in an expression, or as a result of some mathematical operations ("true division" via the `/` operator, or exponentiation with a negative exponent).

Python also supports [complex numbers](/wiki/Complex_number "Complex number") natively. The [imaginary](/wiki/Imaginary_number "Imaginary number") component of a complex number is indicated with the `J` or `j` suffix, e.g. `3 + 4j`.

### Lists, tuples, sets, dictionaries

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=19 "Edit section: Lists, tuples, sets, dictionaries")]

Python has syntactic support for the creation of container types.

Lists (class `list`) are mutable sequences of items of arbitrary types, and can be created either with the special syntax

```
my_list: list[int | str] = [1, 2, 3, "a dog"]
```

or using normal object creation

```
my_second_list: list[int] = []
my_second_list.append(4)
my_second_list.append(5)
```

Tuples (class `tuple`) are immutable sequences of items of arbitrary types. There is also a special syntax to create tuples

```
my_tuple: tuple[int | str] = 1, 2, 3, "four"
my_tuple: tuple[int | str] = (1, 2, 3, "four")
```

Although tuples are created by separating items with commas, the whole construct is usually wrapped in parentheses to increase readability. An empty tuple is denoted by `()`, while a tuple with a single value can be created with `(1,)`.

Sets (class `set`) are mutable containers of hashable items[[22]](#cite_note-26) of arbitrary types, with no duplicates. The items are not ordered, but sets support iteration over the items. The syntax for set creation uses curly brackets

```
my_set: set[Any] = {0, (), False}
```

Python sets are very much like [mathematical sets](/wiki/Set_(mathematics) "Set (mathematics)"), and support operations like set [intersection](/wiki/Set_(mathematics)#Intersections "Set (mathematics)") and [union](/wiki/Set_(mathematics)#Unions "Set (mathematics)"). Python also features a `frozenset` class for immutable sets, see [Collection types](#Collection_types).

Dictionaries (class `dict`) are mutable mappings tying keys and corresponding values. Python has special syntax to create dictionaries (`{key: value}`)

```
my_dictionary: dict[Any, Any] = {"key 1": "value 1", 2: 3, 4: []}
```

The dictionary syntax is similar to the set syntax; the difference is the presence of colons. The empty literal `{}` results in an empty dictionary rather than an [empty set](/wiki/Empty_set "Empty set"), which is instead created using the non-literal constructor: `set()`.

Operators
---------

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=20 "Edit section: Operators")]

### Arithmetic

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=21 "Edit section: Arithmetic")]

Python includes the `+`, `-`, `*`, `/` ("true division"), `//` ([floor](/wiki/Floor_and_ceiling_functions "Floor and ceiling functions") division), `%` ([modulus](/wiki/Modulo_operator "Modulo operator")), and `**` ([exponentiation](/wiki/Exponentiation "Exponentiation")) operators, with their usual [mathematical precedence](/wiki/Order_of_operations "Order of operations").

In Python 3, `x / y` performs "true division", meaning that it always returns a float, even if both `x` and `y` are integers that divide evenly.

```
print(4 / 2)
# prints 2.0
```

and `//` performs [integer division](/wiki/Integer_division "Integer division") or *floor division*, returning the floor of the quotient as an integer.

In Python 2 (and most other programming languages), unless explicitly requested, `x / y` performed integer division, returning a float only if either input was a float. However, because Python is a dynamically-typed language, it was not always possible to tell which operation was being performed, which often led to subtle bugs, thus prompting the introduction of the `//` operator and the change in semantics of the `/` operator in Python 3.

### Comparison operators

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=22 "Edit section: Comparison operators")]

The comparison operators, i.e. `==`, `!=`, `<`, `>`, `<=`, `>=`, `is`, `is not`, `in` and `not in`[[23]](#cite_note-27) are used on all manner of values. Numbers, strings, sequences, and mappings can all be compared. In Python 3, disparate types (such as a `str` and an `int`) do not have a consistent relative ordering, and attempts to compare these types raises a `TypeError` exception. While it was possible to compare disparate types in Python 2 (for example, whether a string was greater-than or less-than an integer), the ordering was undefined; this was considered a historical design quirk and was ultimately removed in Python 3.

Chained comparison expressions such as `a < b < c` have roughly the meaning that they have in mathematics, rather than the unusual meaning found in [C](/wiki/C_(programming_language) "C (programming language)") and similar languages. The terms are evaluated and compared in order. The operation has [short-circuit semantics](/wiki/Short-circuit_evaluation "Short-circuit evaluation"), meaning that evaluation is guaranteed to stop as soon as a verdict is clear: if `a < b` is false, `c` is never evaluated as the expression cannot possibly be true anymore.

For expressions without side effects, `a < b < c` is equivalent to `a < b and b < c`. However, there is a substantial difference when the expressions have side effects. `a < f(x) < b` will evaluate `f(x)` exactly once, whereas `a < f(x) and f(x) < b` will evaluate it twice if the value of `a` is less than `f(x)` and once otherwise.

### Logical operators

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=23 "Edit section: Logical operators")]

In all versions of Python, Boolean operators treat zero values or empty values such as `""`, `0`, `None`, `0.0`, `[]`, and `{}` as false, while in general treating non-empty, non-zero values as true. The Boolean values `True` and `False` were added to the language in Python 2.2.1 as constants (subclassed from `1` and `0`) and were changed to be full blown keywords in Python 3. The binary comparison operators such as `==` and `>` return either `True` or `False`.

The Boolean operators `and` and `or` use [minimal evaluation](/wiki/Minimal_evaluation "Minimal evaluation"). For example, `y == 0 or x/y > 100` will never raise a divide-by-zero exception. These operators return the value of the last operand evaluated, rather than `True` or `False`. Thus the expression `(4 and 5)` evaluates to `5`, and `(4 or 5)` evaluates to `4`.

### Bitwise operators

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=24 "Edit section: Bitwise operators")]

Python is able to do [bitwise operations](/wiki/Bitwise_operation "Bitwise operation") on integers, or binary numbers written with the `0b` prefix. It uses `x << y` to shift `x` left by `y` places, adding zeros to the right. `x >> y` does the same but shifts `x` right, adding copies of the leftmost bit to the left. The operator `x & y` performs a bitwise AND, `x | y` does a bitwise OR, `~ x` returns the bitwise complement/NOT of `x`, and `x ^ y` does a bitwise XOR, contrary to the `^` symbol's usual use as an exponentiation operator.[[24]](#cite_note-28)[[25]](#cite_note-29)

Functional programming
----------------------

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=25 "Edit section: Functional programming")]

A strength of Python is the availability of a [functional programming](/wiki/Functional_programming "Functional programming") style, which makes working with lists and other collections much more straightforward.

### Comprehensions

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=26 "Edit section: Comprehensions")]

Main article: [List comprehension](/wiki/List_comprehension "List comprehension")

One such construction is the [list comprehension](/wiki/List_comprehension "List comprehension"), which can be expressed with the following format:

```
l: list[Any] = [mapping_expression for element in source_list if filter_expression]
```

Using list comprehension to calculate the first five powers of two:

```
powers_of_two: list[int] = [2 ** n for n in range(1, 6)]
```

The [Quicksort](/wiki/Quicksort "Quicksort") algorithm can be expressed elegantly (albeit inefficiently) using list comprehensions:

```
T: TypeVar = TypeVar("T")

def qsort(l: list[T]) -> list[T]:
    if l == []:
        return []
    pivot: T = l[0]
    return (qsort([x for x in l[1:] if x < pivot]) +
            [pivot] +
            qsort([x for x in l[1:] if x >= pivot]))
```

Python 2.7+[[26]](#cite_note-30) also supports set comprehensions[[27]](#cite_note-31) and dictionary comprehensions.[[28]](#cite_note-32)

### First-class functions

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=27 "Edit section: First-class functions")]

In Python, functions are [first-class](/wiki/First-class_function "First-class function") objects that can be created and passed around dynamically.

Python's limited support for [anonymous functions](/wiki/Anonymous_function "Anonymous function") is the `lambda` construct. An example is the anonymous function which squares its input, called with the argument of 5:

```
f: Callable[[int], int] = lambda x: x**2
f(5)
```

Lambdas are limited to containing an [expression](/wiki/Expression_(computer_science) "Expression (computer science)") rather than [statements](/wiki/Statement_(programming) "Statement (programming)"), although control flow can still be implemented less elegantly within lambda by using short-circuiting,[[29]](#cite_note-33) and more idiomatically with conditional expressions.[[30]](#cite_note-34)

### Closures

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=28 "Edit section: Closures")]

Python has had support for [lexical closures](/wiki/Closure_(computer_science) "Closure (computer science)") since version 2.2. Here's an example function that returns a function that [approximates the derivative](/wiki/Finite_difference "Finite difference") of the given function:

```
def derivative(f: Callable[[float], float], dx: float):
    """Return a function that approximates the derivative of f
    using an interval of dx, which should be appropriately small.
    """
    def function(x: float) -> float:
        return (f(x + dx) - f(x)) / dx
    return function
```

Python's syntax, though, sometimes leads programmers of other languages to think that closures are not supported. [Variable scope](/wiki/Scope_(computer_science) "Scope (computer science)") in Python is implicitly determined by the scope in which one assigns a value to the variable, unless scope is explicitly declared with `global` or `nonlocal`.[[31]](#cite_note-35)

Note that the closure's binding of a name to some value is not mutable from within the function. Given:

```
def foo(a: int, b: int) -> None:
    print(f"a: {a}")
    print(f"b: {b}")
    def bar(c: int) -> None:
        b = c
        print(f"b*: {b}")
    bar(a)
    print(f"b: {b}")

print(foo(1, 2))
# prints:
# a: 1
# b: 2
# b*: 1
# b: 2
```

and you can see that `b`, as visible from the closure's scope, retains the value it had; the changed binding of `b` inside the inner function did not propagate out. The way around this is to use a `nonlocal b` statement in `bar`. In Python 2 (which lacks `nonlocal`), the usual workaround is to use a mutable value and change that value, not the binding. E.g., a list with one element.

### Generators

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=29 "Edit section: Generators")]

Introduced in Python 2.2 as an optional feature and finalized in version 2.3, [generators](/wiki/Generator_(computer_science) "Generator (computer science)") are Python's mechanism for [lazy evaluation](/wiki/Lazy_evaluation "Lazy evaluation") of a function that would otherwise return a space-prohibitive or computationally intensive list.

This is an example to lazily generate the prime numbers:

```
import itertools

def generate_primes(stop_at: Optional[int] = None) -> Iterator[int]:
    primes: list[int] = []
    for n in itertools.count(start = 2):
        if stop_at is not None and n > stop_at:
            return # raises the StopIteration exception
        composite: bool = False
        for p in primes:
            if not n % p:
                composite = True
                break
            elif p ** 2 > n:
                break
        if not composite:
            primes.append(n)
            yield n
```

When calling this function, the returned value can be iterated over much like a list:

```
for i in generate_primes(100):  # iterate over the primes between 0 and 100
    print(i)

for i in generate_primes():  # iterate over ALL primes indefinitely
    print(i)
```

The definition of a generator appears identical to that of a function, except the keyword `yield` is used in place of `return`. However, a generator is an object with persistent state, which can repeatedly enter and leave the same scope. A generator call can then be used in place of a list, or other structure whose elements will be iterated over. Whenever the `for` loop in the example requires the next item, the generator is called, and yields the next item.

Generators do not have to be infinite like the prime-number example above. When a generator terminates, an internal exception is raised which indicates to any calling context that there are no more values. A `for` loop or other iteration will then terminate.

### Generator expressions

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=30 "Edit section: Generator expressions")]

Further information: [List comprehension](/wiki/List_comprehension "List comprehension")

Introduced in Python 2.4, generator expressions are the [lazy evaluation](/wiki/Lazy_evaluation "Lazy evaluation") equivalent of list comprehensions. Using the prime number generator provided in the above section, we might define a lazy, but not quite infinite collection.

```
import itertools

primes_under_million: Iterator[int] = (i for i in generate_primes() if i < 1000000)
two_thousandth_prime: Iterator[int] = itertools.islice(primes_under_million, 1999, 2000).next()
```

Most of the memory and time needed to generate this many primes will not be used until the needed element is actually accessed. Unfortunately, you cannot perform simple indexing and slicing of generators, but must use the *itertools* module or "roll your own" loops. In contrast, a list comprehension is functionally equivalent, but is *greedy* in performing all the work:

```
primes_under_million: list[int] = [i for i in generate_primes(2000000) if i < 1000000]
two_thousandth_prime: int = primes_under_million[1999]
```

The list comprehension will immediately create a large list (with 78498 items, in the example, but transiently creating a list of primes under two million), even if most elements are never accessed. The generator comprehension is more parsimonious.

### Dictionary and set comprehensions

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=31 "Edit section: Dictionary and set comprehensions")]

While lists and generators had comprehensions/expressions, in Python versions older than 2.7 the other Python built-in collection types (dicts and sets) had to be kludged in using lists or generators:

```
squares = dict((n, n * n) for n in range(5))
# in Python 3.5 and later the type of squares is dict[int, int]
print(squares)
# prints {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

Python 2.7 and 3.0 unified all collection types by introducing dictionary and set comprehensions, similar to list comprehensions:

```
print([n * n for n in range(5)])  # regular list comprehension
# prints [0, 1, 4, 9, 16]
print({n * n for n in range(5)})  # set comprehension
# prints {0, 1, 4, 9, 16}
print({n: n * n for n in range(5)})  # dict comprehension
# prints {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

Objects
-------

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=32 "Edit section: Objects")]

Python supports most object-oriented programming (OOP) techniques. It allows [polymorphism](/wiki/Polymorphism_(computer_science) "Polymorphism (computer science)"), not only within a [class hierarchy](/wiki/Class_hierarchy "Class hierarchy") but also by [duck typing](/wiki/Duck_typing "Duck typing"). Any object can be used for any type, and it will work so long as it has the proper methods and attributes. And everything in Python is an object, including classes, functions, numbers and modules. Python also has support for [metaclasses](/wiki/Metaclass "Metaclass"), an advanced tool for enhancing classes' functionality. Naturally, [inheritance](/wiki/Inheritance_(object-oriented_programming) "Inheritance (object-oriented programming)"), including [multiple inheritance](/wiki/Multiple_inheritance "Multiple inheritance"), is supported. Python has very limited support for private variables using [name mangling](/wiki/Name_mangling#Python "Name mangling") which is rarely used in practice as [information hiding](/wiki/Information_hiding "Information hiding") is seen by some as [unpythonic](/wiki/Python_(programming_language)#Design_philosophy_and_features "Python (programming language)"), in that it suggests that the class in question contains unaesthetic or ill-planned internals. The slogan "we're all responsible users here" is used to describe this attitude.[[32]](#cite_note-36)

> As is true for modules, classes in Python do not put an absolute barrier between definition and user, but rather rely on the politeness of the user not to "break into the definition."

— [9. Classes](https://docs.python.org/2.6/tutorial/classes.html), *The Python 2.6 Tutorial* (2013)

OOP doctrines such as the use of accessor methods to read data members are not enforced in Python. Just as Python offers functional-programming constructs but does not attempt to demand [referential transparency](/wiki/Referential_transparency "Referential transparency"), it offers an object system but does not demand OOP behavior. Moreover, it is always possible to redefine the class using *properties* (see [Properties](#Properties)) so that when a certain variable is set or retrieved in calling code, it really invokes a function call, so that `spam.eggs = toast` might really invoke `spam.set_eggs(toast)`. This nullifies the practical advantage of accessor functions, and it remains OOP because the property `eggs` becomes a legitimate part of the object's interface: it need not reflect an implementation detail.

In version 2.2 of Python, "new-style" classes were introduced. With new-style classes, objects and types were unified, allowing the subclassing of types.
Even entirely new types can be defined, complete with custom behavior for infix operators. This allows for many radical things to be done syntactically within Python. A new [method resolution order](https://www.python.org/download/releases/2.3/mro/) for multiple inheritance was also adopted with Python 2.3. It is also possible to run custom code while accessing or setting attributes, though the details of those techniques have evolved between Python versions.

### With statement

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=33 "Edit section: With statement")]

The `with` statement handles resources, and allows users to work with the Context Manager protocol.[[33]](#cite_note-37) One function (`__enter__()`) is called when entering scope and another (`__exit__()`) when leaving. This prevents forgetting to free the resource and also handles more complicated situations such as freeing the resource when an exception occurs while it is in use. Context Managers are often used with files, database connections, test cases, etc.

### Properties

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=34 "Edit section: Properties")]

Properties allow specially defined methods to be invoked on an object instance by using the same syntax as used for attribute access. An example of a class defining some properties is:

```
class MyClass:
    def __init__(self) -> None:
        self._a: int = 0

    @property
    def a(self) -> int:
        return self._a

    @a.setter  # makes the property writable
    def a(self, value: int) -> None:
        self._a = value
```

### Descriptors

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=35 "Edit section: Descriptors")]

A class that defines one or more of the three special methods `__get__(self, instance, owner)`, `__set__(self, instance, value)`, `__delete__(self, instance)` can be used as a descriptor. Creating an instance of a descriptor as a class member of a second class makes the instance a property of the second class.[[34]](#cite_note-38)

### Class and static methods

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=36 "Edit section: Class and static methods")]

Python allows the creation of class methods and static methods via the use of the `@classmethod` and `@staticmethod` [decorators](#Decorators). The first argument to a class method is the class object instead of the self-reference to the instance. A static method has no special first argument. Neither the instance, nor the class object is passed to a static method.

Exceptions
----------

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=37 "Edit section: Exceptions")]

Python supports (and extensively uses) [exception handling](/wiki/Exception_handling "Exception handling") as a means of testing for error conditions and other "exceptional" events in a program.

Python style calls for the use of exceptions whenever an error condition might arise. Rather than testing for access to a file or resource before actually using it, it is conventional in Python to just go ahead and try to use it, catching the exception if access is rejected.

Exceptions can also be used as a more general means of non-local transfer of control, even when an error is not at issue. For instance, the [Mailman](/wiki/GNU_Mailman "GNU Mailman") mailing list software, written in Python, uses exceptions to jump out of deeply nested message-handling logic when a decision has been made to reject a message or hold it for moderator approval.

Exceptions are often used as an alternative to the `if`-block, especially in [threaded](/wiki/Thread_(computer_science) "Thread (computer science)") situations. A commonly invoked motto is EAFP, or "It is Easier to Ask for Forgiveness than Permission,"[[35]](#cite_note-39) which is attributed to [Grace Hopper](/wiki/Grace_Hopper#Anecdotes "Grace Hopper").[[36]](#cite_note-40)[[37]](#cite_note-nutshell-41) The alternative, known as LBYL, or "Look Before You Leap", explicitly tests for pre-conditions.[[38]](#cite_note-42)

In this first code sample, following the LBYL approach, there is an explicit check for the attribute before access:

```
if hasattr(spam, "eggs"):
    ham = spam.eggs
else:
    handle_missing_attr()
```

This second sample follows the EAFP paradigm:

```
try:
    ham = spam.eggs
except AttributeError:
    handle_missing_attr()
```

These two code samples have the same effect, although there will be performance differences. When `spam` has the attribute `eggs`, the EAFP sample will run faster. When `spam` does not have the attribute `eggs` (the "exceptional" case), the EAFP sample will run slower. The Python [profiler](https://docs.python.org/library/profile.html) can be used in specific cases to determine performance characteristics. If exceptional cases are rare, then the EAFP version will have superior [average performance](/wiki/Average_performance "Average performance") than the alternative. In addition, it avoids the whole class of [time-of-check to time-of-use](/wiki/Time-of-check_to_time-of-use "Time-of-check to time-of-use") (TOCTTOU) vulnerabilities, other [race conditions](/wiki/Race_conditions "Race conditions"),[[37]](#cite_note-nutshell-41)[[39]](#cite_note-43) and is compatible with [duck typing](/wiki/Duck_typing "Duck typing"). A drawback of EAFP is that it can be used only with statements; an exception cannot be caught in a generator expression, list comprehension, or lambda function.

Comments and docstrings
-----------------------

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=38 "Edit section: Comments and docstrings")]

There are two ways to annotate Python code. One is by using comments to indicate what some part of the code does. Single-line comments begin with the hash character (`#`) and continue until the end of the line. Comments spanning more than one line are achieved by inserting a multi-line string (with `"""` or `'''` as the delimiter on each end) that is not used in assignment or otherwise evaluated, but sits in between other statements.

Commenting a piece of code:

```
import sys

def getline() -> str:
    return sys.stdin.readline()  # Get one line and return it
```

Commenting a piece of code with multiple lines:

```
def getline() -> str:
    """This function gets one line and returns it.

    As a demonstration, this is a multiline docstring.

    This full string can be accessed as getline.__doc__.
    """
    return sys.stdin.readline()
```

[Docstrings](/wiki/Docstring "Docstring") (documentation strings), that is, strings that are located alone without assignment as the first indented line within a module, class, method or function, automatically set their contents as an attribute named `__doc__`, which is intended to store a human-readable description of the object's purpose, behavior, and usage. The built-in `help` function generates its output based on `__doc__` attributes. Such strings can be delimited with `"` or `'` for single line strings, or may span multiple lines if delimited with either `"""` or `'''` which is Python's notation for specifying multi-line strings. However, the style guide for the language specifies that triple double quotes (`"""`) are preferred for both single and multi-line docstrings.[[40]](#cite_note-44)

Single-line docstring:

```
def getline() -> str:
    """Get one line from stdin and return it."""
    return sys.stdin.readline()
```

Multi-line docstring:

```
def getline() -> str:
    """Get one line
       from stdin
       and return it.
    """
    return sys.stdin.readline()
```

Docstrings can be as large as the programmer wants and contain [line breaks](/wiki/Newline "Newline"). In contrast with comments, docstrings are themselves Python objects and are part of the interpreted code that Python runs. That means that a running program can retrieve its own docstrings and manipulate that information, but the normal usage is to give other programmers information about how to invoke the object being documented in the docstring.

There are tools available that can extract the docstrings from Python code and generate documentation. Docstring documentation can also be accessed from the interpreter with the `help()` function, or from the shell with the [pydoc](/wiki/Pydoc "Pydoc") command `pydoc`.

The [doctest](/wiki/Doctest "Doctest") standard module uses interactions copied from Python shell sessions into docstrings to create tests, whereas the [docopt](http://docopt.org) module uses them to define command-line options.

Decorators
----------

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=39 "Edit section: Decorators")]

See also: [Advice (programming)](/wiki/Advice_(programming) "Advice (programming)")

A decorator is any callable Python object that is used to modify a function, method or class definition. A decorator is passed the original object being defined and returns a modified object, which is then bound to the name in the definition. Python decorators were inspired in part by [Java annotations](/wiki/Java_annotation "Java annotation"), and have a similar syntax; the decorator syntax is pure [syntactic sugar](/wiki/Syntactic_sugar "Syntactic sugar"), using `@` as the keyword:

```
@viking_chorus
def menu_item() -> None:
    print("spam")
```

is equivalent to

```
def menu_item() -> None:
    print("spam")
menu_item = viking_chorus(menu_item)
```

Decorators are a form of [metaprogramming](/wiki/Metaprogramming "Metaprogramming"); they enhance the action of the function or method they decorate. For example, in the sample below, `viking_chorus` might cause `menu_item` to be run 8 times (see [Spam sketch](/wiki/Spam_(Monty_Python) "Spam (Monty Python)")) for each time it is called:

```
R: TypeVar = TypeVar("R")

def viking_chorus(myfunc: Callable[..., R]) -> Callable[..., None]:
    def inner_func(*args: tuple[Any, ...], **kwargs: dict[str, Any]):
        for i in range(8):
            myfunc(*args, **kwargs)
    return inner_func
```

Canonical uses of function decorators are for creating [class methods](/wiki/Class_method "Class method") or [static methods](/wiki/Static_method "Static method"), adding function attributes, [tracing](/wiki/Tracing_(software) "Tracing (software)"), setting [pre-](/wiki/Precondition "Precondition") and [postconditions](/wiki/Postcondition "Postcondition"), and [synchronization](/wiki/Synchronization "Synchronization"),[[41]](#cite_note-45) but can be used for far more, including [tail recursion elimination](/wiki/Tail_recursion_elimination "Tail recursion elimination"),[[42]](#cite_note-46) [memoization](/wiki/Memoization "Memoization") and even improving the writing of other decorators.[[43]](#cite_note-47)

Decorators can be chained by placing several on adjacent lines:

```
@invincible
@favourite_colour("Blue")
def black_knight() -> None:
    pass
```

is equivalent to

```
def black_knight() -> None:
    pass
black_knight = invincible(favourite_colour("Blue")(black_knight))
```

or, using intermediate variables

```
def black_knight() -> None:
    pass
blue_decorator = favourite_colour("Blue")
decorated_by_blue = blue_decorator(black_knight)
black_knight = invincible(decorated_by_blue)
```

In the example above, the `favourite_colour` decorator [factory](/wiki/Factory_(software_concept) "Factory (software concept)") takes an argument. Decorator factories must return a decorator, which is then called with the object to be decorated as its argument:

```
def favourite_colour(colour: str) -> Callable[[Callable[[], R]], Callable[[], R]]:
    def decorator(func: Callable[[], R]) -> Callable[[], R]:
        def wrapper() -> R:
            print(colour)
            func()
        return wrapper
    return decorator
```

This would then decorate the `black_knight` function such that the colour, `"Blue"`, would be printed prior to the `black_knight` function running. [Closure](/wiki/Closure_(computer_programming) "Closure (computer programming)") ensures that the colour argument is accessible to the innermost wrapper function even when it is returned and goes out of scope, which is what allows decorators to work.

Despite the name, Python decorators are not an implementation of the [decorator pattern](/wiki/Decorator_pattern "Decorator pattern"). The decorator pattern is a [design pattern](/wiki/Design_pattern "Design pattern") used in [statically-typed](/wiki/Statically-typed "Statically-typed") [object-oriented programming languages](/wiki/Object-oriented_programming_language "Object-oriented programming language") to allow functionality to be added to objects at run time; Python decorators add functionality to functions and methods at definition time, and thus are a higher-level construct than decorator-pattern classes. The decorator pattern itself is trivially implementable in Python, because the language is [duck typed](/wiki/Duck_typed "Duck typed"), and so is not usually considered as such.[*[clarification needed](/wiki/Wikipedia:Please_clarify "Wikipedia:Please clarify")*]

Easter eggs
-----------

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=40 "Edit section: Easter eggs")]

Users of [curly bracket languages](/wiki/Curly_bracket_programming_language "Curly bracket programming language"), such as [C](/wiki/C_(programming_language) "C (programming language)") or [Java](/wiki/Java_(programming_language) "Java (programming language)"), sometimes expect or wish Python to follow a block-delimiter convention. Brace-delimited block syntax has been repeatedly requested, and consistently rejected by core developers. The Python interpreter contains an [easter egg](/wiki/Easter_egg_(virtual) "Easter egg (virtual)") that summarizes its developers' feelings on this issue. The code `from __future__ import braces` raises the exception `SyntaxError: not a chance`. The `__future__` module is normally used to [provide features from future versions](/wiki/Backporting "Backporting") of Python.

Another hidden message, the [Zen of Python](/wiki/Zen_of_Python "Zen of Python") (a summary of [Python design philosophy](/wiki/Python_(programming_language)#Design_philosophy_and_features "Python (programming language)")), is displayed when trying to `import this`.

The message `Hello world!` is printed when the import statement `import __hello__` is used. In Python 2.7, instead of `Hello world!` it prints `Hello world...`.

Importing the `antigravity` module opens a web browser to [xkcd](/wiki/Xkcd "Xkcd") comic [353](https://xkcd.com/353/) that portrays a humorous fictional use for such a module, intended to demonstrate the ease with which Python modules enable additional functionality.[[44]](#cite_note-48) In Python 3, this module also contains an implementation of the "geohash" algorithm, a reference to [xkcd](/wiki/Xkcd "Xkcd") comic [426](https://xkcd.com/426/).[[45]](#cite_note-49)

Notes
-----

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=41 "Edit section: Notes")]

1. ^ [***a***](#cite_ref-keywordIn35_6-0) [***b***](#cite_ref-keywordIn35_6-1) `async` and `await` were introduced in Python 3.5.[[5]](#cite_note-5)
2. ^ [***a***](#cite_ref-becameKeywordIn3_7-0) [***b***](#cite_ref-becameKeywordIn3_7-1) `True` and `False` became keywords in Python 3.0. Previously they were [global variables](/wiki/Global_variable "Global variable").
3. **[^](#cite_ref-keywordIn3_8-0)** `nonlocal` was introduced in Python 3.0.
4. ^ [***a***](#cite_ref-keywordIn310_11-0) [***b***](#cite_ref-keywordIn310_11-1) [***c***](#cite_ref-keywordIn310_11-2) `match`, `case` and `_` were introduced as keywords in Python 3.10.

References
----------

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=42 "Edit section: References")]

1. **[^](#cite_ref-1)** "Readability counts." - [PEP 20 - The Zen of Python](https://www.python.org/dev/peps/pep-0020/) [Archived](https://web.archive.org/web/20141205214430/https://www.python.org/dev/peps/pep-0020/) 2014-12-05 at the [Wayback Machine](/wiki/Wayback_Machine "Wayback Machine")
2. **[^](#cite_ref-PEP20_2-0)** ["PEP 20 - The Zen of Python"](https://www.python.org/dev/peps/pep-0020/). Python Software Foundation. 2004-08-23. [Archived](https://web.archive.org/web/20081203193726/http://www.python.org./dev/peps/pep-0020/) from the original on 2008-12-03. Retrieved 2008-11-24.
3. **[^](#cite_ref-3)** ["2. Lexical analysis"](https://docs.python.org/3/reference/lexical_analysis.html#keywords). *Python 3 documentation*. Python Software Foundation. Retrieved 2021-03-11.
4. **[^](#cite_ref-4)** ["2. Lexical analysis"](https://docs.python.org/2/reference/lexical_analysis.html#keywords). *Python v2.7.18 documentation*. Python Software Foundation. Retrieved 2021-03-11.
5. **[^](#cite_ref-5)** ["New Keywords"](https://docs.python.org/3/whatsnew/3.5.html#new-keywords). *Python v3.5 documentation*. Docs.python.org. [Archived](https://web.archive.org/web/20160618215313/https://docs.python.org/3//whatsnew/3.5.html#new-keywords) from the original on 2016-06-18. Retrieved 2016-06-01.
6. **[^](#cite_ref-9)** ["2. Lexical analysis"](https://docs.python.org/3/reference/lexical_analysis.html#soft-keywords). *Python 3 documentation*. Python Software Foundation. Retrieved 2022-01-22.
7. **[^](#cite_ref-pep-0622_10-0)** ["PEP 622 -- Structural Pattern Matching"](https://www.python.org/dev/peps/pep-0622/#backwards-compatibility). 2020-06-23. Retrieved 2022-01-22.
8. ^ [***a***](#cite_ref-pep3107_12-0) [***b***](#cite_ref-pep3107_12-1) ["PEP 3107 -- Function Annotations"](https://www.python.org/dev/peps/pep-3107/). [Archived](https://web.archive.org/web/20150106050429/https://www.python.org/dev/peps/pep-3107/) from the original on 2015-01-06. Retrieved 2014-08-15.
9. **[^](#cite_ref-13)** ["6. Modules"](https://docs.python.org/tutorial/modules.html). *The Python Tutorial*. Python Software Foundation. Retrieved 25 October 2010.
10. **[^](#cite_ref-14)** ["Python Scopes and Namespaces"](https://docs.python.org/tutorial/classes.html#python-scopes-and-namespaces). Docs.python.org. Retrieved 2011-07-26.
11. **[^](#cite_ref-15)** <https://docs.python.org/3/tutorial/modules.html> "in general the practice of importing \* from a module or package is frowned upon"
12. **[^](#cite_ref-16)** [Guido van Rossum](/wiki/Guido_van_Rossum "Guido van Rossum") (May 15, 2003). ["Python main() functions"](https://www.artima.com/weblogs/viewpost.jsp?thread=4829). [Archived](https://web.archive.org/web/20150711062438/http://www.artima.com/weblogs/viewpost.jsp?thread=4829) from the original on July 11, 2015. Retrieved June 29, 2015,[comments](https://www.artima.com/forums/flat.jsp?forum=106&thread=4829)
13. **[^](#cite_ref-17)** [Code Like a Pythonista: Idiomatic Python](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#modules-scripts) [Archived](https://web.archive.org/web/20140527204143/http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#modules-scripts) 2014-05-27 at the [Wayback Machine](/wiki/Wayback_Machine "Wayback Machine")—on Python scripts used as modules
14. **[^](#cite_ref-18)** Ned Batchelder (6 June 2003). ["Python main() functions"](http://nedbatchelder.com/blog/200306/python_main_functions.html). [Archived](https://web.archive.org/web/20150920223603/http://nedbatchelder.com/blog/200306/python_main_functions.html) from the original on 20 September 2015. Retrieved 29 June 2015.
15. **[^](#cite_ref-19)** ["PEP 8 -- Style Guide for Python Code"](https://www.python.org/dev/peps/pep-0008/). *Python.org*. Retrieved 2021-03-17.
16. **[^](#cite_ref-20)** Hoffa, Felipe (2017-07-26). ["400,000 GitHub repositories, 1 billion files, 14 terabytes of code: Spaces or Tabs?"](https://hoffa.medium.com/400-000-github-repositories-1-billion-files-14-terabytes-of-code-spaces-or-tabs-7cfe0b5dd7fd). *Medium*. Retrieved 2021-03-11.
17. **[^](#cite_ref-21)** ["Tabs or Spaces"](https://ukupat.github.io/tabs-or-spaces/). *ukupat.github.io*. Retrieved 2021-03-11.
18. **[^](#cite_ref-22)** ["PEP 8 -- Style Guide for Python Code"](https://www.python.org/dev/peps/pep-0008/). *Python.org*. Retrieved 2021-03-11.
19. **[^](#cite_ref-23)** ["PEP 498 - Literal String Interpolation"](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498). *What’s New In Python 3.6*. 2016-12-23. [Archived](https://web.archive.org/web/20170330002530/https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498) from the original on 2017-03-30. Retrieved 2017-03-29.
20. **[^](#cite_ref-24)** ["2. Lexical analysis"](https://docs.python.org/reference/lexical_analysis.html#string-literals). *Python v2.7.5 documentation*. Docs.python.org. [Archived](https://web.archive.org/web/20121023010739/http://docs.python.org/reference/lexical_analysis.html#string-literals) from the original on 2012-10-23. Retrieved 2013-08-16.
21. **[^](#cite_ref-25)** ["2. Lexical analysis"](https://docs.python.org/reference/lexical_analysis.html#string-literal-concatenation). *Python v2.7.5 documentation*. Docs.python.org. [Archived](https://web.archive.org/web/20121023010739/http://docs.python.org/reference/lexical_analysis.html#string-literal-concatenation) from the original on 2012-10-23. Retrieved 2013-08-16.
22. **[^](#cite_ref-26)** Hashable items are usually immutable, but not necessarily so by definition. See [python.org/3/glossary.htm](https://docs.python.org/3/glossary.html?highlight=hashable)
23. **[^](#cite_ref-27)** ["6. Expressions — Python 3.9.2 documentation"](https://docs.python.org/3/reference/expressions.html#comparisons). *docs.python.org*. Retrieved 2021-03-17.
24. **[^](#cite_ref-28)** ["BitwiseOperators - Python Wiki"](https://wiki.python.org/moin/BitwiseOperators). *wiki.python.org*. Retrieved 2025-12-02.
25. **[^](#cite_ref-29)** ["Python Bitwise Operators"](https://www.w3schools.com/python/python_operators_bitwise.asp). *www.w3schools.com*. Retrieved 2025-12-02.
26. **[^](#cite_ref-30)** ["Python 2.7.0 Release"](https://www.python.org/download/releases/2.7/). [Archived](https://web.archive.org/web/20160127021350/https://www.python.org/download/releases/2.7/) from the original on 2016-01-27. Retrieved 2016-01-19.
27. **[^](#cite_ref-31)** ["5. Data Structures — Python 2.7.18 documentation"](https://docs.python.org/2/tutorial/datastructures.html#sets). [Archived](https://web.archive.org/web/20160126161121/https://docs.python.org/2/tutorial/datastructures.html#sets) from the original on 2016-01-26. Retrieved 2016-01-19.
28. **[^](#cite_ref-32)** ["5. Data Structures — Python 2.7.18 documentation"](https://docs.python.org/2/tutorial/datastructures.html#dictionaries). [Archived](https://web.archive.org/web/20160126161121/https://docs.python.org/2/tutorial/datastructures.html#dictionaries) from the original on 2016-01-26. Retrieved 2016-01-19.
29. **[^](#cite_ref-33)** David Mertz. ["Functional Programming in Python"](https://web.archive.org/web/20070220181222/http://gnosis.cx/publish/programming/charming_python_13.html). IBM developerWorks. Archived from [the original](http://gnosis.cx/publish/programming/charming_python_13.html) on 2007-02-20. Retrieved 2007-08-27.
30. **[^](#cite_ref-34)** ["PEP 308 -- Conditional Expressions"](https://www.python.org/dev/peps/pep-0308/). [Archived](https://web.archive.org/web/20160313113147/https://www.python.org/dev/peps/pep-0308/) from the original on 2016-03-13. Retrieved 2016-04-14.
31. **[^](#cite_ref-35)** The `nonlocal` keyword was adopted by [PEP 3104](https://www.python.org/dev/peps/pep-3104/) [Archived](https://web.archive.org/web/20141202225741/https://www.python.org/dev/peps/pep-3104) 2014-12-02 at the [Wayback Machine](/wiki/Wayback_Machine "Wayback Machine")
32. **[^](#cite_ref-36)** ["Python Style Guide"](http://docs.python-guide.org/en/latest/writing/style/#we-are-all-responsible-users). docs.python-guide.org. [Archived](https://web.archive.org/web/20150309074305/http://docs.python-guide.org/en/latest/writing/style/#we-are-all-responsible-users) from the original on 2015-03-09. Retrieved 2015-03-08.
33. **[^](#cite_ref-37)** ["PEP 343 -- The "with" Statement"](https://www.python.org/dev/peps/pep-0343/). [Archived](https://web.archive.org/web/20141214110002/https://www.python.org/dev/peps/pep-0343/) from the original on 2014-12-14. Retrieved 2014-08-15.
34. **[^](#cite_ref-38)** ["Glossary — Python 3.9.2 documentation"](https://docs.python.org/3/glossary.html#term-descriptor). *docs.python.org*. Retrieved 2021-03-23.
35. **[^](#cite_ref-39)** [EAFP](https://docs.python.org/glossary.html#term-eafp) [Archived](https://web.archive.org/web/20121026064048/http://docs.python.org/glossary.html#term-eafp) 2012-10-26 at the [Wayback Machine](/wiki/Wayback_Machine "Wayback Machine"), Python Glossary
36. **[^](#cite_ref-40)** Hamblen, Diane. ["Only the Limits of Our Imagination: An exclusive interview with RADM Grace M. Hopper"](https://web.archive.org/web/20090114165606/http://www.chips.navy.mil/archives/86_jul/interview.html). Department of the Navy Information Technology Magazine. Archived from [the original](http://www.chips.navy.mil/archives/86_jul/interview.html) on January 14, 2009. Retrieved 2007-01-31.
37. ^ [***a***](#cite_ref-nutshell_41-0) [***b***](#cite_ref-nutshell_41-1) *Python in a nutshell,* [Alex Martelli](/wiki/Alex_Martelli "Alex Martelli"), [p. 134](https://books.google.com/books?id=JnR9hQA3SncC&pg=PA134)
38. **[^](#cite_ref-42)** [LBYL](https://docs.python.org/3/glossary.html#term-lbyl) [Archived](https://web.archive.org/web/20180121071609/https://docs.python.org/3/glossary.html#term-lbyl) 2018-01-21 at the [Wayback Machine](/wiki/Wayback_Machine "Wayback Machine"), Python Glossary
39. **[^](#cite_ref-43)** [Alex Martelli](/wiki/Alex_Martelli "Alex Martelli") (19 May 2003). ["EAFP v. LBYL"](http://code.activestate.com/lists/python-list/337643/). python-list mailing list. Retrieved 18 July 2011.`{{cite web}}`: CS1 maint: deprecated archival service ([link](/wiki/Category:CS1_maint:_deprecated_archival_service "Category:CS1 maint: deprecated archival service"))
40. **[^](#cite_ref-44)** ["PEP 8 -- Style Guide for Python Code"](https://www.python.org/dev/peps/pep-0008/). *Python.org*. Retrieved 2021-03-23.
41. **[^](#cite_ref-45)** ["Python 2.4 Decorators: Reducing code duplication and consolidating knowledge"](https://www.ddj.com/184406073#l11). *Dr. Dobb's*. 2005-05-01. [Archived](https://web.archive.org/web/20070206063944/http://www.ddj.com/184406073#l11) from the original on 2007-02-06. Retrieved 2007-02-08.
42. **[^](#cite_ref-46)** ["New Tail Recursion Decorator"](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/496691). *ASPN: Python Cookbook*. 2006-11-14. [Archived](https://web.archive.org/web/20070209010200/http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/496691) from the original on 2007-02-09. Retrieved 2007-02-08.
43. **[^](#cite_ref-47)** ["The decorator module"](http://www.phyast.pitt.edu/~micheles/python/documentation.html). [Archived](https://web.archive.org/web/20070210000956/http://www.phyast.pitt.edu/%7Emicheles/python/documentation.html) from the original on 2007-02-10. Retrieved 2007-02-08.
44. **[^](#cite_ref-48)** [*cpython: The Python programming language*](https://github.com/python/cpython), Python, 2017-10-15, [archived](https://web.archive.org/web/20170915183846/https://github.com/python/cpython) from the original on 2017-09-15, retrieved 2017-10-15
45. **[^](#cite_ref-49)** ["Another hidden treasure. · python/cpython@b1614a7"](https://github.com/python/cpython/commit/b1614a7b6705f939b29df4045e591fcf53a8611b). *GitHub*. Retrieved 2017-10-15.

External links
--------------

[[edit](/w/index.php?title=Python_syntax_and_semantics&action=edit&section=43 "Edit section: External links")]

* ["The Python Language Reference"](https://docs.python.org/3/reference/index.html#reference-index).

* [Van Rossum, Guido](/wiki/Guido_van_Rossum "Guido van Rossum"). ["The Python Tutorial"](https://docs.python.org/3/tutorial/). (written by the author of Python)

* Ramalho, Luciano (April 2022). [*Fluent Python, 2nd Edition*](https://www.thoughtworks.com/insights/books/fluent-python-2nd-edition). O'Reilly Media, Inc. [ISBN](/wiki/ISBN_(identifier) "ISBN (identifier)") [9781492056355](/wiki/Special:BookSources/9781492056355 "Special:BookSources/9781492056355").

![](https://en.wikipedia.org/wiki/Special:CentralAutoLogin/start?useformat=desktop&type=1x1&usesul3=1)

Retrieved from "<https://en.wikipedia.org/w/index.php?title=Python_syntax_and_semantics&oldid=1350541549>"

[Categories](/wiki/Help:Category "Help:Category"):

* [Programming language syntax](/wiki/Category:Programming_language_syntax "Category:Programming language syntax")
* [Python (programming language)](/wiki/Category:Python_(programming_language) "Category:Python (programming language)")

Hidden categories:

* [Webarchive template wayback links](/wiki/Category:Webarchive_template_wayback_links "Category:Webarchive template wayback links")
* [CS1 maint: deprecated archival service](/wiki/Category:CS1_maint:_deprecated_archival_service "Category:CS1 maint: deprecated archival service")
* [Articles with short description](/wiki/Category:Articles_with_short_description "Category:Articles with short description")
* [Short description is different from Wikidata](/wiki/Category:Short_description_is_different_from_Wikidata "Category:Short description is different from Wikidata")
* [All articles with unsourced statements](/wiki/Category:All_articles_with_unsourced_statements "Category:All articles with unsourced statements")
* [Articles with unsourced statements from July 2025](/wiki/Category:Articles_with_unsourced_statements_from_July_2025 "Category:Articles with unsourced statements from July 2025")
* [All articles lacking reliable references](/wiki/Category:All_articles_lacking_reliable_references "Category:All articles lacking reliable references")
* [Articles lacking reliable references from March 2021](/wiki/Category:Articles_lacking_reliable_references_from_March_2021 "Category:Articles lacking reliable references from March 2021")
* [Wikipedia articles needing clarification from March 2021](/wiki/Category:Wikipedia_articles_needing_clarification_from_March_2021 "Category:Wikipedia articles needing clarification from March 2021")
* [Wikipedia articles needing clarification from April 2015](/wiki/Category:Wikipedia_articles_needing_clarification_from_April_2015 "Category:Wikipedia articles needing clarification from April 2015")
* [Articles with example Python (programming language) code](/wiki/Category:Articles_with_example_Python_(programming_language)_code "Category:Articles with example Python (programming language) code")
* [Articles with example C code](/wiki/Category:Articles_with_example_C_code "Category:Articles with example C code")

* This page was last edited on 22 April 2026, at 14:28 (UTC).
* Text is available under the [Creative Commons Attribution-ShareAlike 4.0 License](/wiki/Wikipedia:Text_of_the_Creative_Commons_Attribution-ShareAlike_4.0_International_License "Wikipedia:Text of the Creative Commons Attribution-ShareAlike 4.0 International License");
  additional terms may apply. By using this site, you agree to the [Terms of Use](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Terms_of_Use "foundation:Special:MyLanguage/Policy:Terms of Use") and [Privacy Policy](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy "foundation:Special:MyLanguage/Policy:Privacy policy"). Wikipedia® is a registered trademark of the [Wikimedia Foundation, Inc.](https://wikimediafoundation.org/), a non-profit organization.

* [Privacy policy](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Privacy_policy)
* [About Wikipedia](/wiki/Wikipedia:About)
* [Disclaimers](/wiki/Wikipedia:General_disclaimer)
* [Contact Wikipedia](//en.wikipedia.org/wiki/Wikipedia:Contact_us)
* [Legal & safety contacts](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Legal:Wikimedia_Foundation_Legal_and_Safety_Contact_Information)
* [Code of Conduct](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Universal_Code_of_Conduct)
* [Developers](https://developer.wikimedia.org)
* [Statistics](https://stats.wikimedia.org/#/en.wikipedia.org)
* [Cookie statement](https://foundation.wikimedia.org/wiki/Special:MyLanguage/Policy:Cookie_statement)
* [Mobile view](//en.wikipedia.org/w/index.php?title=Python_syntax_and_semantics&mobileaction=toggle_view_mobile)

* [![Wikimedia Foundation](/static/images/footer/wikimedia.svg)](https://www.wikimedia.org/)
* [![Powered by MediaWiki](/w/resources/assets/mediawiki_compact.svg)](https://www.mediawiki.org/)

Search

Search

Toggle the table of contents

Python syntax and semantics

5 languages
[Add topic](#)