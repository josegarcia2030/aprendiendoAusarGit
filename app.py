from mimetypes import init
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL





app = Flask(__name__)


mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'GEEKBOY'
mysql.init_app(app)


@app.route('/')
def home():
    return render_template('empleado/index.html')

@app.route('/insertar')
def insertar():

    sql = "INSERT INTO `empleado` (`id`, `nombre`, `email`, `foto`) VALUES (NULL, 'rasek2030', 'Rasek2030@gmail.com', 'fotoDos.jpg');"
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute(sql)
    conexion.commit()

    return 'Se insertaron los registros'

if __name__ == '__main__':
    app.run(debug=True, port=5000)