class Solution:
    def reversedindex(self, array, req_index:int) -> int:
        i = 0 
        while i < len(array):
            if i+1 == len(array):
                array[0] = array[len(array)]
            else: 
                array[i+1] = array[i] 
            i =+ 1
        return array.index(req_index)