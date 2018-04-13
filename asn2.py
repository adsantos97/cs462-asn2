_author_ = 'arizza santos'

import random

def generate_num(n):
    for x in range(n):
        print random.randint(1, n+1)

def main():
    print("Generating random numbers")
    generate_num(10)


main()

sentence = "the world is mine"
words = sentence.split()
word_lengths = []
for word in words:
  if word != "the":
    word_lengths.append(len(word))
print(word_lengths)
