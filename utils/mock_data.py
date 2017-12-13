import pymongo
import random

c = pymongo.MongoClient()
db = c.gamesdb

collection = "genres"
i = 0
g = ["Action", "Puzzle", "Dance-Dance-Revolution"]
for genre in g:
    entry = {"genre_name": genre,
             "genre_id": i,
             "genre_category": "category",
             "genre_category_id": i,
             "genre_description": "some description"}
    db[collection].insert_one(entry)
    i += 1

collection = "platforms"
i = 0
p = ["PC", "XBOX", "Playstation"]
for platform in p:
    entry = {"platform_name": platform,
             "platform_id": i}
    db[collection].insert_one(entry)
    i += 1

collection = "games"
gamelist = ["Super Mario Bros.", "Frogger", "Sonic the Hog"]
i = 0
for gam in gamelist:
    entry = {"platforms": p,
             "genres": g,
             "description": "Some description here",
             "title": gam,
             "moby_score": i,
             "game_id": i,
             "num"}
    db[collection].insert_one(entry)
    i += 1

collection = "reviews"
rand_reviews = ["Stunning", "A work of art", "Game of the Year", "Wow",
    "So-so", "A masterpiece", "Been done before", "Minor flaws but enjoyable",
    "Garbage", "Terrible", "A pile of junk", "Meh", "Poor controls",
    "Stunning graphics", "Lacking content"]

for game in db.games.find():
    print game
    for i in range(random.randint(3, 7)):
        review = {"game_title": game['title'],
                  "review_text": random.choice(rand_reviews),
                  "review_score": random.randint(1, 5)}

        db[collection].insert_one(review)

print("Finished!")
