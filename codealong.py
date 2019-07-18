'''
In this program, we print out all the text data from our twitter JSON file.
Please explain the comments to students as you code.
'''

# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format
# students learned for their Survey Project!
import json
from wordcloud import WordCloud
from textblob import TextBlob
import matplotlib.pyplot as plt
# Next we want to open the JSON file. We tag this file as
# "r" read only because we are only going to look at the data.
tweetFile = open("tweets_small.json", "r")

# We use the JSON library to get data from the file as JSON data.
tweetData = json.load(tweetFile)
tweetFile.close()

#print(tweetData[1])

#FOR ALL ACCOUNTS
# sum = 0
# for i in range(0,len(tweetData)):
# 	if "favorite_count" in tweetData[i]:
# 		sum += tweetData[i]["favorite_count"]
# 	else:
# 		sum += 0
# 	t = sum/len(tweetData)
#
# print(t)

#FOR ACCOUNTS WITH FAVORITE COUNTS only
# sum = 0
# num = 0
# for tweet in tweetData:
# 	# tweet = tweetData[i]
# 	if "favorite_count" not in tweet:
# 		sum+= 0
# 	else:
# 		#print(tweet['favorite_count'])#TO SEE THEIR FAVORITE COUNT
# 		num += 1
# 		sum += tweet["favorite_count"]
# avg = sum/num
# print(avg)

#print(tweetData[0]['text'])
tweetlist = []
for i in range(len(tweetData)):
	tweetlist.append(tweetData[i]["text"])
	#tweetlist.append("           ")

polarityList = []
for item in tweetlist:
	blob1 = TextBlob(item)
	polar1 = blob1.polarity
	polarityList.append(polar1)

text = "hello hello there it me ngina"
wordcloud = WordCloud().generate(text)

tweetstring = ""
for tweet in tweetlist:
	tweet += " "
	tweetstring += tweet
print(tweetstring)
#print(polarityList)

plt.imshow(wordcloud, interpolation= 'bilinear')
plt.axis("off")
plt.show()
plt.savefig('alischart.png')

      #print(list(tweetData[0].keys()))#to print elements from our tweet data?
#['created_at', 'favorite_count', 'hashtags', 'id', 'id_str', 'lang', 'retweet_count', 'source', 'text', 'truncated', 'urls', 'user', 'user_mentions']

      #print(tweetData[0]["favorite_count"])
# # We can close the file now that we have locally stored the data.
# tweetFile.close()
#
# # We then print the data of ONE tweet:
# # the [0] denotes the *first* tweet object.
# # We access parts of the tweet using ["NameOfPart"].
# print("Tweet id: ", tweetData[0]["id"])
#
# # First ask students how they might print the text object:
# # Then show them the following code
# print("Tweet text: ", tweetData[0]["text"])
#
#
# # First ask students how might they use loops
# # to print the ["text"] of all the tweets:
#
# # Show them the following two options:
#
# # Explain how here, we're using index and
# # counting the number of tweets in the tweetData
# # using the python len() function.
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
# # Explain here how Python lets you get objects
# # directly without having to use an index.
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])
#
# # Encourage students to think about how there are
# # often multiple solutions for each problem, and
# # how each solution might have strenghts and drawbacks.
