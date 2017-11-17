import re
import datetime
import operator

# match = re.search(r'iii[a-zA-Z0-9:\-_]+', ' piii_0-g as')
# print ('\'' + match.group() + '\'')

filename = '/Users/jai1/temp/logFile'
testPattern=r'Test::[a-zA-Z0-9:_]+'
datePattern=r'\d{2}:\d{2}:\d{2}'
file = open(filename, 'r')
firstMatchDict = {}
lastMatchDict = {}
for line in file:
    dateMatch = re.search(datePattern, line)
    if not dateMatch:
        continue
    time = datetime.datetime.strptime(dateMatch.group(), '%H:%M:%S')
    match = re.search(testPattern, line)
    if match:
        if match.group() not in firstMatchDict:
            firstMatchDict[match.group()] = time
        lastMatchDict[match.group()] = time

diffTimeDict = {}
for test in firstMatchDict:
    timeDiffSeconds = (lastMatchDict[test] - firstMatchDict[test]).total_seconds()
    if timeDiffSeconds < 0:
        timeDiffSeconds += 86400
    diffTimeDict[test] = timeDiffSeconds

sred = sorted([(value,key) for (key,value) in diffTimeDict.items()])

for items in sred:
    print(items[0], items[1])
