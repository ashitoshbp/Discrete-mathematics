import hashlib
import random

file = open("211AI007_IT208_Output" , "a")
for trials in range(0 , 100):
    input1 = str(random.randint(pow(10 ,63) , pow(10, 64) ))
    hashedval = hashlib.sha256(input1.encode())
    print(f"INPUT : {input1} ")
    file.write(f"INPUT : {input1} " )
    print(f"OUTPUT :- {hashedval.hexdigest()}")
    file.write("\n")
    file.write(f"OUTPUT :- {hashedval.hexdigest()} "+ "\n")
    print()