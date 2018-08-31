#reverse each words

i = raw_input("Enter a sentence:")

answer = " ".join(word[::-1] for word in i.strip().split())

print answer
