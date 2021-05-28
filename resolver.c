#include <stdio.h>
#include <netdb.h>
#include <arpa/inet.h>

int main(int argc, char *argv[]){

	char *host;
	host = argv[1];
	
	if (argc < 2){
		printf("Modo de uso: ./resolver www.businesscorp.com.br\n");
		return 0;
	} else {
		struct hostent *alvo = gethostbyname(host);

		if (alvo == NULL) {
			printf ("Ocorreu um erro :( \n");
		} else {
			printf("IP: %s\n",inet_ntoa(*((struct in_addr *)alvo->h_addr)));
		}
	}

	return 0;
}