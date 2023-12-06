#!/usr/bin/env python3

""" Read 10 holding registers and print result on stdout. """

import time
from pyModbusTCP.client import ModbusClient


# init modbus client
#
#c = ModbusClient(debug=False, auto_open=True)
c = ModbusClient(host='localhost', port=502, auto_open=True, debug=False)

#Polling a adress IP.
#ip='192.168.0.30'
#puerto = 502
#C = ModbusClient(host=ip, port=puerto, auto_open= True, debug=False)

# main read loop
while True:
    # read 10 registers at address 0, store result in regs list
    # Modiied to rear 5 registers
    regs_l = c.read_holding_registers(0, 5)
    
    # if success display registers
    if regs_l:
        #print('reg ad #0 to : %s' % regs_l)
        print('reg ad #0 to', len(regs_l), ': %s' % regs_l)
    else:
        print('unable to read registers')

    # sleep 2s before next polling
    time.sleep(2)