from flask import Flask, render_template, request
from cipher import encrypt_custom, decrypt_custom
import string, random

app = Flask(__name__)

def generate_random_key(length):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    key = ""
    keylength = 8
    action = ""
    input_text = ""
    if request.method == 'POST':
        action = request.form.get('action')
        input_text = request.form.get('input_text')
        keylength_str = request.form.get('keylength')
        keylength = int(keylength_str) if keylength_str and keylength_str.isdigit() else 8
        key = request.form.get('key','')
        if action == 'Encrypt':
            key = generate_random_key(keylength)
            result = encrypt_custom(input_text, key)
        elif action == 'Decrypt':
            result = decrypt_custom(input_text, key)
    return render_template('index.html', result=result, key=key, keylength=keylength, action=action, input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)
