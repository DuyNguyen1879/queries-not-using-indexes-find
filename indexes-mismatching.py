# indexes-mismatching.py
#find not using indexes
#if anyone is NULL
#if keys in possible keys and len(possible_keys) > len(keys)

with open('explain-output.txt') as f:
    content = f.read()

fileDataInList = content.split('--------------\nEXPLAIN')
for i in fileDataInList:
    indexOfI = fileDataInList.index(i)
    blockData = i.split('\n')
    for j in blockData:
        if j.startswith('possible_keys'):
            index_possible_keys = blockData.index(j)
            #print(index_possible_keys)
            index_keys = index_possible_keys + 1
            possible_keys_data = blockData[index_possible_keys]
            keys_data = blockData[index_keys]
            data1 = possible_keys_data.split(':')
            data2 = keys_data.split(':')
            data1 = data1[-1].strip()
            data2 = data2[-1].strip()
            if (data1 == 'NULL' or data2 == 'NULL'):
                print('--------------\nNULL condition true\nEXPLAIN', end='')
                print(i)
            elif ((data2 in data1) and (len(data1) > len(data2))):
                print('--------------\nNot using all keys\nEXPLAIN', end='')
                print(i)
                
