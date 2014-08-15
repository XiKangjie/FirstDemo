def say(s):
	ret = ''
	i = j = 0
	while(j < len(s)):
		if s[j] != s[i]:
			ret += str(j - i) + s[i]
			i = j
		j += 1
	else:
		ret += str(j - i) + s[i]
	return ret

a = ['1']
for n in range(1, 31):
	a.append(say(a[n - 1]))
#print(a)
print(len(a[30]))	# 5808