import requests

user_prompt ="Ironman flying in his suit,with using his hand"
url=f"https://image.pollinations.ai/prompt/{user_prompt}"

print(f"Generating for : {user_prompt}")

response = requests.get(url)

print(response)

if response.status_code == 200:
    with open("output.png", "wb") as f:
        f.write(response.content)
    print("success")
else:
    print("failed")    