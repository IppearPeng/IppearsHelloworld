from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # 假设我们接收一个名为 'data' 的字段
    data = request.form['data']
    # 进行一些处理（例如，数据存储、计算等）
    processed_data = f"Processed: {data}"
    return jsonify(result=processed_data)

if __name__ == '__main__':
    app.run(debug=True)
