Analysis Done:
i)	The top n users who have tweeted the most related to the search string for the entire timeline 
ii)	The top n users who have tweeted the most for every hour
iii)	The top n users who have the maximum followers
iv)	The top n tweets which have the maximum retweet count

Tweepy is python library for accessing Twitter API. First part of the code is used to set all the credentials necessary to access data from Twitter’s public API. It then goes on to taking input from the user:
•	string to filter tweets 
•	time period for which tweets are needed.
One thing to note is Twitter public API will give tweets only from last 21 days. So giving random dates as inputs should technically should not return data but can’t comment about how tweepy cursor is defined or if it might have some special permissions.
Final part of the code gets tweets with filter criteria provided and takes only the user’s screen_name, time of tweet, text, users follower count, and tweets retweet count till current time and stores everything in a file with name your SearchString.txt

How to get my code running?
•	Place the data file (‘dota.txt’) in the same directory as snandu1.py (Analysis file)
•	I work on Jupyter notebooks. So, output for command prompt will first reqire you to run a command: chcp 65001 (ON WINDOWS)
o	Since twitter has Unicode characters and command prompt is not equipped to print that
•	Then just run the file and you should get the output on command prompt
•	Also, output is stored as csv files with ‘|’ as a separator. You will get all those files in the same folder. You will manually need to convert all those files
