#Learned from: https://youtu.be/f0ZDVqoViqE

import hashlib

#print out the encoded 'Hello World'
#print(hashlib.sha256('Hello World'.encode()).hexdigest())

nonce_limit=10000000
zeros=4 #leading zeros needed

def mine(block_num, transactions, prev_hash):
	for nonce in range(nonce_limit):
		base_text=str(block_num)+transactions+prev_hash+str(nonce)
		hash_try=hashlib.sha256(base_text.encode()).hexdigest()
		if hash_try.startswith('0'*zeros):
			print(f'Found Hash With Nonce: {nonce}')
			return hash_try

	return -1

block_num=24
transactions='76123fcc2141'
prev_hash='876de8756b967c87'

combined_text=str(block_num)+transactions+prev_hash

print(hashlib.sha256(combined_text.encode()).hexdigest())

return_var=mine(block_num, transactions, prev_hash)

print('return_var='+str(return_var))