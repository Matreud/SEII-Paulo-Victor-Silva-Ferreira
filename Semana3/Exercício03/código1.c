/*
If the program is invoked several times, a different process ID is
reported because each invocation is in a new process.
However, if you invoke it everytime from the same shell, the parent process ID
(that is, the process ID of the shell process) is the same.
*/

#include <stdio.h>
#include <unistd.h>

int main(){
    
    printf("The process ID is %d\n", (int) getpid());
    printf("The parent process ID is %d\n", (int) getppid());
    
    return 0;
}