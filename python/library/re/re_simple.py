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
