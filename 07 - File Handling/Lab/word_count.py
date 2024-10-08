# read words from words.txt
with open('words.txt', 'r') as f:
    words = f.read().split()

# count occurrences of words in text.txt
word_counts = {}
with open('text.txt', 'r') as f:
    text = f.read().lower()
    for line in text.splitlines():
        for word in line.split():
            word = word.strip('.,?!-')
            if word.lower() in words:
                word_counts[word] = word_counts.get(word, 0) + 1

# write results to output.txt
with open('output.txt', 'w') as f:
    for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
        f.write('{} - {}\n'.format(word, count))