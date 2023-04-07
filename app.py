from flask import *
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

app = Flask(__name__)
# @app.route("/")
# def hello_world():
#     return render_template("index.html")

@app.route("/elastic3")
def elastic():
   global useranswer
   global elastic_df
   global search_inpt
   if request.method=="POST":
       useranswer = request.form.get("abwh")
       search_inpt = request.form.get("seab")
       response = es.search(index="location" , query={"match":{useranswer:search_inpt}})
       elastic_docs = response["hits"]["hits"]
       print ("documents returned:",  len(response["hits"]["hits"]))
       fields = response
       elastic_df = pandas.DataFrame(fields)
       json_data = elastic_df.to_json()
       return json_data
   return render_template("index.html")
app.run()