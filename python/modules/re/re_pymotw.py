import re

# Finding Patterns in Text

patterns = ['this', 'that']
text = 'Does this text match the patterns'

for pattern in patterns:
    print 'Looking for "%s" in "%s" ->' % (pattern, text),
    if re.search(pattern, text):
        print 'found a match'
    else:
        print 'no match'

'''
Looking for "this" in "Does this text match the patterns" -> found a match
Looking for "that" in "Does this text match the patterns" -> no match
'''

pattern = 'this'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print 'Found "%s" in "%s" from %d to %d (%s)' % \
        (match.re.pattern, match.string, s, e, text[s:e])
'''
Found "this" in "Does this text match the patterns" from 5 to 9 (this)
'''

# Multiple Matches

text = 'abbaaabbbbaaaaa'
pattern = 'ab'
# findall() returns all matched substrings
for match in re.findall(pattern, text):
    print 'Found "%s"' % match
'''
Found "ab"
Found "ab"
'''

# finditer() returns an iterator that produces Match
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print 'Found "%s" at %d:%d' % (match.re.pattern, s, e)
'''
Found "ab" at 0:2
Found "ab" at 5:7
'''

# Compiling Expressions
# return a RegexObject
regex = re.compile('this')
text = 'Does this text match the pattern?'
print 'Looking for "%s" in "%s" ->' % (regex.pattern, text)
if regex.search(text):
    print 'found a match!'
else:
    print 'no match'

# Repetition
text = 'abbaaabbbbaaaaa'
# greedy
match = re.search('ab*', text)
print text[match.start() : match.end()]
# abb

# greedines can be turned off by following the repetition instruction with ?
match = re.search('ab*?', text)
print text[match.start() : match.end()]
# a

def test_patterns(text, patterns = []):
    print text
    for pattern in patterns:
        print 'Matching "%s"' % pattern
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            print ' %2d : %2d = %s' % (s, e - 1, text[s:e])

# Anchoring
test_patterns('This is some text -- with punctuation.',
                [r'^\w+',    # word at start of string
                 r'\w+\S*$', # word at end of string, with optional punctuation
                 r'\bt\w+',  # 't' at start of word
                 r'\w+t\b'   # 't' at end of word
                 ])

'''
This is some text -- with punctuation.
Matching "^\w+"
  0 :  3 = This
Matching "\w+\S*$"
 26 : 37 = punctuation.
Matching "\bt\w+"
 13 : 16 = text
Matching "\w+t\b"
 13 : 16 = text
'''
