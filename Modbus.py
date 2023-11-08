from pyModbusTCP.client import ModbusClient

# TCP auto connect on first modbus request
c = ModbusClient(host="192.168.0.1", port=502, unit_id=1, auto_open=True)


for ad in range(3):
    is_ok = c.write_single_coil(ad, False)

c.write_single_register(0,33)
c.write_single_register(1,44)
c.write_single_register(2,55)


coils_l = c.read_coils(0, 3)
regs = c.read_holding_registers(0, 3)

if coils_l:
        print('Motor 1 status: ' , + coils_l[0])
        print('Motor 2 status: ' , + coils_l[1])
        print('Motor 3 status: ' , + coils_l[2])
else:
        print('unable to read coils')

if regs:
    print('Counts =', + regs[0])
    print('Level =', +regs[1])
    print('Temp =', +regs[2])
else:
    print("read error")
