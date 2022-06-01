# PFuzzy
A simple fuzzer built in python for testing functions. 

## How to run
1. Clone the repo by running "git clone https://github.com/ericspring08/PFuzzy.git"
2. Run main.py which utilizes the Fuzzer class in fuzzer.py

## How to use the Fuzzer Class
### Create a new Fuzzer
```python
my_fuzzer = Fuzzer() 
```
### Create a target function to test
first import target function into the fuzzer.py file
```python
my_fuzzer.fuzz('[function name *no parenthesis)], [parameter types], [# of rounds])
```
### Get crash report
```python
my_fuzzer.get_report() 
```
### Get crash logs
``` python
my_fuzzer.print_crash_logs() 
```
### Reset the crash and total run count
```python
my_fuzzer.reset_crashes() 
```

### Example code
main.py
```python
my_fuzzer = new Fuzzer()
my_fuzzer.fuzz('my_function', ["String", "Integer"], 10)
my_fuzzer..print_crash_logs()
```
fuzzer.py
```python
import ... 

# add any imports or functions that will be used for testing here
import wikipedia #example import

def my_function(my_string, my_integer):
  #code in your function
#---------------------------------------------------

class Fuzzer :
  #fuzzer class
```
