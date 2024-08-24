#  Code Lines Counter

Just a code lines counter

## Installation

 1. Clone this repo

```sh
git clone https://www.github.com/victorzhamval/code-lines-counter
```
2. Install packages

```sh
pip install -r requirements.txt
```

## Usage

<b>Count from a single file:</b>
```sh
python3 code-lines-counter -f example.py
```
or:

```sh
python3 code-lines-counter --file example.py
```

<b>Count from multiple files:</b>
```sh
python3 code-lines-counter -f example.py -f example.js --file example2.txt
```

<b>Count from a directory:</b>
```sh
python3 code-lines-counter -d example-dir
```

or:

```sh
python3 code-lines-counter --directory example-dir
```

# License
MIT