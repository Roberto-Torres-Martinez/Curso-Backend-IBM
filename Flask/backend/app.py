from flask import Flask, render_template, redirect, url_for
from cliente_dao import ClienteDAO
from cliente import Cliente
from cliente_form import ClienteForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'

titulo_app = 'Zona Fit (GYM)'

@app.route('/') #url: http://localhost:5000/
@app.route('/index.html')
def inicio():
    app.logger.debug('Entramos al path de inicio/')
    #Recuperamos los clientes de la db
    clientes_db = ClienteDAO.seleccionar()
    #Objeto de cliente form vacio
    cliente = Cliente()
    cliente_form = ClienteForm(obj=cliente)
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, form=cliente_form)

@app.route('/guardar', methods=['POST'])
def guardar():
    #Creamos objeto de cliente vacio
    cliente = Cliente()
    cliente_form = ClienteForm(obj=cliente)
    if cliente_form.validate_on_submit():
        #Llenamos el objeto cliente con valores de form
        cliente_form.populate_obj(cliente)
        if not cliente.id:    
            #Guardar nuevo cliente en db
            ClienteDAO.insertar(cliente)
        else:
            ClienteDAO.actualizar(cliente)
    #Redireccionar a inicio
    return redirect(url_for('inicio'))

@app.route('/limpiar')
def limpiar():
    return redirect(url_for('inicio'))

@app.route('/editar/<int:id>')
def editar(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    cliente_form = ClienteForm(obj=cliente)
    #Recuperar el listado de clientes para volver a mostrarlo
    clientes_db = ClienteDAO.seleccionar()
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, form=cliente_form)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    cliente = Cliente(id=id)
    ClienteDAO.eliminar(cliente)
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)