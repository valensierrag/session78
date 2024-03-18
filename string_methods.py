s = "hello world my name is John S"
s.capitalize()
s.center(40)
print(s.count(" "))  # number of words
s.replace(" ","!!")
s.split()

text = "abcdefg"
print(dir(text))
help(text.isidentifier)
print(text.isidentifier())
print("1234".isidentifier())
print("ananananananananananan".count("ana"))
print("ananananananananananan".replace("ana","banana"))
print("ananananananananananan".find("ana",1))
print("bbbbbbbabbbbbabbbbabbbb".split("a"))
print("this is a sentence and I want the words".split(" "))
sentence = "Hello, kind-sir, how may! I be of your service today?"
punctuation = ".,;!?-"
# sanitize the sentence
for p in punctuation:
    sentence = sentence.replace(p," ") #replace punctuation with nothing
print(sentence)
sentence = sentence.replace(" ","")
#split the sentence into words
words = sentence.split(" ")
print(words)

#find the links
s = "http://google.com and then there could be http://yahoo.com or even a website like http://bbc.co.uk"
start = 0
while True:
    start = s.find("http://", start)
    if start == -1:
        # If start is -1, it means no more occurrences of "http://" are found, and the loop is terminated with break.
        break
    end = s.find(" ",start)
    # finds index of the first space after the current occurrence of "http://".
    if end == -1:
    # no space is found, URL extends until the end of string, so it prints the URL and breaks out of the loop
        print(s[start:])
        break
    print(s[start:end])
    start = end

template = "Today is %s"
print(template % "Sunday")
print(45%5)
template = "%s I have seen %d %s."
print(template % ("On Monday", 7, "cats"))

hi = "Hello"
who = "World"
print(hi + " " + who)

print(hi + who[:3] + who[4:])
print(hi + " " + who[:3] + who[4:])
print((hi + who).upper())
print("racecar"[::-1])
print((3 * (hi + " ") + 5 * (who + ",")).replace(","," ").split(" "))
