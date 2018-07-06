import wikipedia
import wolframalpha

while True:
    ans = input("Question: ")

    try:
        #wolframalpha
        app_id = "Your_API_ID"
        client = wolframalpha.Client(app_id)
        res = client.query(ans)
        answer = next(res.results).text
        print (answer)
    except:
        #wikipedia
        print (wikipedia.summary(ans))
