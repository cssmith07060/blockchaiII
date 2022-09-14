import hashlib
import json

def stringify(data):
    return json.dumps(data)


def crypto_hash(*args):
    """
    Return a sha-256 hash of the given data.
    """
    
    stringified_args = map(lambda data: json.dumps(data), args)
    
    joined_data = ''.join(stringified_args)
    
    
    
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f "crypto_hash(2,'one' , [3]) : {crypto_hash({2, 'one', [3])})
    
if__name__=='__main__':
        main()
            