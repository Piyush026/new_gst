from pymongo import MongoClient
import urllib.parse

# username = urllib.parse.quote_plus('jack')
# password = urllib.parse.quote_plus("Mongo@123")

url = "mongodb+srv://polo:" + urllib.parse.quote(
    "gvhjgv3456nb") + "@cluster0.b8rq1.mongodb.net/test?retryWrites=true&w=majority"
# url is just an example (your url will be different)

cluster = MongoClient(url)
db = cluster['scraperdep']
collection = db['gst']

# print(db)
lsttt = ["ASHIRVAD PIPES PRIVATE LIMITED ", "ASCO NUMATICS (INDIA) PRIVATE LIMITED ", "sdjzhcb",
         "ARMAN FINANCIAL SERVICES LIMITED"]

orr = "mongodb+srv://polo:" + urllib.parse.quote(
    "gvhjgv3456nb") + "@cluster0.b8rq1.mongodb.net/scraper3"
uh = MongoClient(orr)
print(uh)
def searchData():
    result = collection.find({})
    for document in result:
        ioi = list(document.keys())[1]
        if ioi in lsttt:
            lsttt.remove(ioi)


# searchData()

# print(lsttt)


def insertData(pst1):
    try:
        collection.insert_one(pst1)
        print("data inserted")
    except Exception as e:
        print(e)

# from datetime import date
#
# today = date.today()
# print("Today's date:", today)
