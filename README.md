OMEN: Ordered Markov ENumerator
================================

OMEN is a Markov model-based password guesser written in C. It generates password candidates according to their occurrence probabilities, i.e., it outputs most likely passwords first. OMEN significantly improves guessing speed over existing proposals.

User Guide
-----------

OMEN consists of two separate program modules: `createNG` and `enumNG`. `createNG`
calculates n-gram probabilities based on a given list of passwords and stores them
on the hard disk. Based on these probabilities `enumNG` enumerates new
passwords in the correct order (descending).

### Installation

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

`$ ./createNG --iPwdList=password-training-list.txt`

## After the probabilities of n-gram characters are calculated run the script.py file by executing the following command

`$ python3 script.py <min_characters:int> <max_characrers:int>`

### Here the min_characters and max_characters are the length of passwords you wish to generate.


### The generated passwords can be viewed inside the folder titled 'results'.
