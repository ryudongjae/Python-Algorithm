hash_table = list([0 for i in range(10)])

def get_key(data):
    return hash(data);

def hash_func(key):
    return key % 8

def save_data(data,value):
    hash_address = hash_func(get_key(data))
    hash_table[hash_address] = value

def read_data(data):
    hash_address = hash_func(get_key(data))
    return hash_table[hash_address]

save_data("KIM","0001")
save_data("SIM","0002")

print(read_data("SIM"))

print(hash_table)





