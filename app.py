from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/mainPage')
def main_page():
  return render_template('mainPage.html', title='Main Page')


@app.route('/myWork')
def about_me_page():
  return render_template('myWork.html', title='My Work')


@app.route('/samplePost')
def sample_post_page():
  return render_template('samplePost.html', title='Sample Post')


@app.route('/aboutMe')
def aboutMe():
  return render_template('aboutMe.html', title='About Me')


@app.route('/reflection1')
def reflection1():
  return render_template('mainReflection1.html', title='Refliction 1')


@app.route('/reflection2')
def reflection2():
  return render_template('mainReflection2.html', title='Refliction 2')


@app.route('/reflection3')
def reflection3():
  return render_template('mainReflection3.html', title='Refliction 3')


@app.route('/reflection4')
def reflection4():
  return render_template('mainReflection4.html', title='Refliction 4')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
