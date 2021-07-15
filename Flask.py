from flask import Flask, request, render_template
import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "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"

app = Flask(__name__)

@app.route('/')
def intro():
    return render_template('IntroPage.html')


@app.route('/2nd_grade_summary')
def second_grade_summary():
    return render_template('index.html')

@app.route('/2nd_grade_summary', methods=['POST'])
def second_grade_summary_post():
    user_input = request.form['text']
    extra = "I rephrased this for my daughter, in plain language a second grader can understand:"
    # call the 2nd grade summary function
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input+"\n"+extra,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\"\"\""]
    )
    output= response.choices[0].text
    return render_template('index.html', output=output) 

@app.route('/TLDR')
def tldr():
    return render_template('index.html')

@app.route('/TLDR', methods=['POST'])
def tldr_post():
    user_input = request.form['text']
    extra = "tl;dr:"
    # call the 2nd grade summary function
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input+"\n"+extra,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\"\"\""]
    )
    output= response.choices[0].text
    return render_template('index.html', output=output)


@app.route('/ One_Line_Summary')
def one_line():
    return render_template('index.html')

@app.route('/ One_Line_Summary', methods=['POST'])
def one_line_post():
    user_input = request.form['text']
    extra = "One-sentence summary:"
    # call the 2nd grade summary function
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input+"\n"+extra,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\"\"\""]
    )
    output= response.choices[0].text
    return render_template('index.html', output=output)


@app.route('/sheesh', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text



if __name__ == '__main__':
    app.run(debug=True)