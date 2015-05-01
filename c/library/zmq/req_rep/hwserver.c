/* Hello World server
 * If you kill the server(Ctrl-C) and restart it, the client won't recover properly.
 * Recovering from crashing processes isn't quite that easy.
 * Making a reliable request-reply flow is complex.
 */

#include <zmq.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <assert.h>

int main()
{
	void* context = zmq_ctx_new();
	void* responder = zmq_socket(context, ZMQ_REP);
	int rc = zmq_bind(responder, "tcp://*:5555");
	assert(rc == 0);

	while(1) {
		char buffer[10];
		zmq_recv(responder, buffer, 10, 0);
		printf("Received Hello\n");
		sleep(1);
		zmq_send(responder, "World", 5, 0);
	}

	return 0;
}
