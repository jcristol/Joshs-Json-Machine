from __future__ import print_function
import sys
import datetime as dt


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

class User:

  @staticmethod
  def aprilCheck(date):
    if date.month == 4:
      return True
    return False

  @staticmethod
  def validateData(*args):
    """
    standard data validator fail if any of the arguments are none or empty
    """
    for e in args:
      if e == None or e == "":
        return False
    return True

  @staticmethod
  def timeZoneColonFix(dateString):
    """
    So this might have been a red herring.
    But when I try and parse the dateString with something like datetime.strptime()
    and I give it the format string '%Y-%m-%dT%H:%M:%S%z' the %z cannot correctly parse the 
    timezone written in the format +HH:MM or -HH:MM. Instead the %z expects +HHMM or -HHMM. This
    issue talks about it a little more https://bugs.python.org/issue31800.

    So this function takes the colon out of that timezone string and thats that. There probably is a better
    fix in a non standard library but I didn't want to use anything outside of the python standard.
    """
    return dateString[:-3] + dateString[-2:]

  def __init__(self, email):
    if not User.validateData(email):
      eprint("Invalid Email {}".format(email))
      raise Exception()
    self.email = email
    self.userName = email.split('@')[0]
    self.domain = email.split('@')[1]
    self.logins = []
    self.flags = {"visitedInApril" : False}
  
  def login(self, timeString):
    if not User.validateData(timeString):
      eprint("Invalid Date {}".format(timeString))
      return
    date = dt.datetime.strptime(User.timeZoneColonFix(timeString), "%Y-%m-%dT%H:%M:%S%z")
    self.flags["visitedInApril"] = User.aprilCheck(date)
    self.logins += [date]
