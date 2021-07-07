from flask import Flask, render_template, flash,  request , redirect , url_for
from flask_mysqldb import MySQL
from wtforms import Form, StringField, validators
from wtforms.fields.html5 import EmailField
from utils import logger
app = Flask(__name__)

logger.info("Mysql connection starts")
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Harish'
app.config['MYSQL_DB'] = 'register'
# init MYSQL
mysql = MySQL(app)

logger.info("Index page")
#Index
@app.route('/')
def index():
    return render_template('home.html')

logger.info("This is Registration Class")
# Register Form Class
class RegisterForm(Form):
        firstName = StringField('firstName', [validators.DataRequired(), validators.DataRequired()])
        lastName = StringField('lastName', [validators.DataRequired(), validators.DataRequired()])
        email = EmailField('email', [validators.DataRequired(),validators.email()])
        logger.info("route file for get and post methods")
        # User Register
@app.route('/register', methods=[ 'Get','POST'])
def register():
    try:
            logger.info("Validation for values")
            form = RegisterForm(request.form)
            if request.method == 'POST' and form.validate():
                firstName = form.firstName.data
                lastName = form.lastName.data
                email = form.email.data
                logger.info("mysql Cursor begins")
                # Create cursor
                cur = mysql.connection.cursor()
                logger.info("Sql Query Insertion")
                logger.info("Sql Query Executions")
                # Execute query
                cur.execute("INSERT INTO users(firstName,lastName,email) VALUES( %s, %s, %s)", (firstName,lastName,email))
                logger.info("mysql connection commit")
                # Commit to DB
                mysql.connection.commit()

                # Close connection
                cur.close()
                logger.info("mysql Cursor ends")
                flash('You are now registered', 'success')
                return redirect(url_for('index'))
            return render_template('register.html', form=form)

    except Exception as objException:
        logger.debug("Error occured")
        print("Exception occured",objException)
logger.info("This is main method")
if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)