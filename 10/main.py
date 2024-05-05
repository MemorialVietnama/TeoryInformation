
from flask import Flask, render_template, request
import heming
import binary

app = Flask(__name__)
hem = heming.Heming()

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/result', methods=['POST',])
def result():
    textarea_data = request.form['source_data']
    mode = int(request.form['mode'])

    if mode:
        data = binary.bin(textarea_data, mode)
        data = hem.code(data, mode)
    else:
        data = hem.code(textarea_data, mode)
        data = binary.bin(data, mode)

    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(debug = True)
