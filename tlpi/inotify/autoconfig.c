/* auto  update configuration at runtime */
#include <stdio.h>
#include <sys/inotify.h>
#include <limits.h>
#include <fcntl.h>

#define BUF_LEN (10 * (sizeof(struct inotify_event) + NAME_MAX + 1))

int running = 0;

void dolog()
{
    int inotifyFd, wd;
    char buf[BUF_LEN];
    ssize_t numRead;
    char *p;
    struct inotify_event *event;

    inotifyFd = inotify_init();
    if (inotifyFd == -1)
        printf("error: inotify_init\n");
    // int res = fcntl(inotifyFd, F_GETFL);
    // res |= O_NONBLOCK;
    // fcntl(inotifyFd, F_SETFL, res);
    wd = inotify_add_watch(inotifyFd, "./config.xml", IN_ALL_EVENTS);
    if (wd == -1)
        printf("error: inotify_add_watch\n");

    numRead = read(inotifyFd, buf, BUF_LEN);
    if (numRead == 0)
        printf("error: read() returned 0.\n");
    if (numRead == -1)
        printf("error: read\n");

    p = buf;
    while(p < buf + numRead) {
        event = (struct inotify_event*)p;
        if (event->mask & IN_IGNORED) {
            inotify_add_watch(inotifyFd, "./config.xml", IN_ALL_EVENTS);
            running = !running;
            printf("ignored, running: %d\n", running);
        }
        else if(event->mask & IN_CLOSE_WRITE) {
            running = !running;
            printf("close_write, running: %d\n", running);
        }
        p += sizeof(struct inotify_event) + event->len;
    }
}

int main()
{
    while (1) {
        dolog();    

        if (running)
            printf("log is running.\n");
        else
            printf("log is off.\n");
        sleep(5);
    }
    return 0;
}
