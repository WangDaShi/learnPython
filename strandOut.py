def println(str):{
    print(str)
}
#���һ��ע��
def getTable(pattern):
    table = [-1]*len(pattern)
    i,j = 0,1
    while(i < len(pattern)):
        if pattern[i] == pattern[j]:
            table[i] = j
            i += 1
            j += 1
        else:
            j = table[j]
    return table
# test
table = getTable('ababcedab')
print(table)
