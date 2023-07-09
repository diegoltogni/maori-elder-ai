import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        prompt = [
            {"role": "system", 
             "content": '''
                            You are a wise Maori, who wants to help people with mental health.
                            You also really want to educate people about maori culture and perhaps a few te reo words.
                        '''
             },
            {"role": "user", "content": question}
        ]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt,
            temperature=0.6
        )
        return redirect(url_for("index", result=response.choices[0].message.content))

    result = request.args.get("result")
    return render_template("index.html", result=result)
