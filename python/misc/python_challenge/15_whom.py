import calendar

for year in range(1000, 2000):
	if calendar.weekday(year, 1, 27) == 1 and calendar.isleap(year):
		if str(year).startswith('1') and str(year).endswith('6'):
			print(year)

# 1176
# 1356
# 1576
# 1756		# second
# 1976

# 1756.1.27 is birthday of Mozart