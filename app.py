from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    student_name = request.form['student_name']
    roll_number = request.form['roll_number']
    marks_science = int(request.form['marks_science'])
    marks_social = int(request.form['marks_social'])
    marks_maths = int(request.form['marks_maths'])
    marks_kannada = int(request.form['marks_kannada'])
    marks_hindi = int(request.form['marks_hindi'])
    marks_english = int(request.form['marks_english'])

    total_marks = marks_science + marks_social + marks_maths + marks_kannada + marks_hindi + marks_english
    total_subjects = 6
    percentage = (total_marks / (total_subjects * 100)) * 100

    return render_template('index.html', student_name=student_name, roll_number=roll_number,
                           marks_science=marks_science, marks_social=marks_social, marks_maths=marks_maths,
                           marks_kannada=marks_kannada, marks_hindi=marks_hindi, marks_english=marks_english,
                           total_marks=total_marks, percentage=round(percentage, 2))

if __name__ == '__main__':
    app.run(debug=True)
