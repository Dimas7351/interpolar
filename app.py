from flask import Flask, request, jsonify, render_template
from backend import linear_interpolation_search

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    print(data)
    arr = data.get('arr')
    target = data.get('target')

    print(arr)
    print(target)

    if (not arr) or (len(arr) == 0):
        return jsonify({'index': "Был введен пустой массив"})
    elif not target:
        return jsonify({'index': "Не было задано число для поиска"})
    else:
        result = linear_interpolation_search(arr, target)
        if result != -1:
            response = "Индекс найденного элемента: " + str(result)
        else:
            response = "Элемент не найден"
        return jsonify({'index': response})

if __name__ == '__main__':
    app.run(debug=True)
