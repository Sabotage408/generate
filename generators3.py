#!/usr/bin/env python3

class generates:
    def __init__(self, sause_range):
        self.sause_range = sause_range
        
    def hottest_sauce(self):
        #print(self.sause_range)
        for n in list(self.sause_range):
            yield n + 1
        

gen = generates(sause_range=range(0, 10))

print(gen.hottest_sauce())

for item in gen.hottest_sauce():
    print(item)
