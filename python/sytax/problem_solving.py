# ****************************************************************** #
# ************************* Byte of Python ************************* #
# ****************************************************************** #

########################
# backup_ver1
########################
# import os
# import time

# source = '"D:\\Work\\Develop\\PythonLearning\\base\\backup source"'

# target_dir = '"D:\\Work\\Develop\\PythonLearning\\base\\backup target"'

# target = target_dir + os.sep + time.strftime("%Y%m%d%H%M%S") + ".zip"

# zip_command = "zip -qr {0} {1}".format(target, source)

# print(zip_command)

# if os.system(zip_command) == 0:
# 	print("Successful backup to", target)
# else:
# 	print("Backup FAILED")


########################
# backup_ver2
########################
# import os
# import time

# source = r"D:\Work\Develop\PythonLearning\base\backup source"
# target_dir = r"D:\Work\Develop\PythonLearning\base\backup target"

# # today = '"{0}"'.format(target_dir + os.sep + time.strftime("%Y%m%d"))
# today = target_dir + os.sep + time.strftime("%Y%m%d")
# now = time.strftime("%H%M%S")

# # print(today)
# if not os.path.exists(today):
# 	os.mkdir(today)
# 	print("Sucessfully created directory", today)

# target = today + os.sep + now + ".zip"

# # print(target)
# # print(source)
# zip_command = 'zip -r "{0}" "{1}"'.format(target, source)

# # print(zip_command)
# if os.system(zip_command) == 0:
# 	print("Successful backup to", target)
# else:
# 	print("Backup FAILED")


########################
# backup_ver3
########################
import os
import time

source = r"D:\Work\Develop\PythonLearning\base\backup source"
target_dir = r"D:\Work\Develop\PythonLearning\base\backup target"

today = target_dir + os.sep + time.strftime("%Y%m%d")
now = time.strftime("%H%M%S")

comment = input("Enter a comment --> ")
if len(comment) == 0:
	target = today + os.sep + now + ".zip"
else:
	target = today + os.sep + now + "_" + comment.replace(" ", "_") + ".zip"

if not os.path.exists(today):
	os.mkdir(today)
	print("Successfully created directory", today)

zip_command = 'zip -r "{0}" "{1}"'.format(target, source)

if os.system(zip_command) == 0:
	print("Successful backup to", target)
else:
	print("Backup FAILED")
