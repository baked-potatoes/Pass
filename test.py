import requests

pnr = input("Enter pnr: ")

url = "https://pnr-status-indian-railway.p.rapidapi.com/pnr-check/"

key =  "2de2c68366msh3d9edfb8d2c1629p1c80f3jsn0a540a6f24e2" 
# calls database and fetches latest key

headers = {
	"X-RapidAPI-Key": key,
	"X-RapidAPI-Host": "pnr-status-indian-railway.p.rapidapi.com"
}

response = requests.request("GET", url+pnr, headers=headers)

print(response.text)