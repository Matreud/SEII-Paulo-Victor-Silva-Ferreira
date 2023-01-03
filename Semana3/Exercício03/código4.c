#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int spawn(char* program, char** arg_list){

    pid_t child_pid;

    /*Duplicar processo*/
    child_pid = fork();
    if(child_pid != 0)
        /*Se processo pai:*/
        return child_pid;
        
    else{
        /*Executar programa*/
        execvp(program, arg_list);
        /*Em caso de erro:*/
        fprintf(stderr, "an error occurred in execvp\n");
        abort();
    }
}

int main(){
   /*Lista de argumentos para o comando ls*/
    char* arg_list[] = {
       "ls", /*argv[0], Nome do programa*/
       "-l",
       "/",
       NULL /*NULL mandatório*/
    };    
    /*Cria um processo filho usando ls
    Ignora PID retornado.
    */
    spawn("ls", arg_list);
    printf("done with main program\n");

    return 0;
}