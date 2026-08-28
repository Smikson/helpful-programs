import re

# Read input file
print('Reading input file')
file = open('joshua9.txt', 'r', errors='replace')
lines = file.readlines()
file.close()

# Iterate through file, remove bad ords and combine lines with no bad ords
print('Adjusting format')
badOrds = {239, 8218, 65533}
adjustedlines = []
current_line = ''
prefix = ['A) ', 'B) ', 'C) ', 'D) '] # Replace bad ords with ABCD
prefix_counter = 0
for line in lines:
    newline = False
    char_list = []
    for char in line:
        if ord(char) not in badOrds:
            char_list.append(char)
        else:
            newline = True
    adjusted = ''.join(char_list)

    # Remove starting number for start of question, create extra newline and reset current line
    adjusted = re.sub('^\\d+\\.\\s*','\\n\\n',adjusted.strip())
    if re.match('^\\d+\\.\\s*', adjusted.strip()):
        if current_line:
            adjustedlines.append(current_line)
            current_line = ''
    if newline:
        if current_line:
            adjustedlines.append(current_line)
        letter = prefix[prefix_counter % 4] # Select letter prefix
        prefix_counter += 1
        current_line = letter + adjusted
    else:
        current_line += ' ' + adjusted
# Add the last line, remove the unneeded extra spaces from the first line
adjustedlines.append(current_line)
adjustedlines[0] = adjustedlines[0].strip()

# Write the output to a file
print('Outputting the result')
outfile = open('joshua9_adjusted.txt', 'w')
outfile.write('\n'.join(adjustedlines))
outfile.close()
print('Done!')
