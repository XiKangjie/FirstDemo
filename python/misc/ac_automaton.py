#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Aho–Corasick string matching algorithm

Reference: http://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_string_matching_algorithm
"""

class ACState():
    def __init__(self, char=None):
        self.goto = {}            # {char: ACState, ...}
        self.failure = None
        self.output = None
        self.keyword_index = -1   # keyword index in keyword table


class ACAutomaton():
    def __init__(self):
        self.root = ACState()
        self.keyword_table = []

    def add_keyword(self, keyword):
        """
        add keyword to keyword_table
        """
        self.keyword_table.append(keyword)

    def build_goto(self):
        for index, keyword in enumerate(self.keyword_table):
            state = self.root
            for c in keyword:
                if c not in state.goto:
                    state.goto[c] = ACState(c)
                state = state.goto[c]
            state.keyword_index = index

    def build_failure_output(self):
        """
        build failure table
        """
        queue = []
        queue.append(self.root)
        while queue:
            parent = queue.pop(0)
            for char, child in parent.goto.items():
                failure = parent.failure
                while failure and char not in failure.goto:
                    failure = failure.failure
                child.failure = failure.goto[char] if failure else self.root
                
                output = child.failure
                while output:
                    if output.keyword_index != -1:
                        child.output = output
                        break
                    output = output.failure

                queue.append(child)

    def build(self):
        self.build_goto()
        self.build_failure_output()

    def search(self, text):
        for i, c in enumerate(text):
            print 
        state = self.root
        for i, c in enumerate(text):
            while state and c not in state.goto:
                state = state.failure
            state = state.goto[c] if state else self.root
            if state.keyword_index != -1:
                print self.keyword_table[state.keyword_index]
            output = state.output
            while output:
                print self.keyword_table[output.keyword_index]
                output = output.output


if __name__ == '__main__':
    ac = ACAutomaton()
    for keyword in ['a', 'ab', 'bab', 'bc', 'bca', 'c', 'caa']:
        ac.add_keyword(keyword)
    ac.build()
    ac.search('abccab')

    print
    ac = ACAutomaton()
    for keyword in ['bca', 'ca', 'a']:
        ac.add_keyword(keyword)
    ac.build()
    ac.search('bca')
