
#FizzBuzz
# asnwer[i] == "fizzBuzz" if i is divisible by 3 & 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answe[i] ==  "Buzz" if i is divisible by 5.
# answer[i] == i(as a string) if none of the above condition are true.
n = 8
ans= []
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        ans.append("fizzBuzz")
    elif i%3==0:
        ans.append("fizz")
    elif i%5==0:
        ans.append("Buzz")
    else:
        ans.append(str(i))

        print(ans)   
