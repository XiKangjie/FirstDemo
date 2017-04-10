all: vuln integer-overflow

vuln: vuln.c
	gcc -g -fno-stack-protector -z execstack -o vuln vuln.c
	sudo chown root vuln
	sudo chgrp root vuln
	sudo chmod +s vuln

integer-overflow: integer-overflow.c
	gcc -g -o integer-overflow integer-overflow.c

clean:
	rm vuln integer-overflow
