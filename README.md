## Joshs JSON Machine

- to run type `python3 Main.py` into your console
- Response should contain two sections
- The Submitted section is what got posted to the server
- The Post Response is included to tell the user that the post was successful

### Discussion

<u>Amount of Time Spent</u>

So to start I would like to say this took me over two hours. It was really not that difficult of a task however I am a perfectionist and I spent a good amount of time trying to design a system that I felt was easy to understand. I probably spent a total of 4 hours with most of the time going toward refactoring logic to files and functions that I felt where appropriate.

<u>Big O</u>

I worst case for my program is O(N) where N is the number of data points I was given. I iterate through equivalently sized lists a constant number of times and all house keeping is done using dictionaries which has constant insert and lookup. This will lead my program to have good linear time complexity.

<u>Interesting Stuff</u>

I designed my solution to using three python modules. The first is a main module that runs the program at a high level and communicates to the server. The next module is User module which consists of a class called User that encapsulates everything I think it means to be a User. I made logins a list of the User and established a dictionary of flags that could be extended to have extra functionality similar to the april_emails function. Lastly the ApiFunction module encapsulates the logic that gives the user of the program the results. The functions defined inside the module both build a dict of Users and query the dict to find out the things we are interested in.

<u>Weird Stuff</u>

1. I tried to not use any not standard python libraries so I would not have to have any sort of requirements file.
2. Because of this first constraint I stumbled into an odd problem. Check out the function inside User called timeZoneColonFix(). Look into the link I provided there. But the short of it is the timestamp strings that were provided in the response data does not follow the date time standard in python3.



I really had fun doing this so I hope you enjoy my code. 😎