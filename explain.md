# File Reading and Writing

## Opening a file
```python
file = open("<path>", "mode")
file.close()
```
[File Modes](https://tutorial.eyehunts.com/python/python-file-modes-open-write-append-r-r-w-w-x-etc/)  
Remember to close the file after opening it


## Reading a file
Open the file in "r" mode and run the .read() function on it
```python
file = open("test.txt", "r")
print(file.read())
file.close()
```

## Writing to a file
Open the file in "w" mode (overwrite) and run .write(\<string\>) with \<string\> being what you want to write
```python
file = open("test.txt", "w")
file.write("Hello World!")
file.close()
```

## Apending to a file
Open the file in "a" mode (append) and run .write(\<string\>) with \<string\> being what you want to append.
```python
file = open("test.txt", "a")
file.write("Hello World!")
file.close()
```

## Extras
A "\\n" in a file, means "new line"
The .strip() method removes trailing whitespace (\\n and spaces)
