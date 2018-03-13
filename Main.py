import requests
import json
import ApiFunctions as api

apiUrl = " https://us-central1-marcy-playground.cloudfunctions.net/ordoroCodingTest"
r = requests.get(apiUrl)
if not r.ok:
  raise Exception("url down {}".format(apiUrl))
data = r.json()['data']

users = {} 
for access in data:
  api.registerLogin(access, users)

emails = api.emailList(users)
domains = api.usersPerDomain(users)
aprilBois = api.aprilUsers(users)

my_response = {
  "your_email_address" : "joshcristol@gmail.com",
  "unique_emails" : emails,
  "user_domain_counts" : dict(domains),
  "april_emails" : aprilBois
}

r = requests.post(apiUrl, json=my_response)
print("Submitted {}".format(json.dumps(my_response)), "\n")
print("Post Response {}".format(r), "\n")