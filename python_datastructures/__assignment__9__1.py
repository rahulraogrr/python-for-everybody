# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the
# mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
# they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum
# loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
greatest_no_email_sender = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith("From:"):
        continue
    line_list = line.split()
    greatest_no_email_sender[line_list[1]] = greatest_no_email_sender.get(line_list[1], 0) + 1

big_count = None
big_word = None
for word,count in greatest_no_email_sender.items():
    if big_count is None or count > big_count:
        big_word = word
        big_count = count

print(big_word, big_count)
