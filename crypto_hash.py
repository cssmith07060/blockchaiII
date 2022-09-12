import hashlib
import json
def crypto_hash(*args):
    """
    Return a sha-256 hash of the given data.
    """
    
    stringified_data = json.dumps(data)
    
    return hashlib.sha256(stringified_data.encode('utf-8')).hexdigest()

def main():
    
if__name__=='__main__':
        main()
            