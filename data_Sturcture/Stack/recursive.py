#재귀 함수

def recursive(data):
    if data <0:
        print("ended")
    else:
        print(data)
        recursive(data -1)
        print("returned",data)

print(recursive(4))