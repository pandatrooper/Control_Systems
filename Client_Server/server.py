#!/usr/bin/env python
# Pymodbus Asynchronous Server Example

# import the various server implementations
from pymodbus.version import version
from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.server.asynchronous import StartUdpServer
from pymodbus.server.asynchronous import StartSerialServer

from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import (ModbusRtuFramer,
                                  ModbusAsciiFramer,
                                  ModbusBinaryFramer)

# configure the service logging
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [17] * 100),  # Discrete inputs initializer
    co=ModbusSequentialDataBlock(0, [17] * 100),  # Coils initializer
    hr=ModbusSequentialDataBlock(0, [17] * 100),  # Holding register initializer
    ir=ModbusSequentialDataBlock(0, [17] * 100))  # Input registers initializer
context = ModbusServerContext(slaves=store, single=True)

# initialize the server information
identity = ModbusDeviceIdentification()
identity.VendorName = 'Pymodbus'
identity.ProductCode = 'PM'
identity.VendorUrl = 'http://github.com/bashwork/pymodbus/'
identity.ProductName = 'Pymodbus Server'
identity.ModelName = 'Pymodbus vServer'
identity.MajorMinorRevision = '1.0'

# run the server you want

# Modbus over Ethernet via IP
StartTcpServer(context, identity=identity, address=("localhost", 502))
# StartUdpServer(context, identity=identity, address=("127.0.0.1", 502))

# Serial
# StartSerialServer(context, identity=identity, port='/dev/pts/3', framer=ModbusRtuFramer)
# StartSerialServer(context, identity=identity, port='/dev/pts/3', framer=ModbusAsciiFramer)