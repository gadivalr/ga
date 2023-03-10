
from flask import Flask
from flask import render_template, request, redirect, session
from flaskext.mysql import MySQL
from datetime import datetime
from flask import send_from_directory
import os

app=Flask(__name__)
app.secret_key="clave_secreta"
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'sitio'
mysql.init_app(app)


@app.route("/css/<css>")
def css_link(css):
    return send_from_directory(os.path.join('templates/sitio/css'), css)
@app.route("/js/<js>")
def js_link(js):
    return send_from_directory(os.path.join('templates/sitio/js'), js)
@app.route("/fonts/<fonts>")
def fonts_link(fonts):
    return send_from_directory(os.path.join('templates/sitio/fonts'), fonts)

@app.route('/')
def inicio():
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `post`")
    post=cursor.fetchall()
    conexion.commit()
    print(post)
    return render_template('sitio/index.html',post=post)

@app.route('/img/<imagen>')
def imagen(imagen):
    return send_from_directory(os.path.join('templates/sitio/img'), imagen)

@app.route('/post')
def post():
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `post`")
    post=cursor.fetchall()
    conexion.commit()
    print(post)
    return render_template('sitio/post.html', post=post)

@app.route('/about')
def about():
    return render_template('sitio/about.html')

@app.route('/mangas')
def manga():
    return render_template('sitio/Mangas.html')

@app.route('/admin/')
def admin_index():
    if not session.get('login'):
        return redirect('/admin/login')
    return render_template('admin/indexadmin.html')

@app.route('/admin/login')
def admin_login(): 
    return render_template('admin/login.html')

@app.route('/admin/login/', methods=['POST'])
def admin_login_post():
    usuario = request.form['txtUsuario']
    password = request.form['txtPassword']
    print(usuario)
    print(password)
    if usuario == 'LeviS' and password == 'gadiel1999':
        session['login'] = True
        session['usuario'] = "Administrador"
        return redirect('/admin/')
    return redirect('/admin/login')

@app.route('/admin/cerrar')
def admin_cerrar():
    session.clear()
    return redirect('/')

@app.route('/admin/post')
def admin_post():
    if not session.get('login'):
        return redirect('/admin/login')
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `post`")
    post=cursor.fetchall()
    conexion.commit()
    print(post)
    return render_template('admin/post.html',npost=post)

@app.route('/admin/post/guardar', methods=['POST'])
def admin_post_guardar():
    if not session.get('login'):
        return redirect('/admin/login')
    titulo = request.form['txtNombre']
    fecha = request.form['txtFecha']
    imagen = request.files['txtImagen']
    descripcion = request.form['txtDescripcion']
    contenido = request.form['txtContenido']
    contenidoo=contenido
    tags = request.form['txtTag']
    tiempo=datetime.now()
    horaActual=tiempo.strftime("%Y%H%M%S")
    
    if imagen.filename != '':
        nuevoNombreImagen=horaActual+"_"+imagen.filename
        imagen.save("templates/sitio/img/"+nuevoNombreImagen)

    sql= "INSERT INTO `post` (`id`, `nombre`, `fecha`, `descripcion`, `imagen`, `contenido`, `tag`) VALUES (NULL, %s, %s, %s,%s,%s,%s);"
    

    datos=(titulo,fecha,descripcion,nuevoNombreImagen,contenidoo,tags)
    
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()
    
    print(titulo)
    print(fecha)
    print(imagen)
    print(descripcion)
    return redirect('/admin/post')

@app.route('/admin/post/delete', methods=['POST'])
def admin_post_delete():
    if not session.get('login'):
        return redirect('/admin/login')
    id = request.form['txtID']
    print(id)
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT imagen FROM `post` WHERE id=%s",(id))
    post=cursor.fetchall()
    conexion.commit()
    print(post)
    
    if os.path.exists("templates/sitio/img/"+str(post[0][0])):    
        os.unlink("templates/sitio/img/"+str(post[0][0]))
    
    
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("DELETE FROM `post` WHERE id=%s",(id))
    conexion.commit()
    
    
    return redirect('/admin/post')
@app.route("/blog/<nombre>")
def blog(nombre):
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `post` WHERE nombre=%s",(nombre))
    post=cursor.fetchall()
    conexion.commit()
    print(post)
    return render_template('sitio/blog2.html',post=post)



if __name__ == '__main__':
    app.run(debug=True)
