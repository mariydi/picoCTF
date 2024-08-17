char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = [20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]

ans =""
for i in range(15):
    ans += char[number[i]-1]
print("picoctf{"+ans+"}")
