/* Task ventilator
 * Binds PUSH socket to tcp://localhost:5557
 * Sends batch of tasks to workers via that socket
 */

#include "../zhelpers.h"

int main()
{
    void* context = zmq_ctx_new();

    /* Socket to send message on */
    void* sender = zmq_socket(context, ZMQ_PUSH);
    zmq_bind(sender, "tcp://*:5557");
    /* Socket to send start of batch message on */
    void* sink = zmq_socket(context, ZMQ_PUSH);
    zmq_connect(sink, "tcp://localhost:5558");

    printf("Press Enter when the workers are ready: ");
    getchar();
    printf("Sending tasks to workres...\n");

    /* The first message is "0" and signals start of batch */
    s_send(sink, "0");
    printf("start of batch.\n");
    /* Initialize random number generator */
    srandom((unsigned)time(NULL));

    int task_nbr;
    int total_msec = 0;
    for(task_nbr = 0; task_nbr < 100; task_nbr++) {
        int workload;
        workload = randof(100) + 1;
        total_msec += workload;
        char string[10];
        sprintf(string, "%d", workload);
        s_send(sender, string);
        printf("%s.", string);
    }
    printf("\nTotal expected cost: %d msec\n", total_msec);

    zmq_close(sink);
    printf("sink closed.\n");
    zmq_close(sender);
    printf("sender closed.\n");
    zmq_ctx_destroy(context);
    printf("context destroyed.\n");

    return 0;
}
