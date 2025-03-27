#### **Longest Common Substring/Subsequence**
>Es gibt unterschiedliche Methoden, um dises Problem zu lösen.
>
>**1. Rekursiver Algorithmus**
```python
LCSubstring(T,P,i,j,counter):
	if i == 0 or j == 0:
		return counter
	if T[i] == P[j]:
		counter = LCSubstring(T,P,i-1,j-1,counter+1)
	counter2 = LCSubstring(T,P,i-1,j,0)
	counter3 = LCSubstring(T,P,i,j-1,0)
	return max(counter,counter2,counter3)

print(LCSubstring("abcd","abd",3,2,0))
```
>Time complexity : O(2^n)
>**2.Memoization**
>keine unnötigte Berechnungen sollen gemacht werden.
>hier wird ein 3D Matrix verwendet, um bereits gemachte Schritte nicht nochmal zu berechnen.
>Problem : Speicherplatz 
>**3. Dynamische Programierung**
> ![[Pasted image 20240425195425.png]]
```python
str1 = "abcdefg"
str2 = "cdgi"
dp = [[0]* (len(str1)+1) for i in range(len(str2)+1)]
longest = 0
for i in range(1,len(str2)+1):
	for j in range(1,len(str1)+1):
		if str1[j-1] == str2[i-1]:
			dp[i][j] = dp[i-1][j-1] + 1
			longest = max(longest,dp[i][j])
print(dp)
print(longest)
```
> **4. Suffix Trie**
> ![[Pasted image 20240425195520.png]]
```python
S1 = "abcdefg$"
S2 = "cdgi#"
suffixS1 = [S1[i:] for i in range(len(S1))]
suffixS2 = [S2[i:] for i in range(len(S2))]
suffixes = suffixS1 + suffixS2
print(suffixes)
root = dict()
for suffix in suffixes:
	curr = root
	for character in suffix:
		curr = curr.setdefault(character,{})

print(root)
```


#### **Longest Common Subsequence**
>![[Pasted image 20240425200101.png]]
```python

str1 = "abcdefg"
str2 = "cdgi"
dp = [[0]* (len(str1)+1) for i in range(len(str2)+1)]

for i in range(1,len(str2)+1):
	for j in range(1,len(str1)+1):
		if str2[i-1] == str1[j-1]:
			dp[i][j] = dp[i-1][j-1]+1
		else : 
			dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp)
```