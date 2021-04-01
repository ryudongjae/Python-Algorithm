#Chainning

hash_table = list([0 for i in range(10)])

def get_key(data):
    return hash(data);

def hash_func(key):
    return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_func(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_func(index_key)

    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None

print(hash('Kim')%8)
print(hash('Lee')%8)
print(hash('Park')%8)


save_data('Park','8970870')
save_data('Lee','21321213213')
print(read_data('Lee'))

print(hash_table)

