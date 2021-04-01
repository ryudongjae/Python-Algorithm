hash_table = list([0 for i in range(10)])
print(hash_table)

data1 ="Kim"
data2 ="Park"
data3 ="Yoon"

def hash_func(key):
    return key % 5

def storage_data(data,value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

storage_data("Kim","01011112222")
storage_data("park","01033334444")
storage_data("Yoon","01044445555")


def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]

print(get_data("Kim"))


#문자의 ASCII(아스키) 코드리턴
print(ord(data1[0]),ord(data2[0]),ord(data3[0]))
print(hash_func(ord(data1[0])))
print(hash_func(ord(data2[0])))
print(hash_func(ord(data3[0])))