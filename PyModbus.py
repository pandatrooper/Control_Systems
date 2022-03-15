from pymodbus.client.sync import ModbusTcpClient

hostname = '192.168.1.251'
client = ModbusTcpClient(hostname)
client.connect()
client.write_coils(1, [1] * 5)
client.write_coils
result = client.read_coils(0, 5)
if result:
    print("%M0 : " + str(result.bits[0]))
    print("%M1 : " + str(result.bits[1]))
    print("%M2 : " + str(result.bits[2]))
    print("%M3 : " + str(result.bits[3]))
    print("%M4 : " + str(result.bits[4]))
