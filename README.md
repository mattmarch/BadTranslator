# Bad Translator

A quick tool for translating an input file from English between multiple languages and back to English using Google Translate (via the unofficial googletrans Python API).

## Requirements
- Python 3.7
- virtualenv (`pip install virtualenv`)

## Setup
- Clone directory
- Create virtualenv e.g. `virtualenv --python=/usr/bin/python3.7 venv`
- Activate `source venv/bin/activate`
- Install requirements `pip install -r requirements.txt`

# Run
`python translator.py inputfile times`

e.g. `python translator.py frozen.txt 5` to translate the file *frozen.txt* 5 times. The output will be printed to the console.

**Probably don't set the number too high or else you might upset Google.**
