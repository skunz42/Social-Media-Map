import sqlite3
import praw

reddit = praw.Reddit(client_id='vrZ4ypHWQ6oF-Q',
                         client_secret='kS-WA9nayjVVr4DHLnSuwygUOuE',
                         password='SiouxFalls187',
                         user_agent='mapping project by u/walebluber',
                         username='walebluber')

connection = sqlite3.connect("cities.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM city")
result = cursor.fetchall()

#cursor.execute("""UPDATE city set subname2 = ? WHERE fips = ?""", ('murfreesboro', 34980))

for r in result:
    if r[2] != None:
        #Do something
        subreddit = reddit.subreddit(r[2])
        #r[3] = subreddit.subscribers;
        numSubs = subreddit.subscribers;
        cursor.execute("""UPDATE city SET subs1 = ? WHERE subname1 = ?""", (numSubs, r[2]))
    if r[4] != None:
        #Do something
        subreddit = reddit.subreddit(r[4])
        numSubs = subreddit.subscribers;
        cursor.execute("""UPDATE city SET subs2 = ? WHERE subname2 = ?""", (numSubs, r[4]))
        #r[5] = subreddit.subscribers;
    if r[6] != None:
        #Do something
        subreddit = reddit.subreddit(r[6])
        numSubs = subreddit.subscribers;
        cursor.execute("""UPDATE city SET subs3 = ? WHERE subname3 = ?""", (numSubs, r[6]))
        #r[7] = subreddit.subscribers;
    connection.commit()
    print(r)

connection.commit()
connection.close()
