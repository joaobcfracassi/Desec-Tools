param($ip)
if (!$ip){
    echo "DESEC SECURITY"
    echo "Exemplo de uso: .\portscanner.ps1 192.168.0.1" 
} else {
    $topports = 21,22,3306,80,443
    try {foreach ($porta in $topports){
        if (Test-NetConnection $ip -Port $porta -WarningAction SilentlyContinue -InformationLevel Quiet){
            echo "Porta $porta aberta"
            }
        }
    } catch {}
}