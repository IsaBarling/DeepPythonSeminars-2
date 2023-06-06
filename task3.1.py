def task3(num: int, mode: str) -> str:
     result = ''
     convert: int = 24

     match mode:
         case "bin":
             convert = 2
         case "oct":
             convert = 8

     while num >= 1:
         res = num % convert

         result += str(res)
         num = num // convert

     return result[::-1]


print(task3(21, mode="bin"), f"assert: {bin(21)}")
print(task3(21, mode="oct"), f"assert: {oct(21)}")
    