import wikipedia

while True:
        ans = input("Question: ")
        wikipedia.set_lang("es")
        print (wikipedia.summary(ans, sentences=2))
