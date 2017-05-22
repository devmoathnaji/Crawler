import string
import random
from pymongo import MongoClient


class MongoDbInsert:
    # this function just to generate random string code

    def id_generator(size = 6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    # you can change the project name and home page to what ever you want
    PROJECT_NAME = "www.moathnaji.com"
    HOME_PAGE = "www.moathnaji.com"
    client = MongoClient()
    db = client.test

    lines = []

    result = db.Crawler.insert_one(
        {
            "Project_Crawling": {
                "ProjectName": PROJECT_NAME,
                "Links": lines,
                "Home Page": HOME_PAGE,
                "Code": id_generator( )

            }
        }
    )

    with open("Crawler/crawled.txt") as file:
        for line in file:
            line = line.strip()
            lines.append(line)

        test = db.Crawler
        for doc in test.find():
            print(doc)
