/* Weather update client
 * Collects weather updates and finds avg  temp in zipcode.
 */

#include "../zhelpers.h"

int main(int argc, char* argv[])
{
    printf("Collecting updates from weather server...\n");
    void* context = zmq_ctx_new();
    void* subscriber = zmq_socket(context, ZMQ_SUB);
    int rc = zmq_connect(subscriber, "tcp://localhost:5556");
    assert(rc == 0);
    
    /* When you use a SUB socket you must set a subscription using zmq_setsockopt(),
     * otherwise you won't get any messages.
     * A subscription is often, but not necessarily a printable string.
     */
    char* filter = (argc > 1) ? argv[1] : "10001 ";
    rc = zmq_setsockopt(subscriber, ZMQ_SUBSCRIBE, filter, strlen(filter));
    assert(rc == 0);

    int update_nbr;
    long total_temp = 0;
    for(update_nbr = 0; update_nbr < 10; update_nbr++) {
        char* string = s_recv(subscriber);
        int zipcode, temperature, relhumidity;
        sscanf(string, "%d %d %d", &zipcode, &temperature, & relhumidity);
        printf("%d %d %d\n", zipcode, temperature, relhumidity);
        total_temp += temperature;
        free(string);
    }
    printf("Average temperature for zipcode '%s' was %dF\n", filter, (int)(total_temp / update_nbr));

    zmq_close(subscriber);
    printf("subscriber closed.\n");
    zmq_ctx_destroy(context);
    printf("context destroyed.\n");

    return 0;
}
