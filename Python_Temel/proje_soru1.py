"""
Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
Elemanları birden çok katmanlı listelerden ([[3],2] gibi)
oluşabileceği gibi, non-scalar verilerden de oluşabilir.
Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output: [1,'a','cat',2,3,'dog',4,5]
"""

def include_list(l):

    for i in l:
        if type(i) is list:
            return True
    
    return False

def flatten(l):

    while (include_list(l)):
        new_l = []
        for i in l:
            if type(i) is list:
                new_l.extend(i)
            else:
                new_l.append(i)
        l = new_l

    print(new_l)

if __name__ == '__main__':
    
    input_list = [[1, 'a', ['cat'] ,2], [[[3]], 'dog'], 4, 5]
    flatten(input_list)