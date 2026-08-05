import csv
import os

from flask import Flask, render_template, request, redirect, url_for, session
import datetime

from services.loader import load_manifest, load_all_chunks
from services.retriever import retrieve_chunks, format_sources
from services.llm import call_llm

app = Flask(__name__)

app.secret_key = os.getenv("FLASK_SECRET_KEY")



@app.get('/')
def home():  # put application's code here

    question = session.pop('question', '')
    sources = session.pop('sources', '')
    answer = session.pop('answer', '')

    titles = ['', '', '']

    if question:
        titles = ['Your question:', 'RAG\'s sources:', 'CHATbot\'s answer:']

    return render_template("index.html",
                           question=question,
                           sources=sources,
                           answer=answer,
                           titles=titles
                           )

@app.post('/')
def asking():

    question = request.form.get('ask','').strip()

    if not question:
        return redirect(url_for('home'))

    manifest = load_manifest()
    chunks = load_all_chunks()

    selected_chunks = retrieve_chunks(question, chunks, manifest)

    sources = format_sources(selected_chunks)
    answer = call_llm(question, selected_chunks)

    try:
        memory(question, answer)
    except OSError as error:
        print(f"MEMORY WRITE FAILED: {error!r}")

    session['question'] = question
    session['sources'] = sources
    session['answer'] = answer

    return redirect(url_for('home'))

def memory(ask, answ):
    file_path = 'data/memory.csv'
    field_names = ['Date_time', 'Question', 'Answer']
    file_exist = os.path.isfile(file_path)
    formated_answer = answ.replace('\n',' ').replace('\t',' ').strip()
    with open('data/memory.csv', 'a', encoding='utf-8', newline='') as memo:
        csv_writer = csv.DictWriter(memo, fieldnames=field_names, quoting=csv.QUOTE_ALL, delimiter=';')
        if not file_exist or os.stat(file_path).st_size == 0:
            csv_writer.writeheader()
        csv_writer.writerow({'Date_time': datetime.datetime.now(), 'Question': ask, 'Answer': formated_answer})

if __name__ == '__main__':
    app.run(debug=True)
