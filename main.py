text = input("String to decode to brainf**k code: ")
out = 10*"+" + "\n" + "[" + "".join(list(map(lambda x: ">" + int((x-x%10)/10) * "+" + "\n", list(map(lambda x: ord(x), list(text)))))) + len(text)*"<" + "-]\n" + "".join(list(map(lambda x: ">" + x%10*"+" + ".\n", list(map(lambda x: ord(x), list(text))))))
print(out)