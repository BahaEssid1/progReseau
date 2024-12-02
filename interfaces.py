from netmiko import ConnectHandler 
router = {
'device_type':'cisco_ios',
'host':'sandbox-iosxe-latest-1.cisco.com',
'username':'admin',
'password':'Cisco12345',
'port':22,}

connection = ConnetHandler(**router)
print("connection success to router cisco")
print("afficher la date coté routeur")
output_clock = connection.send_command("show clock")
print(output_clock)

print("affiche les intefaces des routeurs dans un fichier")
output_interfaces = connection.send_command("sh ip int br")
with open("interfaces.txt", "w")as file:
file.write("output_interfaces")
print("configuration 
config_commands = [
"interface loopback0",
"ip address 10.8.8.8 255.255.255.240",
"no shutdown" ]
connection.send_config_set(config_commands
print("configuration succes")
connection.disconnect()
