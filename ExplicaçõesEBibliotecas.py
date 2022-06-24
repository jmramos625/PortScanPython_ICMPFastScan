import ipaddress

# defina o IP, com a variável do próprio IPAdrress

ip = ipaddress.ip_address("192.168.0.1")
print(ip)
ip += 1  # quando se adiciona 1 a esse IP, ele mesmo adiciona um na sequencia do IP
print(ip)

network = ipaddress.ip_network("192.168.0.0/24")  # criando um range de IP's

for i in network:
    print(i)

network2 = ipaddress.ip_network("192.168.1.0/16", strict=False)  # cria um range que varia a última e penúltima casas do IP
# porém para isso é necessário que coloque o strict=False, para não ter problema com a penúltima parte do IP


