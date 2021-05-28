#include <stdio.h>
#include <sys/socket.h>
#include <netdb.h>

int main(void){

	char host[] = "businesscorp.com.br";
	int porta = 80;
	int conecta;
	int meusocket;

	struct sockaddr_in alvo;

	while(1){
		meusocket = socket(AF_INET,SOCK_STREAM,0);
		alvo.sin_family = AF_INET;
		alvo.sin_port = htons(porta);
		alvo.sin_addr.s_addr = inet_addr(host);

		conecta = connect(meusocket, (struct sockaddr *)&alvo, sizeof alvo);
		if(conecta == 0){
			printf("conectando a porta %d\n",porta);
		}

	}

}