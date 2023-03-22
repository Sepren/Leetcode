class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.split('.')
        new_address = ''
        for i in range(len(address) - 1):
            new_address += address[i] + '[.]'
        return new_address + address[-1]