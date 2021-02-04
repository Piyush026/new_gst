from pymongo import MongoClient
import urllib.parse

# username = urllib.parse.quote_plus('jack')
# password = urllib.parse.quote_plus("Mongo@123")

#url = "mongodb+srv://polo:" + urllib.parse.quote(
 #   "gvhjgv3456nb") + "@cluster0.b8rq1.mongodb.net/test?retryWrites=true&w=majority"
url = 'mongodb://localhost:27017'

cluster = MongoClient(url)
db = cluster['scraper']
collection = db['company_16l']
#mydict = {"name":"Piyush"}
#x = collection.insert_one(mydict)
#print(x)
# print(db)
lsttt = ["ASHIRVAD PIPES PRIVATE LIMITED ", "ASCO NUMATICS (INDIA) PRIVATE LIMITED ", "sdjzhcb",
         "ARMAN FINANCIAL SERVICES LIMITED"]


def searchData():
    result = collection.find()
    print("start")
    print(result)
    for document in result:
       print(document)
       # ioi = list(document.keys())[1]
        #print(ioi)
        #if ioi in lsttt:
         #   lsttt.remove(ioi)


#searchData()

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

