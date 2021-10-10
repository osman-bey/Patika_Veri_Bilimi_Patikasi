"""
Verilen listenin içindeki elemanları tersine döndüren
bir fonksiyon yazın. Eğer listenin içindeki elemanlar
da liste içeriyorsa onların elemanlarını da tersine
döndürün. Örnek olarak:

input: [[1, 2], [3, 4], [5, 6, 7]]

output: [[[7, 6, 5], [4, 3], [2, 1]]
"""

def reverse(l):

    for i in l:
        if type(i) is list:
            i.reverse()
        else:
            continue
    
    l.reverse()
    print(l)

if __name__ == '__main__':
    
    input_list = [[1, 2], [3, 4], [5, 6, 7]]
    reverse(input_list)