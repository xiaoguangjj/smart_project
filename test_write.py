import write
from write import rfid_write


set_data = [1 for i in range(16)]
a = True

result =  rfid_write(set_data,a)

