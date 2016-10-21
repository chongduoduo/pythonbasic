import hashmap

## test hash_key function
testdict = hashmap.new()
bucket = hashmap.get_bucket(testdict, 'Oregon')
#print bucket

hashmap.set(testdict, 'Oregon', 'OR')
#print testdict

testbucket = hashmap.get_bucket(testdict, 'Oregon')
print testbucket

for i, kv in enumerate(testbucket):
    print i, kv
    k, v = kv
    print i, k, v
#    if key == k:
#        return i, k, v

		#i, k, v = hashmap.get_slot(testdict, 'Oregon')
#print i, k, v