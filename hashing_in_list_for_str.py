s="azyxyyzaaaa"
q =['d','a','y','x']

hash_list=[0]*26
for ch in s:
    ascii_val=ord(ch)
    index=ascii_val - 97
    hash_list[index]+=1
print(hash_list)

for i in range(0,len(q)):
    print(f"{q[i]}:{hash_list[ord(q[i])-97]} times")
