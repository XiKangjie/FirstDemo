#include <stdio.h>
#include <stdlib.h>
#include "../timeuse.h"

int main()
{
    TimeUse tu0;
    tu0.Start();
    tu0.End();
    tu0.PrintTimeUse();


    char buf[128];
    TimeUse tu;
    tu.Start();
    snprintf(buf, 128, "mv %s.old %s", "rename.txt", "rename.txt");
    system(buf);
    tu.End();
    printf("system(): ");
    tu.PrintTimeUse();
    tu.Start();
    snprintf(buf, 128, "%s.old", "rename.txt");
    rename("rename.txt", buf);
    tu.End();
    printf("rename(): ");
    tu.PrintTimeUse();
    return 0;
}
