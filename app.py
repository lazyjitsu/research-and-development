from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from ice_breaker import ice_breaker_with
import os
load_dotenv()
# os.environ['LANGSMITH_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGSMITH_API_KEY'] = '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'
# os.environ['OPENAI_API_KEY'] = '8w3qsMSZU5SfFBn4v7nT13M0WOXxaiFyM7M0TATsOJ2FuvUtY4dARPzjdDM3TbjpyQLOuLWWKDT3BlbkFJEgw1uyLqC6dASzCDPyrnQpYDM7ehbxkX5xjH3e9prGbcsbQ4fjYdNW'
# os.environ['LANGSMITH_PROJECT'] = "Break ICE"
from langsmith import Client
import os

client = Client(api_key=os.environ['LANGSMITH_API_KEY'])
app = Flask(__name__)
#0333323333222
print('OS ENV',os.environ["LANGSMITH_API_KEY"])
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process",methods=["POST"])
def process():
    name = request.form["name"]
    summary, profile_pic_url = ice_breaker_with(name=name)
    print('returning finallying ',profile_pic_url)
    return jsonify({
        "summary_and_facts": summary.to_dict(),
        "profile_url": profile_pic_url
    })
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
# Compare this snippet from output_parsers.py: