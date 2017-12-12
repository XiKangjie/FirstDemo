#include <stdio.h>
#include <stdlib.h>
#include <xen/evtchn.h>
#include <sys/ioctl.h>

int main()
{
    printf("IOCTL_EVTCHN_BIND_VIRQ: %#x\n", IOCTL_EVTCHN_BIND_VIRQ);
    printf("IOCTL_EVTCHN_BIND_INTERDOMAIN: %#x\n", IOCTL_EVTCHN_BIND_INTERDOMAIN);
    printf("IOCTL_EVTCHN_BIND_UNBOUND_PORT: %#x\n", IOCTL_EVTCHN_BIND_UNBOUND_PORT);

    struct ioctl_evtchn_bind_interdomain bind;
    bind.remote_domain = 0;
    bind.remote_port = 212;

    int fd;
    fd = open("/dev/xen/evtchn", 0);
    if(fd < 0) {
        printf("can't open.");
        exit(-1);
    }

    int ret = ioctl(fd, IOCTL_EVTCHN_BIND_UNBOUND_PORT, &bind);
    if(ret < 0) {
        printf("ioctl failed: %d\n", ret);
    }
}
