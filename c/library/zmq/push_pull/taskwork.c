/* Task worker
 * Connects PULL socket to tcp://localhost:55557
 * Collects workloads from ventilator via that socket
 * Connects PUSH socket to tcp://localhost:5558
 * Sends results to sink via that socket
 */

#include "../zhelpers.h"

int main()
{
    /* Socket to receive message on */
    void* context = zmq_ctx_new();
    void* receiver = zmq_socket(context, ZMQ_PULL);
    zmq_connect(receiver, "tcp://localhost:5557");
    /* Socket to send message to */
    void* sender = zmq_socket(context, ZMQ_PUSH);
    zmq_connect(sender, "tcp://localhost:5558");

    while(1) {
        char* string = s_recv(receiver);
        printf("%s.", string);
        fflush(stdout);
        s_sleep(atoi(string));
        free(string);
        s_send(sender, "");
    }

    zmq_close(receiver);
    printf("receiver closed.\n");
    zmq_close(sender);
    printf("sender closed.\n");
    zmq_ctx_destroy(context);
    printf("context destroyed.\n");

    return 0;
}
