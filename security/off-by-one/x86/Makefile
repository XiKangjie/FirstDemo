all: vuln

vuln: vuln.c
	gcc -g -fno-stack-protector -z execstack -mpreferred-stack-boundary=2 -o vuln vuln.c
	sudo chown root vuln
	sudo chgrp root vuln
	sudo chmod +s vuln

clean:
	rm vuln
