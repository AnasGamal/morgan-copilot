from .process_file import main
from flask import jsonify
# from .text_embed import embed_text
import openai

def generate_prompt(document, query):
    return (f"""
    Question:
    "{query}"

    Context:
    "{document}"
    """)

# when file is sent to backend, it is processed and sent to api
def delegate(file):
    processed_file = main(file)
    print('this is what we have processed here')
    print(processed_file)
    query = "Describe relevant laws mentioned in the document."
    # embedded = embed_text(processed_file)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(file, query),
        temperature=0.6,
    )

    return jsonify({'status': 'success', 'open_ai_response': response})

