OMEN: Ordered Markov ENumerator
================================

OMEN is a Markov model-based password guesser written in C. It generates password candidates according to their occurrence probabilities, i.e., it outputs most likely passwords first. OMEN significantly improves guessing speed over existing proposals.
If you are interested in the details on how OMEN improves on existing Markov model-based password guessing approaches, please refer to [OMEN: Faster Password Guessing Using an Ordered Markov Enumerator](https://hal.archives-ouvertes.fr/hal-01112124/file/omen.pdf).

User Guide
-----------

OMEN consists of two separate program modules: `createNG` and `enumNG`. `createNG`
calculates n-gram probabilities based on a given list of passwords and stores them
on the hard disk. Based on these probabilities `enumNG` enumerates new
passwords in the correct order (descending).

### Installation

Check out the source code via:

`$ git clone https://github.com/RUB-SysSec/OMEN.git OMEN`

Change into the newly created directory `OMEN` and run:

`$ make`

If compilation is successful, you can find `createNG` and `enumNG` within the current directory.

```
.
├── alphabetCreator
├── createNG
├── docs
│   ├── CHANGELOG.md
│   ├── LICENSE
│   └── screenshots
├── enumNG
├── evalPW
├── makefile
├── README.md
└── src
    ├── alphabetCreator.c
    ...
```

If you like, you can now remove the `src` folder and the `makefile` file, they are no longer used.

### Basic Usage

Before one can generate any passwords, the n-gram probabilities have to be estimated using
`createNG`. To calculate the probabilities using the default settings, `createNG` must be
called giving a path to a password list that should be trained:

`$ ./createNG --iPwdList password-training-list.txt`

Each password of the given list must be in a new line. The module then
reads and evaluates the list generating a couple of files. Besides a config file (`createConfig`) storing the used settings (in this case the default setting), several files are created containing information about the grams and the password length. These files have the extension '`.level`':

* **IP.level** (Initial Probability): Stores the probabilities of the first
(n-1)-gram of each password.
* **CP.level** (Conditional Probability): Stores the probabilities of the actual
n-grams.
* **EP.level** (End Probability): Stores the probabilities of the last (n-1)-gram
of each password.
* **LN.level** (Length): Stores the probabilities for the password length.

The probabilities of each n-gram and the lengths are mapped to levels between 0
(most likely) and 10 (least likely). Once those files are created, `enumNG` can
be used to generate a list of passwords ordered by probabilities. Currently, `enumNG` supports three modes of operation: *file*, *stdout*, *simulated plaintext attack*. In the default mode of `enumNG`, a list of password guesses based on these levels is created. Using the command

`$ ./enumNG`

generates 1 billion passwords and **stores them in a text file**, which can be found
in the '*results*' folder. The passwords in this file are ordered by level (i.e., by
probability). Since common text editors are not able to handle such huge files,
it is recommended for testing to reduce the number of passwords created. This
can be done using the argument `-m`.

`$ ./enumNG -m 10000`

It will create an ordered list with 10,000 passwords only. If you are interested in printing the passwords to the **standard output (stdout) stream** use the argument `-p`.

`$ ./enumNG -p -m 10000`

If you are interested in evaluating the guessing performance against a *plaintext* password test set use the argument `-s`. Please note: In this mode OMEN benefits from the adaptive length scheduling algorithm incorporating live feedback, which is not available (due to the missing feedback channel) in *file* and *stdout* mode.

`$ ./enumNG -s=password-testing-list.txt -m 10000`

The result of this evaluation can be found in the '*results*' folder.

Both modules provide a help dialog which can be shown using the `-h` or `--help` argument.

### Advanced Usage

Both modules provide several command line arguments to select the various
modes available and change the default settings. For instance, the probability
distribution created during the `createNG` process may be manipulated by
choosing one of the supported smoothing functions, the n-gram size, or the used
alphabet. All available parameters for `createNG`, a short description, and the default values can be seen by calling the program with `-h` or `--help`. The same works for `enumNG` where for instance, the enumeration mode, the used length scheduling algorithm (only used in `-s` mode, see '*Basic Usage*' section), and the maximum amount of attempts can be selected. If no enumeration mode is given, the
default mode is executed, storing all created passwords in a text file in the
'*results*' folder.

OMEN+
-----

OMEN+ is based on [When Privacy Meets Security: Leveraging Personal Information for Password Cracking](https://arxiv.org/pdf/1304.6584.pdf)
and is an additional feature of OMEN (implemented in the same binary). Using additional personal information about a user (e.g., a password hint or personal background information scraped from a social network) may help in speeding up the password guessing process (comparable to John the Ripper '*Single crack*' mode).


Therefore, a related hint or several hints (tabulator separated) must be provided in a separate file. Furthermore, an alpha file is required containing the respective
alpha values (tab separated in one line). Alpha values are used to weight the impact of the provided hints. Important is that for each hint in a
line an alpha has to be specified in the alpha file. These alphas have to be in
the same order as the hints per line.

Exemplary, we want to guess the password "*Mary'sPW2305*". The
corresponding line in the hint file containing *first name*, *username*, *date of
birth*, and *email address* looks like the following:

```
mary   mary1   19880523    mary1@yahoo.com
```

An alpha file should order the related alpha values for *first name*, *username*,
*date of birth*, and *email address* in the same order as in the hint file. In
example:

```
1   2   1   2
```

For the usage of OMEN+ `enumNG` must be called giving a path to a hint and an
alpha file:

`$ ./enumNG -H hint-file.txt -a alpha-file.txt`

Performance
-----------
![OMEN](/docs/screenshots/performance.png?raw=true "OMEN")

FAQ
---

* Very poor performance and strange looking passwords?
Make sure you generated the alphabet file with the `alphabetCreator`. Manually generating the alphabet is not supported (see [Issue#4](https://github.com/RUB-SysSec/OMEN/issues/4)).
