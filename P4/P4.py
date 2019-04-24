input_file  = "sample1.txt"
INPF = open(input_file,"r")
line_count = 0
word_count = 0

char_array = []
for i in range (0,26):
    char_array.append(0)
    
def char_cnt(v):
    global char_array
    text = v.lower()
    for i in range (0, len(text)):
        k = ord(text[i]) - 97
        if k >= 0 and k <= 25:
            char_array[k] += 1

for line in INPF:
   words = line.split(' ')
   word_count += len(words)
   char_cnt(line)
   line_count += 1
INPF.close()

print("Total number of lines: %d" % line_count)
print("Total number of words: %d" % word_count)
for i in range (0,26):
    c = chr(i+97)
    print("%s : %3d" % (c, char_array[i]))
