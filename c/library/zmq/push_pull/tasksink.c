/* Task sink
 * Binds PULL socket to tcp://localhost:5558
 * Collects results from workers via that socket
 */

#include "../zhelpers.h"

int main()
{
    void* context = zmq_ctx_new();
    void* receiver = zmq_socket(context, ZMQ_PULL);
    zmq_bind(receiver, "tcp://*:5558");
    
    /* Wait for start of batch */
    char* string = s_recv(receiver);
    printf("start of batch.\n");
    free(string);

    int64_t start_time = s_clock();

    int task_nbr;
    for(task_nbr = 0; task_nbr < 100; task_nbr++) {
        char* string = s_recv(receiver);
        free(string);
        if((task_nbr / 10) * 10 == task_nbr) {
            printf(":");
        }
        else {
            printf(".");
        }
        fflush(stdout);
    }
    printf("\nTotal elapsed time: %d msec\n", (int)(s_clock() - start_time));

    zmq_close(receiver);
    printf("receiver closed.\n");
    zmq_ctx_destroy(context);
    printf("context destroyed.\n");

    return 0;
}
