
#create keys string
def enigma_light():
    keys = 'abcdefghijklmnopqrstuvwxyz !.'
    values = keys[-1] + keys[0:-1]
    print(keys)
    print(values)
    

#autogenerate the values string by offering the original string as a default argument

#create two dictionaries, one for encryption and one for decryption
    dict_e = dict(zip(keys,values))
    dict_c = dict(zip(values,keys))
    
# OR create one then flip it so the key and value are switched
    dict_f = dict(zip(keys,values))
    dict_h = {value:key for key, value in dict_f.items()}

#user input 'the message' and mode
    msg = input("Enter your message:")
    mode = input("Enter the mode: encode (e) or decrypt:")

#run code or encode
    if mode.lower() == "e":
        new_msg = ''.join([dict_e[letter] for letter in msg.lower()])
    else:
        new_msg = ''.join([dict_c[letter] for letter in msg.lower()])
#return result
    return new_msg.capitalize()

print(enigma_light())