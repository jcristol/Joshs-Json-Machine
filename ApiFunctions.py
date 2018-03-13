from User import User
import collections as cll

def emailList(emailToUserDict):
  """
  emailToUserDict - dict of all users maps from email to User (User objects) 
  returns - list of all the unique emails of the users
  """
  return [email for email in emailToUserDict.keys()]

def registerLogin(access, emailToUserDict):
  """
  access - dict like object {"email": "sjobs@apple.com", "login_date": "2014-04-10T11:22:33+00:00"}
  emailToUserDict - dict of all users maps from email to User (User objects) 
  returns - None
  """
  try:
    user = User(access['email'])
    if user.email in emailToUserDict:
      user = emailToUserDict[user.email]
    user.login(access['login_date'])
    emailToUserDict[user.email] = user
  except:
    pass


def usersPerDomain(emailToUserDict):
  """
  emailToUserDict - dict of all users maps from email to User (User objects) 
  returns - a dict of domains that have a user count greater than 1 
  """
  domains = cll.Counter()
  for _, user in emailToUserDict.items():
    domains[user.domain] += 1
  result = {}
  for domain, count in domains.items():
    if count > 1:
      result[domain] = count
  return result

def aprilUsers(emailToUserDict):
  """
  emailToUserDict - dict of all users maps from email to User (User objects) 
  returns - a list of all users who used the api in april (User objects)
  """
  return [email for email, user in emailToUserDict.items() if user.flags["visitedInApril"]]
