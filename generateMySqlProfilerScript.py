#SELECT
#UPDATE
#DELETE
#INSERT
#REPLACE
# with open('localhost-slow.log') as f:/var/log/mysql/localhost-slow.log



with open('/var/log/mysql/localhost-slow.log') as f:
    content = f.readlines()
#remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
str1 = ''
lenContent = len(content)

def getEndingLinePosition(startIndex):
        for i in range(startIndex, lenContent):
                if(content[i].endswith(';')):
                        endIndex = i
                        return endIndex
def getTheContent(startIndex, endIndex):
        str2 = ''
        for i in range(startIndex, endIndex+1):
                str2 = str2+' '+content[i].strip()
        #print(str2)
        return str2

for data in content:
        if (data.startswith('USE')):
                str1 = str1+data[:-1]+' \G;'+'\n'
        if (data.startswith('SELECT') or data.startswith('UPDATE') or data.startswith('DELETE') or data.startswith('INSERT') or data.startswith('REPLACE') ):
                startIndex = content.index(data)
                endIndex = getEndingLinePosition(startIndex)
                str2 = getTheContent(startIndex, endIndex)
                str1 = str1+' EXPLAIN '+str2[:-1]+' \G;\n'

f2 = open('explain-query.txt', "w")
f2.write(str1)
f2.close()
