import hashlib
print("Expected password input is either a birthday, x/x/xxxx, or studentid, xxxxxx. You can also enter a number up to 14 characters.")
passtohash = raw_input("What password would you like to hash? ")
print("hashing " + passtohash)
passasbytes = str.encode(passtohash)
hash_object = hashlib.md5(passasbytes)
print("your hash is " + hash_object.hexdigest())
print("When you hack into a database, you will get a bunch of passwords that are hashed, just like the one you see above. We will now write that hash to a file and then use a program to crack the hash. We have not stored your password anywhere; the program is only given the hash.") 
hashfile = open("hash.hash", "w")
n = hashfile.write(hash_object.hexdigest())
hashfile.close()
