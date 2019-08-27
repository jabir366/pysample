valid_characters = 'ABCDEFabcdef:0123456789'
address = input('Please enter an IP address: ')

is_valid = all(current in valid_characters for current in address)
address_list = address.split(':')
valid_segment = all(len(current) <= 4 for current in address_list)
morethan2col= address.find(':::') != -1
if is_valid and valid_segment and not morethan2col  :
    print('It is a valid IPv6 address.')
else:
    print('It is not a valid IPv6 address.')
