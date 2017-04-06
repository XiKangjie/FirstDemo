all: vuln

vuln: vuln.c
	gcc -g -fno-stack-protector -z execstack -o vuln vuln.c
	sudo chown root vuln
	sudo chgrp root vuln
	sudo chmod +s vuln

clean:
	rm vuln
