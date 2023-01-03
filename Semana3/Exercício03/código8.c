#include <signal.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>

sig_atomic_t child_exit_status;

void clean_up_child_process(int signal_number){
    /*rotina para limpar processos zumbis*/
    int status;
    wait (&status);
    /*guarda o status de saída em uma variável global*/
    child_exit_status = status;
}

int main(){
    
    
    return 0;
}
