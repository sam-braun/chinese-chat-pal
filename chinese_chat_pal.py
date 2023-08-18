from flask import Flask, render_template, request, jsonify
import openai
from datetime import datetime

app = Flask(__name__)

# Set API key
openai.api_key = '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'

messages = [{"role": "system", "content": "You are a helpful assistant."}]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_message']
    translation, pinyin = True, True

    # Check for pinyin command
    if 'no pinyin' in user_input.lower():
        pinyin = False

    # Check for translation command
    if 'no translation' in user_input.lower():
        translation = False

    # Construct the model's instruction
    instruction = "Please respond in Simplified Mandarin."
    if pinyin:
        instruction += " Include pinyin in a separate new line."
    if translation:
        instruction += " Include an English translation in a separate new line."

    # Get GPT-3 response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages + [{"role": "user", "content": user_input + f' ({instruction})'}]
    )

    answer = response.choices[0].message['content']
    messages.append({"role": "assistant", "content": answer})

    # Split the answer for better presentation if necessary
    split_answers = answer.split('\n')
    formatted_answer = '<br>'.join(split_answers)

    # Add timestamp (this can also be done frontend, but here's the backend implementation)
    timestamp = datetime.now().strftime('%H:%M:%S')
    return jsonify({'response': formatted_answer, 'timestamp': timestamp})

if __name__ == '__main__':
    app.run(debug=True)
