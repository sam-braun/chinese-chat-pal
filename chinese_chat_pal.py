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

def chinese_to_pinyin(chinese_text):
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

    # User-selected options
    show_pinyin = request.json['show_pinyin']
    # show_translation = request.json['show_translation']
    show_simplified = request.json['show_simplified']

    # if 'toggle pinyin' in user_input.lower():
    #     pinyin = not pinyin


    chinese_char_style = 'Simplified' if show_simplified else 'Traditional'

    instruction = "Please respond in " + chinese_char_style + " Mandarin."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages + [{"role": "user", "content": user_input + f' ({instruction})'}]
    )

    answer_chinese = response.choices[0].message['content']
    messages.append({"role": "assistant", "content": answer_chinese})

    answer_pinyin = chinese_to_pinyin(answer_chinese)

    return jsonify({'chinese': answer_chinese, 'pinyin': answer_pinyin})

if __name__ == '__main__':
    app.run(debug=True)

