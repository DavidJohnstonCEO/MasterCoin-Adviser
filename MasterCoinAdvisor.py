import sys
import base58_found

print "MasterCoinAdvisor.py - version 0.01 - Simple Send Only"
print ""
print "Enter currency identifier (MasterCoin = 1, Test MasterCoin = 2)"
currencyId = int(sys.stdin.readline())
print "Enter amount of currency you wish to send: "
amount = long(float(sys.stdin.readline())*100000000)
print "Enter the address you wish to send to: "
recipientAddress = sys.stdin.readline().strip("\r\n")

recipientBytes = base58_found.b58decode(recipientAddress, 25);

recipientSequenceNum = ord(recipientBytes[1])
#print "Recipient sequence number: {0}".format(recipientSequenceNum) 
dataSequenceNum = recipientSequenceNum - 1
if dataSequenceNum < 0:
	dataSequenceNum = dataSequenceNum + 256

transactionType = 0
dataHex = '{:02x}'.format(0) + '{:02x}'.format(dataSequenceNum) + '{:08x}'.format(transactionType) + '{:08x}'.format(currencyId) + '{:016x}'.format(amount) + '{:06x}'.format(0)
#print "Transaction Data (hex)   : {0}".format(dataHex) 
dataBytes = dataHex.decode('hex_codec')
dataAddress = base58_found.hash_160_to_bc_address(dataBytes[1:21])
#print "data Address: {0}".format(dataAddress)

print ""
print "Step 1: Send all funds in your wallet to the address which owns the MasterCoins (the following sends must come from that address)"
print ""
print "Step 2: Send exactly 0.00006 BTC from your address to each of the following 3 addresses in one transaction:"
print ""
print "The Exodus Address:    1EXoDusjGwvnjZUyKkxZ4UHEf77z6A5S4P"
print "The recipient address: {0}".format(recipientAddress)
print "The data address:      {0}".format(dataAddress)
print ""

dataStored = base58_found.b58decode(dataAddress, 25).encode('hex_codec')
print "data stored was: {0}".format(dataStored) 