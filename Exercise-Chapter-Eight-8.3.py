fhand = open('mbox.txt')
count = 0
words = []
week = ['Sat','Sun','Mon','Tue','Wed','Thu','Fri']
for line in fhand:
    words = line.split()
# print 'Debug:', words
    if len(words) >= 3  and words[2] in week  and  words[0] == 'From' :
        print(words[2])
