'''
TITLE: NETWORK INFORMATION GENERATOR v1
AUTHOR: JOSHUA WOOTEN
DATE: 3.29.22

GIVEN:
    - NETWORK ADDRESS
    - NUMBER OF HOSTS AVAILABLE
DISPLAY:
    - SUBNET MASK
    - CIDR
    - NUMBER OF AVAILABLE ADDRESSES
'''

netaddress = input('ENTER NETWORK ADDRESS: ')
numhosts = input('ENTER NUMBER OF HOSTS AVAILABLE: ')

def main():

    print("GENERATING NETWORK INFO ...")
    ''' DETERMINE SUBNET MASK CLASSIFICATION BASED ON FIRST SECTION OF IPV4 '''
    netaddress_ARR = netaddress.split('.')
    if int(netaddress.split('.')[0]) <= 127:
        subnet_mask_base = "11111111"
        hostbit_count = 24
    elif int(netaddress.split('.')[0]) >= 128 and int(netaddress.split('.')[0]) <= 191:
        subnet_mask_base = "11111111.11111111"
        hostbit_count = 16
    else:
        subnet_mask_base = "11111111.11111111.11111111"
        hostbit_count = 8

    ''' DETERMINE NUMBER OF BORROWED BITS BASED ON NUMBER OF HOSTS '''
    bb = 0
    for i in range(0, hostbit_count):
        bitval = 2**i
        if int(bitval) >= int(numhosts):
            bb = int(hostbit_count) - i
            break

    ''' USE BORROWED BITS TO GENERATE LAST STRING OF SUBNET MASK '''
    numzeroes = int(hostbit_count) - bb
    finalstring_nodots = f"{'1' * bb}{'0' * numzeroes}"
    finalstring = '.'.join(finalstring_nodots[i:i+8] for i in range(0, len(finalstring_nodots), 8))

    ''' APPEND LAST STRING OF BITS TO FULL STRING '''
    subnet_mask_binary = f"{subnet_mask_base}.{finalstring}"
    '''print(subnet_mask_binary)'''

    ''' CONVERT BINARY SUBNET MASK TO DECIMAL '''
    subnet_mask_string = ""
    subnet_mask_ARR = subnet_mask_binary.split('.')
    for octet in subnet_mask_ARR:
        octet = int(str(octet), 2)
        if subnet_mask_string == "":
            subnet_mask_string = str(octet)
        else:
            subnet_mask_string += f".{str(octet)}"

    print(f"\t→ SUBNET MASK ( BIN ): {subnet_mask_binary}")
    print(f"\t→ SUBNET MASK ( DEC ): {subnet_mask_string}")

    ''' CALCULATE CIDR '''
    cidr = str(subnet_mask_binary.count("1"))
    print(f"\t→ CIDR: /{cidr}")

    ''' CALCULATE AVAILABLE ADDRESSES '''
    available_addr = 2 ** (32 - int(cidr)) - 2
    print(f"\t→ AVAILABLE ADDRESSES: {available_addr}")
    print("DONE.")

if __name__ == "__main__":
    main()
