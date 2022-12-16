'''Given an integer N.Create a string using only lowercase characters from a to z that follows the given rules.

When N is even:

Use N/2 characters from the beginning of a-z and N/2 characters from the ending of a-z.

When N is greater than 26,continue repeating the instructions until length of string becomes N.

When N is odd:

Case 1: If the sum of digits of N is even, Select (N+1)/2 characters from the beginning of a-z and (N-1)/2 characters from the ending of a-z.

Case 2: If the sum of digits of N is odd, Select (N-1)/2 characters from the beginning of a-z and (N+1)/2 characters from the ending of a-z.

When N is greater than 26,continue repeating the instructions until length of string becomes N.

 '''

 def BalancedString(N):
    li='abcdefghijklmnopqrstuvwxyz'
    n=N//26
    p=N
    ans=li*n
    c=0
    while N>0:
        c+=N%10
        N=N//10
    N=p%26
    if c%2==0:
        if N%2==0:
            ans+=li[:N//2]+li[26-(N//2):26]
        else:
            ans+=li[:(N+1)//2]+li[26-((N-1)//2):26]
    else:
        if N%2==0:
            ans+=li[:N//2]+li[26-(N//2):26]
        else:
            ans+=li[:(N-1)//2]+li[26-((N+1)//2):26]
    return ans