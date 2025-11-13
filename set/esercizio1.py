numeri = {1,1,2,2,3,4,5}
print(numeri) 

print("--------------------")

s = {"a", "b"}
s.add("c")
print(s)

print("--------------------")

a = {1,2,3}
b = {3,4,5}
print(a.union(b))

print("--------------------")
print("intersezione e differenza")
c = {1,2,3}
d = {2,3,4}
print(c & d);

print(c - d);
print(d - c);

print("--------------------")
print("verifica di appartennenza")

s = {"mela", "banana", "arancia"}
print("banana" in s)
print("kiwi" in s)