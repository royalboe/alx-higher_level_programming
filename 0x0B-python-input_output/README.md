# 0x0B. Python - Input/Output

## Description
This project is about how to read/write files and working with json files in python

## Table of contents

Files | Description
----------- | -----------
[0-read_file.py](./0-read_file.py) | Function that reads a text file (UTF8) and prints it to stdout: Prototype: def read_file(filename=""):
[1-write_file.py](./1-write_file.py) | Function that writes a string to a text file (UTF8) and returns the number of characters written: Prototype: def write_file(filename="", text=""):
[2-append_write.py](./2-append_write.py) | Function that appends a string at the end of a text file (UTF8) and returns the number of characters added: Prototype: def append_write(filename="", text=""):
[3-to_json_string.py](./3-to_json_string.py) | Function that returns the JSON representation of an object (string): Prototype: def to_json_string(my_obj):
[4-from_json_string.py](./4-from_json_string.py) | Function that returns an object (Python data structure) represented by a JSON string: Prototype: def from_json_string(my_str):
[5-save_to_json_file.py](./5-save_to_json_file.py) | Function that writes an Object to a text file, using a JSON representation: Prototype: def save_to_json_file(my_obj, filename):
[6-load_from_json_file.py](./6-load_from_json_file.py) | Function that creates an Object from a “JSON file”: Prototype: def load_from_json_file(filename)
[7-add_item.py](./7-add_item.py) | A script that adds all arguments to a Python list, and then save them to a file: 
[8-class_to_json.py](./8-class_to_json.py) | Function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object: Prototype: def class_to_json(obj):
[9-student.py](./9-student.py) | A class Student that defines a student by: Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
[10-student.py](./10-student.py) | A class Student that defines a student by: (based on 9-student.py) Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
[11-student.py](./11-student.py) | A class Student that defines a student by: (based on 10-student.py) Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
[12-pascal_triangle.py](./12-pascal_triangle.py) | Function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:
[100-append_after.py](./100-append_after.py) | Function that inserts a line of text to a file, after each line containing a specific string (see example): Prototype: def append_after(filename="", search_string="", new_string=""):
[101-stats.py](./101-stats.py) | A script that reads stdin line by line and computes metrics: Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>


---
## Resources
- [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
- [Dive Into Python 3: Chapter 11. Files](https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)


