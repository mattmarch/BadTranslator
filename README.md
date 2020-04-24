# Bad Translator

A quick tool for translating an input file from English between multiple languages and back to English using Google Translate (via the unofficial googletrans Python API).

Created to easily generate pub quiz questions.

## Requirements
- Python 3.7
- virtualenv (`pip install virtualenv`) *OPTIONAL*

## Setup
- Clone repository 
  - `git clone git@github.com:mattmarch/BadTranslator.git`
  - `cd BadTranslator`
- *OPTIONAL* Create and activate virtualenv e.g. 
  - `virtualenv --python=/usr/bin/python3.7 venv`
  - `source venv/bin/activate`
- Install requirements `pip install -r requirements.txt`

# Run
`python translator.py inputfile times`

e.g. `python translator.py frozen.txt 5` to translate the file *frozen.txt* 5 times. The output will be printed to the console.

**You probably don't want to set the number too high or else you might upset Google.**
