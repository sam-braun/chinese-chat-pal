from flask import Flask, render_template, request, jsonify
import openai
from datetime import datetime
import jieba
from pypinyin import lazy_pinyin, Style
import logging

app = Flask(__name__)

# Set API key
openai.api_key = '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'

messages = [{"role": "system", "content": "You are a helpful assistant."}]

def write_pinyin(chinese_text):
    logging.getLogger('jieba').setLevel(logging.ERROR)

    # Use jieba to segment the Chinese text
    segments = jieba.lcut(chinese_text)

    # TONE is used to add tone marks
    return ' '.join([''.join(lazy_pinyin(segment, style=Style.TONE)) for segment in segments])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_message']
    translation, pinyin = True, True

    if 'toggle pinyin' in user_input.lower():
        pinyin = not pinyin

    if 'toggle translation' in user_input.lower():
        translation = not translation

    instruction = "Please respond in Simplified Mandarin."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages + [{"role": "user", "content": user_input + f' ({instruction})'}]
    )

    answer = response.choices[0].message['content']
    messages.append({"role": "assistant", "content": answer})

    formatted_answer = "中文: " + answer + "\nPīnyīn: " + write_pinyin(answer) 

    timestamp = datetime.now().strftime('%H:%M:%S')
    return jsonify({'response': formatted_answer, 'timestamp': timestamp})

if __name__ == '__main__':
    app.run(debug=True)