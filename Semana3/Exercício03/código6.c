#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main(){
    int child_status;

    /*Lista de argumentos para o comando ls*/
    char* arg_list[] = {
        "ls", /*argv[0], nome do programa*/
        "-l",
        "/",
        NULL /*NULL mandatório*/
    };

    /*Cria processo filho
    ignora PID do processo filho*/
    spawn("ls", arg_list);

    /*Espera o fim do processo filho*/
    wait(&child_status);
    
    if(WIFEXITED(child_status)){
        printf("the child process exited normally, with exit code %d\n"), WEXITSATUS(child_status);
    }
    else{
        printf("the child process exited abnormally\n");
    }
    
    return 0;
}
