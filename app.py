from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': '1',
  'title': 'Data Analyst',
  'location': 'Bengaluru',
  'salary': 'Rs 10,00,000'
}, {
  'id': '2',
  'title': 'Frontend Developer',
  'location': 'Chennai',
  'salary': 'Rs 8,00,000'
}, {
  'id': '3',
  'title': 'Data scientist',
  'location': 'Pune',
  'salary': 'Rs 15,00,000'
}]


@app.route('/')
def welcome_page():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
