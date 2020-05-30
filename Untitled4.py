#!/usr/bin/env python3

class generate: 
    def __init__(self, the_range):
        self.the_range = the_range
        
    def do_the_work(self):
        print(self.the_range)
        
        
        
gen = generate(the_range=range(0, 10))

gen.do_the_work()