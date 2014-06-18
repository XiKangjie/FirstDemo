import time

# timestamp
print(time.time())

# timestamp -> struct_time
print(time.localtime())

# struct_time -> strftime
print(time.strftime("%Y-%m-%d	%H:%M:%S"))

#time.sleep(2)

# struct_time -> strftime
print(time.strftime("%Y-%m-%d	%H:%M:%S", time.localtime(1400580394)))