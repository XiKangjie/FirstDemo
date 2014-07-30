#ifndef SIGNAL_FUNCTION_H
#define SIGNAL_FUNCTION_H

#include <signal.h>
#include "../lib/tlpi_hdr.h"

int printSigMask(FILE* of, const char* msg);

int printPendingSigs(FILE* of, const char* msg);

void printSigset(FILE* of, const char* ldr, const sigset_t* mask);

#endif
