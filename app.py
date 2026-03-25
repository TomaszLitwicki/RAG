from flask import Flask, render_template, request, redirect, url_for, session
import datetime
from pathlib import Path

from services.loader import load_manifest, load_all_chunks
from services.retriever import retrieve_chunks, format_sources

app = Flask(__name__)

app.secret_key = 'Really_secret_key'



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
    answer = 'Here will be answer to your question'

    memory(question, answer)

    session['question'] = question
    session['sources'] = sources
    session['answer'] = answer

    return redirect(url_for('home'))

def memory(ask, answ):
    with open('data/memory.csv', 'a') as memo:
        memo.write(f'{datetime.datetime.now()}\t{ask}\t{answ}\n')

if __name__ == '__main__':
    app.run(debug=True)
