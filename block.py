import time
def mine_block(last_block, data):
     """
     Mine a block based on the given last_block and data.
     """

   timestamp = time.time_ns()
   last_hash = last_block.hash
   hash = f '{timestamp} - {last_hash}'
   
   return Block(timestamp, last_hash, hash, data)

def genesis():
     '''
     Generate the genesis block.
     '''
     return Block(1, 'genesis_last_hash', 'genesis_hash', [])

class Block:
    '''
Block: a unit of storage.
Store transactions in a blockchain that supports a cryptocurrency.
'''
def__init__(self, timestamp, last_hash, hash):
    self.timestamp= timestamp
    self.last_hash = last_hash
    self.hash = hash
    self.data = data
def __repr__(self):    
     return (
          'Block('
          f'Block: {self.data},'
          f'last_hash: {self.last_hash},'
          f'hash: {hash},'
          f'data: {self.data})'
          )
     
@staticmethod     
def mine_block(last_block, data):
         """
     Mine a block based on the given last_block and data.
     """

   timestamp = time.time_ns()
   last_hash = last_block.hash
   hash = f '{timestamp} - {last_hash}'
   
   return Block(timestamp, last_hash, hash, data)

@staticmethod
def genesis():
     '''
     Generate the genesis block.
     '''
     return Block(1, 'genesis_last_hash', 'genesis_hash', [])

class Block:
def main():
     block = Block('foo')
     print(block)
     print(f'block.py__name: {__name__}')
     
if __name__=='__main__':     