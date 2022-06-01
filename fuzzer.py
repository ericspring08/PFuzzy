import random
import string
import sys
import os
import sys
# add any imports or functions that will be used for testing here
import wikipedia
from art import *
#---------------------------------------------------


class Fuzzer:
    def __init__(self) :
        tprint("PFUZZY")
        self.crashes = 0
        self.total = 0
        self.crash_types = []

    def run_test(self,function_to_run, data) :
        try:
            with HiddenPrints():
                eval(f"{function_to_run}({data})")
            return "succesful"
        except Exception as e :
            return e
    def convert_to_param(self, params) :
        s = ""

        for i in range(len(params)):
            if params[i] == "String":
                s += self.generate_random_string()
            if params[i] == "Integer":
                s += str(random.randint(-10000, 10000))
            if params[i] == "Boolean":
                s += str(random.choice([True, False]))
            if i != len(params) - 1:
                s += ", "
        return s

    def fuzz(self, function_to_run, parameters, rounds) :
        print("----------------------------")
        print("Function: " + function_to_run)
        for i in range(rounds) :
            result = self.run_test(function_to_run, self.convert_to_param(parameters))
            self.total += 1
            if(result != "succesful"):
                self.crashes += 1
                if(result not in self.crash_types) :
                    self.crash_types.append(result)
            self.drawProgressBar((i+1)/rounds)

        print("\n")
        print("Total Runs: " + str(self.total))
        print("Crashes: " + str(self.crashes))
        print("Crash Percentage: " + str((self.crashes/self.total) * 100) + "%")
        print("----------------------------")

    def print_crash_logs(self):
        print("Crashes: " + str(self.crash_types))

    def get_report(self):
        print("----------------------------")
        print("Total Runs: " + str(self.total))
        print("Crashes: " + str(self.crashes))
        print("Crash Percentage: " + str((self.crashes/self.total) * 100) + "%")
        print("----------------------------")
    
    def generate_random_string(self) :
        s = '"'
        for i in range(random.randint(0, 1000)):
            s += random.choice(string.ascii_letters)
        s+= '"'
        return s

    def reset_crashes(self):
        self.crashes = 0
        self.total = 0

    def drawProgressBar(self, percent, barLen = 20):
        # percent float from 0 to 1. 
        sys.stdout.flush()
        sys.stdout.write("[{:<{}}] {:.0f}%".format("#" * int(barLen * percent), barLen, percent * 100))
        sys.stdout.write("\r")

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout 