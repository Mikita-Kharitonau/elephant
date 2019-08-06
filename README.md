# elephant

Workflow application.

## How to run?
```
$ git clone https://github.com/Mikita-Kharitonau/elephant.git
$ cd elephant
$ source venv/bin/activate
$ python main.py input output
```
For example:

input.txt
```
C 25 7
L 4 2 6 2
L 2 2 2 6
R 16 1 20 3
R 5 4 20 6
B 19 2 %
B 10 5 %
B 1 1 1
```

running
```
$ python main.py -h
usage: main.py [-h] input output

Elephant application.

positional arguments:
  input       Path to input file.
  output      Path to output file.

optional arguments:
  -h, --help  show this help message and exit

$ python main.py input.txt output.txt
```

will create output.txt file with the following content:
```
---------------------------
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
|                         |
---------------------------
---------------------------
|                         |
|   xxx                   |
|                         |
|                         |
|                         |
|                         |
|                         |
---------------------------
---------------------------
|                         |
| x xxx                   |
| x                       |
| x                       |
| x                       |
| x                       |
|                         |
---------------------------
---------------------------
|               xxxxx     |
| x xxx         x   x     |
| x             xxxxx     |
| x                       |
| x                       |
| x                       |
|                         |
---------------------------
---------------------------
|               xxxxx     |
| x xxx         x   x     |
| x             xxxxx     |
| x  xxxxxxxxxxxxxxxx     |
| x  x              x     |
| x  xxxxxxxxxxxxxxxx     |
|                         |
---------------------------
---------------------------
|               xxxxx     |
| x xxx         x%%%x     |
| x             xxxxx     |
| x  xxxxxxxxxxxxxxxx     |
| x  x              x     |
| x  xxxxxxxxxxxxxxxx     |
|                         |
---------------------------
---------------------------
|               xxxxx     |
| x xxx         x%%%x     |
| x             xxxxx     |
| x  xxxxxxxxxxxxxxxx     |
| x  x%%%%%%%%%%%%%%x     |
| x  xxxxxxxxxxxxxxxx     |
|                         |
---------------------------
---------------------------
|111111111111111xxxxx11111|
|1x1xxx111111111x%%%x11111|
|1x1111111111111xxxxx11111|
|1x11xxxxxxxxxxxxxxxx11111|
|1x11x%%%%%%%%%%%%%%x11111|
|1x11xxxxxxxxxxxxxxxx11111|
|1111111111111111111111111|
---------------------------
```

> Note, that **incorrect instructions would be skipped**.

## How to test?

```
$ cd elephant
$ python -m unittest discover test/ -v
```

Please, fill free to write review to nikita.kharitonov99@gmail.com

