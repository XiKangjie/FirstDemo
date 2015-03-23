#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Aho–Corasick string matching algorithm

Reference: http://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_string_matching_algorithm
"""
from collections import defaultdict

class ACState():
    def __init__(self):
        self.goto          = {}            # {char: ACState, ...}
        self.failure       = None
        self.output        = None
        self.keyword_index = -1            # keyword index in keyword table


class ACAutomaton():
    def __init__(self):
        self.root = ACState()


    def build_goto(self, keyword_table):
        """
        build goto table, that's trie tree.
        """
        for index, keyword in enumerate(keyword_table):
            state = self.root
            for c in keyword:
                if c not in state.goto:
                    state.goto[c] = ACState()
                state = state.goto[c]
            state.keyword_index = index

    def build_failure_output(self):
        """
        build failure and output table
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
                while output and output.keyword_index == -1:
                    output = output.failure
                child.output = output

                queue.append(child)

    def build(self, keyword_table):
        self.build_goto(keyword_table)
        self.build_failure_output()

    def search(self, text):
        """
        search keywords in text
        return a match dict,
        key = index of char in text,
        value = a list of index of matched keywords in keyword_table
        """
        match = defaultdict(list)
        state = self.root
        for i, c in enumerate(text):
            while state and c not in state.goto:
                state = state.failure
            state = state.goto[c] if state else self.root
            if state.keyword_index != -1:
                match[i].append(state.keyword_index)
            output = state.output
            while output:
                match[i].append(output.keyword_index)
                output = output.output
        return match


if __name__ == '__main__':
    keyword_table = ['a', 'ab', 'bab', 'bc', 'bca', 'c', 'caa']
    text = 'abccab'
    
    print 'keywords table:'
    for i, k in enumerate(keyword_table):
        print i, k
    print '\ntext: ', text
    
    ac = ACAutomaton()
    ac.build(keyword_table)
    match = ac.search(text)
    
    print '\nmatched:'
    for i in match:
        print i,
        for index in match[i]:
            print keyword_table[index],
        print


"""
keywords table:
0 a
1 ab
2 bab
3 bc
4 bca
5 c
6 caa

text:  abccab

matched:
0 a
1 ab
2 bc c
3 c
4 a
5 ab
"""
