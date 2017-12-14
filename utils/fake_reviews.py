import pymongo
import random

c = pymongo.MongoClient()
db = c.gamesdb

collection = "reviews"
count = 0

rand_reviews = ["Stunning", "A work of art", "Game of the Year", "Wow",
    "So-so", "A masterpiece", "Been done before", "Minor flaws but enjoyable",
    "Garbage", "Terrible", "A pile of junk", "Meh", "Poor controls",
    "Stunning graphics", "Lacking content"]

for game in db.games.find():
    for i in range(random.randint(3, 7)):
        review = {"game_title": game['title'],
                  "review_text": random.choice(rand_reviews),
                  "review_score": random.randint(1, 5)}

        db[collection].insert_one(review)

print("Finished!")
