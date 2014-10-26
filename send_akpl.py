from nrf24 import NRF24
import time

pipes = [[0xe7, 0xe7, 0xe7, 0xe7, 0xe7], [0xc2, 0xc2, 0xc2, 0xc2, 0xc2]]

radio = NRF24()
radio.begin(0, 0, 17) #Set ce0/csn and rf24-CE
radio.setRetries(15,15)
radio.setPayloadSize(32)
radio.setChannel(0x60)



radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MAX)
radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()


radio.openWritingPipe(pipes[0])
radio.openReadingPipe(1, pipes[0])

radio.printDetails()

c=1
while True:
    buf = [0x81, c, "O", "D", "I"]
    c = (c + 1) & 255
    # send a packet to receiver
    radio.write(buf)
    print buf
    radio.printDetails()
    # did it return with a payload?
    if radio.isAckPayloadAvailable():
        print "tes lah"
        pl_buffer=[]
        radio.read(pl_buffer, radio.getDynamicPayloadSize())
        print pl_buffer
    time.sleep(1)
