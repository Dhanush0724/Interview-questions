print("This is how the dhanush do the problem solving taking more time sucks!!!!")
s = "abcdefg"
k = 2
res = ""
res2 = ""
for char in range(len(s)):
    if char < k:
        res += s[char]
    else:
        res2  += s[char]
#print(res)
reverse_two = res[::-1]
#print(reverse_two)
#print(res2)
print("the result of first k reversed::",reverse_two+res2)
print("dhanush code complecity is \n TIme complexity : O(n) \n Space complecity : O(n)")
print("///////////////////////////////////////////")
print("This how James do the Code")
print("Fewer lines and less readablity reduces your overhead")

reverse_two_james = s[:k][::-1]
print(reverse_two_james)
reverse = reverse_two_james + s[k:]
print(reverse)