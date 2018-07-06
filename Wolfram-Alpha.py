import wolframalpha

input = input("Question: ")
app_id = "Your_API_ID"
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print (answer)
