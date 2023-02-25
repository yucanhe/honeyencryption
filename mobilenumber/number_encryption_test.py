# credit_card_test.py

# Tests to see if the methods in credit_card.py, probabilityfunctionAPI.py, and DTE.py


from number_encryption import *
from DTE import *


telno_example = '13146959906'
secret_key = 2048101736616812280

guess_key = 5496328831800304765


id_fxns = TelNOProbabilityFxns()

# Use DTE on identification example
seed = encode(telno_example, id_fxns)
ciphertext = secret_key ^ seed
decipher_seed = guess_key ^ ciphertext

print("MOBILE NUMBER TO BE ENCRYPED:"  + telno_example)
print("CIPHERTEXT: " + str(ciphertext))

message = decode(decipher_seed, id_fxns)
print("decoded by the guessed seed, returned MESSAGE: " + message)

message = decode(seed, id_fxns)
print("decoded by a right seed, returned MESSAGE: " + message)
