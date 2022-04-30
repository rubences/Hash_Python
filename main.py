# for a complete usage of hashlib, see https://docs.python.org/3/library/hashlib.html
import hashlib
from data import * 

print(msg1==msg2)

m = hashlib.md5()
m.update(msg1)

#m = hashlib.sha1(b'SAR111 is full of fun')
print(m.hexdigest())


m2 = hashlib.md5()
m2.update(msg2)
print(m2.hexdigest())

print(m.hexdigest()==m2.hexdigest())