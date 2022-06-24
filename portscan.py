import socket  # como vamos fazer as conexões TCP precisamos de um cliente TCP
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # client TCP

# variáveis para conexão


def scan(host, ports):  # criando função para organizar a aplicação
    try:
        for port in ports:  # looping para pegar várias portas
            # definir tempo para conexão
            client.settimeout(0.5)  # tempo que irá tentar se conectar

            # connect_ex pois precisamos apenas saber se foi feita a conexão com o porta
            code = client.connect_ex((host, int(port)))  # mostra se deu certo, ou se deu errado
                                     # tem dois parênteses pq estou passando um tupla

            if code == 0:  # quando deu o código 0 é porque deu tudo certo, caso não algum erro ocorreu
                print("Porta {} no {} está aberta".format(port, host))
            # else:  # caso queira mostrar as portas fechadas também
            #     print("Porta {} fechada".format(port))
    except:
        print("Algum argumento errado")
        print("Como usar: python3 portscan.py 'dominio' 'portas'")
        print("Ex: python3 portscan.py google.com")
        print("Ex: python3 portscan.py google.com 22,23,24,25,80,443")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        host = sys.argv[1]
        if len(sys.argv) >= 3:
            ports = sys.argv[2].split(",")  # para dividir as portas informadas por "," virgula
        else:
            # preciso ajustar para pegar o range de IP's ****************
            ports = range(100)  # escanear todas as 65.536 portas *******
            # str(ports) ************************************************
        scan(host, ports)
    else:
        print("Como usar: python3 portscan.py 'dominio' 'portas'")
        print("Ex: python3 portscan.py google.com")
        print("Ex: python3 portscan.py google.com 22,23,24,25,80,443")


