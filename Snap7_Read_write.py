import snap7
import struct

plc = snap7.client.Client()
plc.connect('192.168.0.9',0,1)

db_number = 100
start_offset = 2
bit_offset = 0
value =1

start_address = 2
length = 4

def writeBool(db_number, start_offset,bit_offset,value):
    reading = plc.db_read(db_number,start_offset,1)
    snap7.util.set_bool(reading,0,bit_offset,value)
    plc.db_write(db_number,start_offset,reading)
    return None

def readBool(db_number, start_offset,bit_offset):
    reading = plc.db_read(db_number,start_offset,1)
    a = snap7.util.get_bool(reading,0,bit_offset)
  
    print('DB number:'+ str(db_number) + 'Bit:' +str(start_offset) + ','
            + ',' + str(bit_offset) + 'value' + str(a))
    return None

# Write Integer value
def write_int(db_num,start_byte,int_value): #Integer yazma 
    data = bytearray(2)
    snap7.util.set_int(data,0,int_value)
    plc.db_write(db_num,start_byte,data) 
    return None

# Read Integer value
def read_int(db_num,start_byte,size): #Integer yazma 
    data = bytearray(2)
    snap7.util.get_int(data,0)
    reading = plc.db_read(db_num,start_byte,size) 
    value = int.from_bytes(reading, "big")
    print(f"{db_num} {start_byte} ':' {value}")
    return None


# Write floating point value
def write_real(db_num,start_byte,real_value): #Real yazma 
    data = bytearray(4)
    snap7.util.set_real(data,0,real_value)
    plc.db_write(db_num,start_byte,data)
    return None

# Read Floating Point
def read_real(db_num,start_byte,size): #Real yazma 
    data = bytearray(4)
    snap7.util.get_real(data,0)
    reading =plc.db_read(db_num,start_byte,size)
    [value] = struct.unpack('>f', reading)
    print(f"{db_num} {start_byte} ':' {value}")
    return None


while True:
        
    #read_int(db_number,start_address,2)
    #read_real(db_number,start_address,4)
    #write_int(db_number,start_address,2)
    #write_real(db_number,start_address,value)
    #readBool(db_number, start_offset,bit_offset)
    #writeBool(db_number, start_offset,bit_offset,value)
    #1