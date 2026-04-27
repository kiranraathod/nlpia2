Statement (computer science) - Wikipedia

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
* [Create account](/w/index.php?title=Special:CreateAccount&returnto=Statement+%28computer+science%29 "You are encouraged to create an account and log in; however, it is not mandatory")
* [Log in](/w/index.php?title=Special:UserLogin&returnto=Statement+%28computer+science%29 "You're encouraged to log in; however, it's not mandatory. [o]")

Personal tools

* [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
* [Create account](/w/index.php?title=Special:CreateAccount&returnto=Statement+%28computer+science%29 "You are encouraged to create an account and log in; however, it is not mandatory")
* [Log in](/w/index.php?title=Special:UserLogin&returnto=Statement+%28computer+science%29 "You're encouraged to log in; however, it's not mandatory. [o]")

Contents
--------

move to sidebar
hide

* [(Top)](#)
* [1
  Simple statements](#Simple_statements)
* [2
  Compound statements](#Compound_statements)
* [3
  Syntax](#Syntax)


  Toggle Syntax subsection
  + [3.1
    Statements and keywords](#Statements_and_keywords)
    - [3.1.1
      No distinguished keywords](#No_distinguished_keywords)
    - [3.1.2
      Flagged words](#Flagged_words)
    - [3.1.3
      Reserved keywords](#Reserved_keywords)
* [4
  Semantics](#Semantics)
* [5
  Expressions](#Expressions)
* [6
  Extensibility](#Extensibility)
* [7
  See also](#See_also)
* [8
  References](#References)
* [9
  External links](#External_links)

Toggle the table of contents

Statement (computer science)
============================

25 languages

* [العربية](https://ar.wikipedia.org/wiki/%D8%B9%D8%A8%D8%A7%D8%B1%D8%A9_(%D8%B9%D9%84%D9%85_%D8%A7%D9%84%D8%AD%D8%A7%D8%B3%D9%88%D8%A8) "عبارة (علم الحاسوب) – Arabic")
* [Azərbaycanca](https://az.wikipedia.org/wiki/Deyim_(informatika) "Deyim (informatika) – Azerbaijani")
* [Čeština](https://cs.wikipedia.org/wiki/P%C5%99%C3%ADkaz_(programov%C3%A1n%C3%AD) "Příkaz (programování) – Czech")
* [Dansk](https://da.wikipedia.org/wiki/S%C3%A6tning_(programmering) "Sætning (programmering) – Danish")
* [Deutsch](https://de.wikipedia.org/wiki/Anweisung_(Programmierung) "Anweisung (Programmierung) – German")
* [Esperanto](https://eo.wikipedia.org/wiki/Ordono_(programlingvo) "Ordono (programlingvo) – Esperanto")
* [Eesti](https://et.wikipedia.org/wiki/Lause_(programmeerimine) "Lause (programmeerimine) – Estonian")
* [Suomi](https://fi.wikipedia.org/wiki/Lause_(ohjelmointi) "Lause (ohjelmointi) – Finnish")
* [Hrvatski](https://hr.wikipedia.org/wiki/Naredba_(programiranje) "Naredba (programiranje) – Croatian")
* [日本語](https://ja.wikipedia.org/wiki/%E6%96%87_(%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0) "文 (プログラミング) – Japanese")
* [Qaraqalpaqsha](https://kaa.wikipedia.org/wiki/Operator_(programmalast%C4%B1r%C4%B1w) "Operator (programmalastırıw) – Kara-Kalpak")
* [한국어](https://ko.wikipedia.org/wiki/%EB%AC%B8_(%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D) "문 (프로그래밍) – Korean")
* [Олык марий](https://mhr.wikipedia.org/wiki/%D0%9E%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80 "Оператор – Eastern Mari")
* [മലയാളം](https://ml.wikipedia.org/wiki/%E0%B4%B8%E0%B5%8D%E0%B4%B1%E0%B5%8D%E0%B4%B1%E0%B5%86%E0%B4%AF%E0%B5%8D%E2%80%8C%E0%B4%B1%E0%B5%8D%E0%B4%B1%E0%B5%8D%E0%B4%AE%E0%B5%86%E0%B4%A8%E0%B5%8D%E0%B4%B1%E0%B5%8D_(%E0%B4%95%E0%B4%AE%E0%B5%8D%E0%B4%AA%E0%B5%8D%E0%B4%AF%E0%B5%82%E0%B4%9F%E0%B5%8D%E0%B4%9F%E0%B5%BC_%E0%B4%AA%E0%B5%8D%E0%B4%B0%E0%B5%8B%E0%B4%97%E0%B5%8D%E0%B4%B0%E0%B4%BE%E0%B4%AE%E0%B4%BF%E0%B4%99%E0%B5%8D%E0%B4%99%E0%B5%8D) "സ്റ്റെയ്‌റ്റ്മെന്റ് (കമ്പ്യൂട്ടർ പ്രോഗ്രാമിങ്ങ്) – Malayalam")
* [Nederlands](https://nl.wikipedia.org/wiki/Statement "Statement – Dutch")
* [Polski](https://pl.wikipedia.org/wiki/Instrukcja_(informatyka) "Instrukcja (informatyka) – Polish")
* [Русский](https://ru.wikipedia.org/wiki/%D0%9E%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80_(%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5) "Оператор (программирование) – Russian")
* [Slovenčina](https://sk.wikipedia.org/wiki/Programov%C3%BD_pr%C3%ADkaz "Programový príkaz – Slovak")
* [Shqip](https://sq.wikipedia.org/wiki/Deklarata_(shkenc%C3%AB_kompjuterike) "Deklarata (shkencë kompjuterike) – Albanian")
* [Српски / srpski](https://sr.wikipedia.org/wiki/%D0%9D%D0%B0%D1%80%D0%B5%D0%B4%D0%B1%D0%B0_(%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%B8%D1%80%D0%B0%D1%9A%D0%B5) "Наредба (програмирање) – Serbian")
* [Svenska](https://sv.wikipedia.org/wiki/Sats_(programmering) "Sats (programmering) – Swedish")
* [Українська](https://uk.wikipedia.org/wiki/%D0%86%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D1%96%D1%8F_(%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D1%83%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F) "Інструкція (програмування) – Ukrainian")
* [Tiếng Việt](https://vi.wikipedia.org/wiki/C%C3%A2u_l%E1%BB%87nh_(khoa_h%E1%BB%8Dc_m%C3%A1y_t%C3%ADnh) "Câu lệnh (khoa học máy tính) – Vietnamese")
* [粵語](https://zh-yue.wikipedia.org/wiki/%E9%99%B3%E8%BF%B0%E5%BC%8F_(%E9%9B%BB%E8%85%A6%E7%A7%91%E5%AD%B8) "陳述式 (電腦科學) – Cantonese")
* [中文](https://zh.wikipedia.org/wiki/%E9%99%B3%E8%BF%B0%E5%BC%8F "陳述式 – Chinese")

[Edit links](https://www.wikidata.org/wiki/Special:EntityPage/Q613299#sitelinks-wikipedia "Edit interlanguage links")

* [Article](/wiki/Statement_(computer_science) "View the content page [c]")
* [Talk](/wiki/Talk:Statement_(computer_science) "Discuss improvements to the content page [t]")

English

* [Read](/wiki/Statement_(computer_science))
* [Edit](/w/index.php?title=Statement_(computer_science)&action=edit "Edit this page [e]")
* [View history](/w/index.php?title=Statement_(computer_science)&action=history "Past revisions of this page [h]")



Tools

Tools

move to sidebar
hide

Actions

* [Read](/wiki/Statement_(computer_science))
* [Edit](/w/index.php?title=Statement_(computer_science)&action=edit "Edit this page [e]")
* [View history](/w/index.php?title=Statement_(computer_science)&action=history)

General

* [What links here](/wiki/Special:WhatLinksHere/Statement_(computer_science) "List of all English Wikipedia pages containing links to this page [j]")
* [Related changes](/wiki/Special:RecentChangesLinked/Statement_(computer_science) "Recent changes in pages linked from this page [k]")
* [Upload file](//en.wikipedia.org/wiki/Wikipedia:File_Upload_Wizard "Upload files [u]")
* [Permanent link](/w/index.php?title=Statement_(computer_science)&oldid=1341072797 "Permanent link to this revision of this page")
* [Page information](/w/index.php?title=Statement_(computer_science)&action=info "More information about this page")
* [Cite this page](/w/index.php?title=Special:CiteThisPage&page=Statement_%28computer_science%29&id=1341072797&wpFormIdentifier=titleform "Information on how to cite this page")
* [Get shortened URL](/w/index.php?title=Special:UrlShortener&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FStatement_%28computer_science%29)

Print/export

* [Download as PDF](/w/index.php?title=Special:DownloadAsPdf&page=Statement_%28computer_science%29&action=show-download-screen "Download this page as a PDF file")
* [Printable version](/w/index.php?title=Statement_(computer_science)&printable=yes "Printable version of this page [p]")

In other projects

* [Wikidata item](https://www.wikidata.org/wiki/Special:EntityPage/Q613299 "Structured data on this page hosted by Wikidata [g]")

Appearance

move to sidebar
hide

From Wikipedia, the free encyclopedia

Section of code that details a specific command

For other uses, see [Statement](/wiki/Statement_(disambiguation) "Statement (disambiguation)").

In [computer programming](/wiki/Computer_programming "Computer programming"), a **statement** is a [syntactic](/wiki/Syntax_(programming_languages) "Syntax (programming languages)") unit of an [imperative programming language](/wiki/Imperative_programming "Imperative programming") that expresses some action to be carried out.[[1]](#cite_note-1) [*[vague](/wiki/Wikipedia:Vagueness "Wikipedia:Vagueness")*] A [program](/wiki/Computer_program "Computer program") written in such a language is formed by a sequence of one or more statements. A statement may have internal components (e.g. [expressions](/wiki/Expression_(computer_science) "Expression (computer science)")).

Many programming languages (e.g. [Ada](/wiki/Ada_(programming_language) "Ada (programming language)"), [Algol 60](/wiki/Algol_60 "Algol 60"), [C](/wiki/C_(programming_language) "C (programming language)"), [Java](/wiki/Java_(programming_language) "Java (programming language)"), [Pascal](/wiki/Pascal_(programming_language) "Pascal (programming language)"))[[2]](#cite_note-CommonBase-2): 15 make a distinction between statements and [definitions/declarations](/wiki/Declaration_(computer_programming) "Declaration (computer programming)"). A definition or declaration specifies the data on which a program is to operate, while a statement specifies the actions to be taken with that data.

Statements which cannot contain other statements are *simple*; those which can contain other statements are *compound*.[[3]](#cite_note-ALGOL60-3)

The appearance of a statement (and indeed a program) is determined by its [syntax](/wiki/Syntax_(programming_languages) "Syntax (programming languages)") or grammar. The meaning of a statement is determined by its [semantics](/wiki/Semantics_(computer_science) "Semantics (computer science)").

Simple statements
-----------------

[[edit](/w/index.php?title=Statement_(computer_science)&action=edit&section=1 "Edit section: Simple statements")]

Simple statements are complete in themselves; these include assignments, subroutine calls, and a few statements which may significantly affect the program flow of control (e.g. [goto](/wiki/Goto "Goto"), [return](/wiki/Return_statement "Return statement"), stop/halt). In some languages, input and output, assertions, and exits are handled by special statements, while other languages use calls to predefined subroutines.

* [assignment](/wiki/Assignment_(computer_science) "Assignment (computer science)")
  + Fortran: `variable = expression`
  + Pascal, Algol 60, Ada: `variable := expression;`
  + C, C#, C++, PHP, Java: `variable = expression;`
* [call](/wiki/Subroutine "Subroutine")
  + Fortran: `CALL subroutine name(parameters)`
  + C, C++, Java, PHP, Pascal, Ada: `subroutine name(parameters);`
* [assertion](/wiki/Assertion_(software_development) "Assertion (software development)")
  + C, C++, PHP: `assert(relational expression);`
  + Java: `assert relational expression;`
* [goto](/wiki/GOTO "GOTO")
  + Fortran: `GOTO numbered-label`
  + Algol 60: `goto label;`
  + C, C++, PHP, Pascal: `goto label;`
* [return](/wiki/Return_statement "Return statement")
  + Fortran: `RETURN value`
  + C, C++, Java, PHP: `return value;`
* [stop/halt/exit](/wiki/Exit_(system_call) "Exit (system call)")
  + Fortran: `STOP number`
  + C, C++: `exit(expression)`
  + PHP: `exit number;`

Compound statements
-------------------

[[edit](/w/index.php?title=Statement_(computer_science)&action=edit&section=2 "Edit section: Compound statements")]

Main article: [Block (programming)](/wiki/Block_(programming) "Block (programming)")

Compound statements may contain (sequences of) statements, nestable to any reasonable depth, and generally involve tests to decide whether or not to obey or repeat these contained statements.

:   :   Notation for the following examples:

        * <statement> is any single statement (could be simple or compound).
        * <sequence> is any sequence of zero or more <statements>
    :   Some programming languages provide a general way of grouping statements together, so that any single <statement> can be replaced by a group:

:   :   * Algol 60: `begin <sequence> end`
        * Pascal: `begin <sequence> end`
        * C, PHP, Java: `{ <sequence> }`

:   :   Other programming languages have a different special terminator on each kind of compound statement, so that one or more statements are automatically treated as a group:

        * Ada: `if test then <sequence> end if;`

Many compound statements are loop commands or choice commands. In theory only one of each of these types of commands is required. In practice there are various special cases which occur quite often; these may make a program easier to understand, may make programming easier, and can often be implemented much more efficiently. There are many subtleties not mentioned here; see the linked articles for details.

* [count-controlled loop](/wiki/For_loop "For loop"):
  + Algol 60: `for index := 1 step 1 until limit do <statement> ;`
  + Pascal: `for index := 1 to limit do <statement> ;`
  + C, Java: `for ( index = 1; index <= limit; index += 1) <statement> ;`
  + Ada: `for index in 1..limit loop <sequence> end loop`
  + Fortran 90:

    ```
    DO index = 1,limit
        <sequence>
    END DO
    ```
* [condition-controlled loop](/wiki/While_loop "While loop") with test at start of loop:
  + Algol 60: `for index := expression while test do <statement> ;`
  + Pascal: `while test do <statement> ;`
  + C, Java: `while (test) <statement> ;`
  + Ada: `while test loop <sequence> end loop`
  + Fortran 90:

    ```
    DO WHILE (test)
        <sequence>
    END DO
    ```
* [condition-controlled loop](/wiki/Do_while_loop "Do while loop") with test at end of loop:
  + Pascal: `repeat <sequence> until test; { note reversed test }`
  + C, Java: `do { <sequence> } while (test) ;`
  + Ada: `loop <sequence> exit when test; end loop;`
* condition-controlled loop with test in the middle of the loop:
  + C: `do { <sequence> if (test) break; <sequence> } while (true) ;`
  + Ada: `loop <sequence> exit when test; <sequence> end loop;`
* [if-statement](/wiki/Conditional_(programming) "Conditional (programming)") simple situation:
  + Algol 60:`if test then <unconditional statement> ;`
  + Pascal: `if test then <statement> ;`
  + C, Java: `if (test) <statement> ;`
  + Ada: `if test then <sequence> end if;`
  + Fortran 77+:

    ```
    IF (test) THEN
        <sequence>
    END IF
    ```
* [if-statement](/wiki/Conditional_(programming) "Conditional (programming)") two-way choice:
  + Algol 60: `if test then <unconditional statement> else <statement> ;`
  + Pascal: `if test then <statement> else <statement> ;`
  + C, Java: `if (test) <statement> else <statement> ;`
  + Ada: `if test then <sequence> else <sequence> end if;`
  + Fortran 77+:

    ```
    IF (test) THEN
        <sequence>
    ELSE
        <sequence>
    END IF
    ```
* [case/switch statement](/wiki/Switch_statement "Switch statement") multi-way choice:
  + Pascal: `case c of 'a': alert(); 'q': quit(); end;`
  + Ada: `case c is when 'a' => alert(); when 'q' => quit(); end case;`
  + C, Java: `switch (c) { case 'a': alert(); break; case 'q': quit(); break; }`
* [Exception handling](/wiki/Exception_handling "Exception handling"):
  + Ada: `begin protected code except when exception specification => exception handler`
  + Java: `try { protected code } catch (exception specification) { exception handler } finally { cleanup }`
  + Python:  `try: protected code except exception specification: exception handler else: no exceptions finally: cleanup`

Syntax
------

[[edit](/w/index.php?title=Statement_(computer_science)&action=edit&section=3 "Edit section: Syntax")]

Main article: [Syntax (programming languages)](/wiki/Syntax_(programming_languages) "Syntax (programming languages)")

Apart from assignments and subroutine calls, most languages start each statement with a special word (e.g. goto, if, while, etc.) as shown in the above examples. Various methods have been used to describe the form of statements in different languages; the more formal methods tend to be more precise:

* Algol 60 used [Backus–Naur form](/wiki/Backus%E2%80%93Naur_form "Backus–Naur form") (BNF) which set a new level for language grammar specification.[[4]](#cite_note-ALGOL60RPT-4)
* Up until Fortran 77, the language was described in English prose with examples,[[5]](#cite_note-FORTRAN66-5) From Fortran 90 onwards, the language was described using a variant of BNF.[[6]](#cite_note-FORTRAN95-6)
* Cobol used a two-dimensional metalanguage.[[7]](#cite_note-COBOL1959-7)
* Pascal used both [syntax diagrams](/wiki/Syntax_diagram "Syntax diagram") and equivalent BNF.[[8]](#cite_note-PASCAL-8)

BNF uses recursion to express repetition, so various [extensions](/wiki/Extended_Backus%E2%80%93Naur_form "Extended Backus–Naur form") have been proposed to allow direct indication of repetition.

### Statements and keywords

[[edit](/w/index.php?title=Statement_(computer_science)&action=edit&section=4 "Edit section: Statements and keywords")]

Some programming language grammars [reserve keywords](/wiki/Reserved_word "Reserved word") or [mark them specially](/wiki/Stropping_(syntax) "Stropping (syntax)"), and do not allow them to be used as [identifiers](/wiki/Identifier_(computer_languages) "Identifier (computer languages)"). This often leads to [grammars](/wiki/Formal_grammar "Formal grammar") which are easier to [parse](/wiki/Parsing "Parsing"), requiring less [lookahead](/wiki/Parsing#Lookahead "Parsing").

#### No distinguished keywords

[[edit](/w/index.php?title=Statement_(computer_science)&action=edit&section=5 "Edit section: No distinguished keywords")]

Fortran and PL/1 do not have reserved keywords, allowing statements like:

* in PL/1:
  + `IF IF = THEN THEN ...` (the second `IF` and the first `THEN` are variables).
* in Fortran:
  + `IF (A) X = 10...` conditional statement (with other variants)
  + `IF (A) = 2` assignment to a subscripted variable named `IF`

:   :   As spaces were optional up to Fortran 95, a typo could completely change the meaning of a statement:

    * `DO 10 I = 1,5` start of a loop with I running from 1 to 5
    * `DO 10 I = 1.5` assignment of the value 1.5 to the variable `DO10I`

#### Flagged words

[[edit](/w/index.php?title=Statement_(computer_science)&action=edit&section=6 "Edit section: Flagged words")]

Main article: [Stropping (syntax)](/wiki/Stropping_(syntax) "Stropping (syntax)")

In Algol 60 and Algol 68, special tokens were distinguished explicitly: for publication, in boldface e.g. `begin`; for programming, with some special marking, e.g., a flag (`'begin`), quotation marks (`'begin'`), or underlined (`begin` on the [Elliott 503](/wiki/Elliott_503 "Elliott 503")). This is called "stropping".

Tokens that are part of the language syntax thus do not conflict with programmer-defined names.

#### Reserved keywords

[[edit](/w/index.php?title=Statement_(computer_science)&action=edit&section=7 "Edit section: Reserved keywords")]

Main article: [Reserved word](/wiki/Reserved_word "Reserved word")

Certain names are reserved as part of the programming language and can not be used as programmer-defined names. The majority of the most popular programming languages use reserved keywords. Early examples include [FLOW-MATIC](/wiki/FLOW-MATIC "FLOW-MATIC") (1953) and [COBOL](/wiki/COBOL "COBOL") (1959). Since 1970 other examples include Ada, C, C++, Java, and Pascal. The number of reserved words depends on the language: C has about 30 while COBOL has about 400.

Semantics
---------

[[edit](/w/index.php?title=Statement_(computer_science)&action=edit&section=8 "Edit section: Semantics")]

Main article: [Semantics (computer science)](/wiki/Semantics_(computer_science) "Semantics (computer science)")

Semantics is concerned with the meaning of a program. The standards documents for many programming languages use BNF or some equivalent to express the syntax/grammar in a fairly formal and precise way, but the semantics/meaning of the program is generally described using examples and English prose. This can result in ambiguity.[[9]](#cite_note-Trouble-9) In some language descriptions the meaning of compound statements is defined by the use of 'simpler' constructions, e.g. a while loop can be defined by a combination of tests, jumps, and [labels](/wiki/Label_(computer_science) "Label (computer science)"), using `if` and `goto`.

The [semantics](/wiki/Semantics_(computer_science) "Semantics (computer science)") article describes several mathematical/logical formalisms which have been used to specify semantics in a precise way; these are generally more complicated than BNF, and no single approach is generally accepted as the way to go. Some approaches effectively define an interpreter for the language, some use formal logic to reason about a program, some attach affixes to syntactic entities to ensure consistency, etc.

Expressions
-----------

[[edit](/w/index.php?title=Statement_(computer_science)&action=edit&section=9 "Edit section: Expressions")]

A distinction is often made between statements, which are executed, and [expressions](/wiki/Expression_(computer_science) "Expression (computer science)"), which are evaluated. Expressions always evaluate to a value, which statements do not. However, expressions are often used as part of a larger statement.

In most programming languages, a statement can consist of little more than an expression, usually by following the expression with a statement terminator (semicolon). In such a case, while the expression evaluates to a value, the complete statement does not (the expression's value is discarded). For instance, in C, C++, C#, and many similar languages, `x = y + 1` is an expression that will set x to the value of y plus one, and the whole expression itself will evaluate to the same value that x is set to. However, `x = y + 1;` (note the semicolon at the end) is a statement that will still set x to the value of y plus one because the expression within the statement is still evaluated, but the result of the expression is discarded, and the statement itself does not evaluate to any value.[[10]](#cite_note-10)

Expressions can also be contained within other expressions. For instance, the expression `x = y + 1` contains the expression `y + 1`, which in turn contains the values `y` and `1`, which are also technically expressions.

Although the previous examples show assignment expressions, some languages do not implement assignment as an expression, but rather as a statement. A notable example of this is [Python](/wiki/Python_(Programming_Language) "Python (Programming Language)"), where = is not an operator, but rather just a separator in the assignment statement. Although Python allows multiple assignments as each assignment were an expression, this is simply a special case of the assignment statement built into the language grammar rather than a true expression.[[11]](#cite_note-11)

Extensibility
-------------

[[edit](/w/index.php?title=Statement_(computer_science)&action=edit&section=10 "Edit section: Extensibility")]

Most languages have a fixed set of statements defined by the language, but there have been experiments with [extensible languages](/wiki/Extensible_languages "Extensible languages") that allow the programmer to define new statements.

See also
--------

[[edit](/w/index.php?title=Statement_(computer_science)&action=edit&section=11 "Edit section: See also")]

* [Comparison of programming languages (syntax) § Statements](/wiki/Comparison_of_programming_languages_(syntax)#Statements "Comparison of programming languages (syntax)")
* [Control flow](/wiki/Control_flow "Control flow")
* [Command (computing)](/wiki/Command_(computing) "Command (computing)")

References
----------

[[edit](/w/index.php?title=Statement_(computer_science)&action=edit&section=12 "Edit section: References")]

1. **[^](#cite_ref-1)** ["statement"](http://www.webopedia.com/TERM/S/statement.html). webopedia. September 1996. Retrieved 2015-03-03.
2. **[^](#cite_ref-CommonBase_2-0)** 
   [Dahl, Ole-Johan](/wiki/Ole-Johan_Dahl "Ole-Johan Dahl"); Myhrhaug, Bjørn; [Nygaard, Kristen](/wiki/Kristen_Nygaard "Kristen Nygaard") (1970). [Common Base Language](https://web.archive.org/web/20240919044713/https://www.softwarepreservation.org/projects/ALGOL/manual/Simula-CommonBaseLanguage.pdf) (PDF) (Report). Norwegian Computing Center. Archived from the original on 2024-09-19. Retrieved 20 August 2025.
3. **[^](#cite_ref-ALGOL60_3-0)** Backus, J.W.; Bauer, F.L.; Green, J.; Katz, C.; McCarthy, J.; Naur, P.; Perlis, A.J.; Rutishauser, H.; Samuelson, K.; Vauquois, B.; Wegstein, J.H.; van Wijngaarden, A.; Woodger, M. Naur, Peter (ed.). ["Revised Report on the Algorithmic Language Algol 60"](https://www.masswerk.at/algol60/report.htm). *mass:werk*. Section "4.1". Retrieved January 23, 2021.
4. **[^](#cite_ref-ALGOL60RPT_4-0)** Backus, J.W.; Bauer, F.L.; Green, J.; Katz, C.; McCarthy, J.; Naur, P.; Perlis, A.J.; Rutishauser, H.; Samuelson, K.; Vauquois, B.; Wegstein, J.H.; van Wijngaarden, A.; Woodger, M. Naur, Peter (ed.). ["Revised Report on the Algorithmic Language Algol 60"](https://www.masswerk.at/algol60/report.htm). *mass:werk*. Section "1.1". Retrieved January 23, 2021.
5. **[^](#cite_ref-FORTRAN66_5-0)** ["FORTRAN"](https://wg5-fortran.org/ARCHIVE/Fortran66.pdf) (PDF). United States of America Standards Institute. 1966. Retrieved February 19, 2021 – via WG5 Fortran Standards.
6. **[^](#cite_ref-FORTRAN95_6-0)** ["Working draft J3/04-007"](https://j3-fortran.org/doc/year/04/04-007.pdf) (PDF). J3 Fortran. May 10, 2004. Retrieved February 19, 2021.
7. **[^](#cite_ref-COBOL1959_7-0)** ["ASCII COBOL Programming Reference Manual"](https://public.support.unisys.com/2200/docs/CP18.0/PDF/78307709-002.pdf) (PDF). unisys. June 2010. Retrieved January 23, 2021.
8. **[^](#cite_ref-PASCAL_8-0)** Jensen, Kathleen; Wirth, Niklaus (1974). Goos, G.; Hartmanis, J. (eds.). ["PASCAL User Manual and Report"](http://prog.vub.ac.be/~tjdhondt/ESL/Pascal_files/PASCAL%20user%20manual%20and%20report.pdf) (PDF). *Lecture Notes in Computer Science*. Appendix D. Retrieved February 19, 2021.
9. **[^](#cite_ref-Trouble_9-0)** Knuth, D. E. (Jul 1967). ["The Remaining Trouble Spots in Algol 60"](https://people.eecs.berkeley.edu/~necula/Papers/KnuthTroubleAlgol.pdf) (PDF). *The ALGOL Family*. Retrieved February 24, 2021.
10. **[^](#cite_ref-10)** ["ISO/IEC 9899:1999 (E)"](https://www.dii.uchile.cl/~daespino/files/Iso_C_1999_definition.pdf) (PDF). *ISO/IEC*. [Archived](https://web.archive.org/web/20240207035551/http://www.dii.uchile.cl/~daespino/files/Iso_C_1999_definition.pdf) (PDF) from the original on Feb 7, 2024.
11. **[^](#cite_ref-11)** ["7. Simple statements"](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements). *Python 3.10.8 documentation*.

External links
--------------

[[edit](/w/index.php?title=Statement_(computer_science)&action=edit&section=13 "Edit section: External links")]

* [PC ENCYCLOPEDIA: Definition of: program statement](https://www.pcmag.com/encyclopedia/term/program-statement)

|  |  |
| --- | --- |
| [Authority control databases](/wiki/Help:Authority_control "Help:Authority control") [Edit this at Wikidata](https://www.wikidata.org/wiki/Q613299#identifiers "Edit this at Wikidata") | * [GND](https://d-nb.info/gnd/4458688-7) |

![](https://en.wikipedia.org/wiki/Special:CentralAutoLogin/start?useformat=desktop&type=1x1&usesul3=1)

Retrieved from "<https://en.wikipedia.org/w/index.php?title=Statement_(computer_science)&oldid=1341072797>"

[Categories](/wiki/Help:Category "Help:Category"):

* [Programming language concepts](/wiki/Category:Programming_language_concepts "Category:Programming language concepts")
* [Statements](/wiki/Category:Statements "Category:Statements")

Hidden categories:

* [CS1: unfit URL](/wiki/Category:CS1:_unfit_URL "Category:CS1: unfit URL")
* [Articles with short description](/wiki/Category:Articles_with_short_description "Category:Articles with short description")
* [Short description is different from Wikidata](/wiki/Category:Short_description_is_different_from_Wikidata "Category:Short description is different from Wikidata")
* [All Wikipedia articles needing clarification](/wiki/Category:All_Wikipedia_articles_needing_clarification "Category:All Wikipedia articles needing clarification")
* [Wikipedia articles needing clarification from December 2025](/wiki/Category:Wikipedia_articles_needing_clarification_from_December_2025 "Category:Wikipedia articles needing clarification from December 2025")

* This page was last edited on 1 March 2026, at 07:32 (UTC).
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
* [Mobile view](//en.wikipedia.org/w/index.php?title=Statement_(computer_science)&mobileaction=toggle_view_mobile)

* [![Wikimedia Foundation](/static/images/footer/wikimedia.svg)](https://www.wikimedia.org/)
* [![Powered by MediaWiki](/w/resources/assets/mediawiki_compact.svg)](https://www.mediawiki.org/)

Search

Search

Toggle the table of contents

Statement (computer science)

25 languages
[Add topic](#)