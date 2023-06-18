import time as utime
import busio
import board
import usb_cdc
from Arducam import *
from board import *

once_number=128
mode = 0
start_capture = 0
stop_flag=0
data_in=0
value_command=0
flag_command=0
buffer=bytearray(once_number)

mycam = ArducamClass(OV2640)
mycam.Camera_Detection()
mycam.Spi_Test()
mycam.Camera_Init()
utime.sleep(1)
mycam.clear_fifo_flag()

#import uos
#import gc
import time




def read_fifo_burst():
    count=0
    lenght=mycam.read_fifo_length()
    mycam.SPI_CS_LOW()
    mycam.set_fifo_burst()
    while True:
        mycam.spi.readinto(buffer,start=0,end=once_number)
        print(buffer)
        usb_cdc.data.write(buffer)
        
        utime.sleep(0.00015)
        count+=once_number
        if count+once_number>lenght:
            count=lenght-count
            mycam.spi.readinto(buffer,start=0,end=count)
            print(buffer)
            usb_cdc.data.write(buffer) 
            
            mycam.SPI_CS_HIGH()
            mycam.clear_fifo_flag()
            break

class aclass(object):
    def __init__(self, spi):
        self.hspi = spi
        self.cspin = 2
    def capture_to_file(self, fn, overwrite):
        mycam.clear_fifo_flag()
        
        # bit 1 - start capture then read status
        # cam_spi_write(b'\x04', b'\x02', self.hspi, self.cspin)
        mycam.start_capture()
        #time.sleep(10)
    
        # read status
        #res = cam_spi_read(b'\x41', self.hspi, self.cspin)
        mycam.Spi_read(0x41)
        cnt = 0
        #if (res == b'\x00'):
        #    print("initiate capture may have failed, return byte: %s" % ubinascii.hexlify(res))

        # read the image from the camera fifo
        while True:
            res = mycam.Spi_read(0x41)
            mask = b'\x08'
            if (res[0] & mask[0]):
                break
            #print("continuing, res register %s" % ubinascii.hexlify(res))
            #time.sleep(10)
            cnt += 1
        #print("slept in loop %d times" % cnt)
   
        # read the fifo size
        b1 = mycam.Spi_read(0x44)
        b2 = mycam.Spi_read(0x43)
        b3 = mycam.Spi_read(0x42)
        val = b1[0] << 16 | b2[0] << 8 | b3[0] 
        print("ov2640_capture: %d bytes in fifo" % val)
        #gc.collect()
        
        PICBUFSIZE = 64
        
        bytebuf = [ 0, 0 ]
        picbuf = [ b'\x00' ] * PICBUFSIZE
        l = 0
        bp = 0
        #if (overwrite == True):
            #pass
            #print("deleting old file %s" % fn)
            #try:
            #    uos.remove(fn)
            #except OSError:
            #    pass
        while ((bytebuf[0] != b'\xd9') or (bytebuf[1] != b'\xff')):
            bytebuf[1] = bytebuf[0]
            if (bp > (len(picbuf) - 1)):
                #print("appending buffer to %s" % fn)
                appendbuf(fn, picbuf, bp)
                bp = 0
    
            bytebuf[0] = mycam.Spi_read(0x3d)
            l += 1
            #print("read so far: %d, next byte: %s" % (l, ubinascii.hexlify(bytebuf[0])))
            picbuf[bp] = bytebuf[0]
            bp += 1
        if (bp > 0):
            #print("appending final buffer to %s" % fn)
            appendbuf(fn, picbuf, bp)
        print("read %d bytes from fifo, camera said %d were available" % (l, val))
        return (l)

x = bytearray()

def appendbuf(fn, picbuf, howmany):
    try:
        # f = open(fn, 'ab')
        c = 1
        for by in picbuf:
            if (c > howmany):
                break
            c += 1
            #print(by[0])
            #print(bytes([by[0]]))
            x.append(by[0])
            # f.write(bytes([by[0]]))
        # f.close()
    except OSError:
        raise OSError
        print("error writing file")
    print("write %d bytes from buffer" % howmany)

a = aclass(mycam.spi)
a.capture_to_file('mysavedimage.jpg',True)

print(x)