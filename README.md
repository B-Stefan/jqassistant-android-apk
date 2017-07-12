# Android reverse engineer jQAssistant 

This is a simple prototype to run jQAssistant tests on a apk file. 


## Introduction
This script decompiles an apk to its corresponding java jar file and scan this file with jQAssistant. 

 ***This script just automates the sequence in which various tools are initiated and does not handle any error events. You will have to go through the cmd verbose to figure out the problem.***

## Getting started

```
Usage: apk_to_jqassistant.py action ApkFileName [options]

action can  be 'test' (to run the jqassistant tests on the apk) 'server' (stats the neo4j server with the data), analysis (to run just the analysis)
Options:
  -h, --help   show this help message and exit
```

## Requirements

* JRE 1.7 (Java Runtime Environment)
* Python 3


## Tools used

* [Dex2jar](http://code.google.com/p/dex2jar/)
* [jQAssistant](https://jqassistant.org/)

