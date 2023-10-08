import os

import openai
from flask import Flask, redirect, render_template, request, url_for, jsonify

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

import utils.agent as agent


@app.route("/add-document", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})
        file = request.files["file"]

        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        
        # read_file = file.read()
        if file:
            return agent.delegate(file)
    
        # response = openai.Completion.create(
        #     model="text-davinci-003",
        #     prompt=generate_prompt(animal),
        #     temperature=0.6,
        # )
        # return redirect(url_for("index", result=response.choices[0].text))

    # result = request.args.get("result")
    result = process_file(uploaded_file)

    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )
