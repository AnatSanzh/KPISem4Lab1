import doctest
import cui
import fake_storage
import record
import record_decoder
import record_encoder
import server
import storage

print(doctest.testmod(cui))
print(doctest.testmod(fake_storage))
print(doctest.testmod(record))
print(doctest.testmod(record_decoder))
print(doctest.testmod(record_encoder))
print(doctest.testmod(server))
print(doctest.testmod(storage))
