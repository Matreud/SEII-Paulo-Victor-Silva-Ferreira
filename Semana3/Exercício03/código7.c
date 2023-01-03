#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main(){
    pid_t child_pid;

    /*cria processo filho*/
    child_pid = fork();
    if(child_pid > 0){
        /*processo pai. sleep por um minuto*/
        sleep(60);
    }
    
    else{
        /*processo filho. Acabar imediatamente.*/
        exit(0);
    }
    
    return 0;
}
