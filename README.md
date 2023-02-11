## Prerequisites
Python3 and Pip

make sure `python3` and `pip` command can found in PATH. 

## Installation and run
1. `git clone <this repo>` or download zip and extract it
1. `cd <local repo>`
1. `python3 -m venv venv`
1. enter venv, for example: `source venv/bin/activate.fish`
1. `pip install -r requirements.txt`
1. `./images2pdf.py <txt file path>`

## Example

Assume there has a text file `images.txt`, it's content like this:
```
/path/to/a.jpg
/path/to/b.jpg
/path/to/c.jpg
```

Then run this command:
`./images2pdf images.txt`

It will produce a pdf file named `images.pdf` in current directory.
