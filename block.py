def mine_block(last_block, data):
     """
     Mine a block based on the given last_block and data.
     """


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
def main():
     block = Block('foo')
     print(block)
     print(f'block.py__name: {__name__}')
     
if __name__=='__main__':     