from PyQt5 import QtWidgets, uic, QtCore  
from PyQt5.QtCore import QTimer
import pyodbc
import pandas as pd #libreria que permite exportar hacia excel



app = QtWidgets.QApplication([])   # Encargado de gestionar todas las interacciones con la interfaz gráfica de usuario.

login = uic.loadUi("ventana_01.ui")
entrar = uic.loadUi("ventana_06_7_01.ui")
error = uic.loadUi("ventana_03.ui")
registro = uic.loadUi("ventana_04.ui")
exito = uic.loadUi("ventana_05.ui")

def gui_login():
    name = login.lineEdit.text()
    password_input = login.lineEdit_2.text()
    if len(name)==0 or len(password_input)==0:
        login.label_5.setText("Ingrese todos los datos")
    else:
        # Conexion base de datos
        server = 'DESKTOP-A779937'
        database = 'BD_LOGIN4'
        username = 'sa'
        password = '123456'
        cnxn = pyodbc.connect(f'Driver=SQL Server;Server={server};Database={database};UID={username};PWD={password}')

        # Comprobar si existe el usuario en la base de datos
        cursor = cnxn.cursor()
        cursor.execute("SELECT usuario, contrasena FROM usuarios WHERE usuario=? AND contrasena=?", (name, password_input))
        row = cursor.fetchone()
        if row is not None:
            # Usuario encontrado, vaya a la siguiente pantalla
            entrar.show()
            login.show()
        else:
            # Usuario no encontrado, mostrar pantalla de error
            error.show()

def agregar_producto():
    # Obtener los datos del formulario
    nombre = entrar.line_NOMBRE.text()
    descripcion = entrar.line_DESCR.text()
    stock = entrar.line_STOCK.text()
    valor = entrar.line_VALO.text()
    codigo = entrar.line_COD.text()
    fecha_ex=entrar.line_VALO_4.text()
    fecha_com=entrar.line_VALO_3.text()
    fecha_ven=entrar.line_VALO_5.text()
    marca=entrar.line_VALO_6.text()
    # Conexion base de datos
    server = 'DESKTOP-A779937'
    database = 'BD_LOGIN4'
    username = 'sa'
    password = '123456'
    cnxn = pyodbc.connect(f'Driver=SQL Server;Server={server};Database={database};UID={username};PWD={password}')

    # Insertar los datos del producto en la base de datos
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO productos (COD_PRODUCTOS, NOMBRE, DESCRIPCION, STOCK, VALOR ,FECHA_EXPEDICION , FECHA_COMPRA ,FECHA_VENCIMIENTO , MARCA) VALUES (?, ?, ?, ?, ?,?,?,?,?)", (codigo, nombre, descripcion, stock, valor,fecha_ex,fecha_com,fecha_ven,marca))
    cnxn.commit()

    # Mostrar mensaje de éxito
    entrar.label_AGREGAR.setText("Producto agregado exitosamente")
    QTimer.singleShot(10000, lambda: entrar.label_AGREGAR.setText(""))

    # Limpiar los campos de entrada
    entrar.line_NOMBRE.setText("")
    entrar.line_DESCR.setText("")
    entrar.line_STOCK.setText("")
    entrar.line_VALO.setText("")
    entrar.line_COD.setText("")
    entrar.line_VALO_4.setText("")
    entrar.line_VALO_3.setText("")
    entrar.line_VALO_5.setText("")
    entrar.line_VALO_6.setText("")

def cargar_datos_productos():
    # Conexión a la base de datos
    server = 'DESKTOP-A779937'
    database = 'BD_LOGIN4'
    username = 'sa'
    password = '123456'
    cnxn = pyodbc.connect(f'Driver=SQL Server;Server={server};Database={database};UID={username};PWD={password}')

    # Consulta a la base de datos
    query = 'SELECT COD_PRODUCTOS, NOMBRE, DESCRIPCION, STOCK, VALOR FROM dbo.productos'
    cursor = cnxn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

    # Cargar los datos en la tabla de la interfaz gráfica
    table = entrar.table_PRODUCTO
    table.setColumnCount(len(data[0]))
    table.setRowCount(len(data))
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            table.setItem(i, j, QtWidgets.QTableWidgetItem(str(item)))


def refrescar_tabla():
    # Obtener la conexión a la base de datos
    server = 'DESKTOP-A779937'
    database = 'BD_LOGIN4'
    username = 'sa'
    password = '123456'
    cnxn = pyodbc.connect(f'Driver=SQL Server;Server={server};Database={database};UID={username};PWD={password}')

    # Ejecutar la consulta SQL
    query = 'SELECT COD_PRODUCTOS, NOMBRE, DESCRIPCION, STOCK, VALOR , FECHA_EXPEDICION , FECHA_COMPRA ,FECHA_VENCIMIENTO , MARCA FROM dbo.productos'
    cursor = cnxn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()

    # Limpiar la tabla
    table = entrar.table_PRODUCTO
    table.clearContents()

    # Cargar los nuevos datos en la tabla
    table.setRowCount(len(data))
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            table.setItem(i, j, QtWidgets.QTableWidgetItem(str(item)))

def actualizar_producto():
    # Obtener los datos del formulario
    nombre = entrar.line_NOMBRE_2.text()
    descripcion = entrar.line_DESCR_2.text()
    stock = entrar.line_STOCK_2.text()
    valor = entrar.line_VALO_2.text()
    actualizar= entrar.line_ACTUALIZAR.text()
    nombre1=entrar.line_ACTUALIZAR_2.text()
    # Conexion base de datos
    server = 'DESKTOP-A779937'
    database = 'BD_LOGIN4'
    username = 'sa'
    password = '123456'
    cnxn = pyodbc.connect(f'Driver=SQL Server;Server={server};Database={database};UID={username};PWD={password}')

    # Insertar los datos del producto en la base de datos
    cursor = cnxn.cursor()
    cursor.execute("UPDATE productos SET NOMBRE = ?, DESCRIPCION = ? ,STOCK = ? ,VALOR = ? WHERE COD_PRODUCTOS=? OR NOMBRE = ?", ( nombre, descripcion, stock, valor, actualizar,nombre1))
    cnxn.commit()

    # Mostrar mensaje de éxito
    entrar.label_AGREGAR_2.setText("Producto actualizado exitosamente")
    QTimer.singleShot(10000, lambda: entrar.label_AGREGAR_2.setText(""))

    # Limpiar los campos de entrada
    entrar.line_NOMBRE_2.setText("")
    entrar.line_DESCR_2.setText("")
    entrar.line_STOCK_2.setText("")
    entrar.line_VALO_2.setText("")



def buscar_boton_act_produc():
    actualizar= entrar.line_ACTUALIZAR.text()
    nombre1=entrar.line_ACTUALIZAR_2.text()

    # Conexion base de datos
    server = 'DESKTOP-A779937'
    database = 'BD_LOGIN4'
    username = 'sa'
    password = '123456'
    cnxn = pyodbc.connect(f'Driver=SQL Server;Server={server};Database={database};UID={username};PWD={password}')

    # Insertar los datos del producto en la base de datos
    cursor = cnxn.cursor()
    cursor.execute("SELECT NOMBRE, DESCRIPCION, STOCK, VALOR FROM dbo.productos WHERE  NOMBRE = ? OR COD_PRODUCTOS = ?", (nombre1,actualizar))
    
    data = cursor.fetchall()
    entrar.line_NOMBRE_2.setText(str(data[0][0]))
    entrar.line_DESCR_2.setText(str(data[0][1]))
    entrar.line_STOCK_2.setText(str(data[0][2]))
    entrar.line_VALO_2.setText(str(data[0][3]))




def eliminar_producto():
# Obtener los datos del formulario
    eliminar= entrar.line_ELIMINAR_CODIGO.text()
    # Conexion base de datos
    server = 'DESKTOP-A779937'
    database = 'BD_LOGIN4'
    username = 'sa'
    password = '123456'
    cnxn = pyodbc.connect(f'Driver=SQL Server;Server={server};Database={database};UID={username};PWD={password}')

    # Insertar los datos del producto en la base de datos
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM productos WHERE COD_PRODUCTOS = ?", (eliminar))
    cnxn.commit()

    print(eliminar)
    # Mostrar mensaje de éxito
    entrar.label_MENSAJE_ELIMINAR.setText("Producto eliminado exitosamente")
    QTimer.singleShot(10000, lambda: entrar.label_MENSAJE_ELIMINAR.setText(""))

    # Limpiar los campos de entrada
    entrar.line_COD.setText("")

def buscar_producto():
    # Obtener la conexión a la base de datos
    
    buscar= entrar.lineEdit_CODIGO_2.text()
    buscar1= entrar.lineEdit_CODIGO_3.text()
    buscar2= entrar.lineEdit_CODIGO_4.text()
    server = 'DESKTOP-A779937'
    database = 'BD_LOGIN4'
    username = 'sa'
    password = '123456'
    cnxn = pyodbc.connect(f'Driver=SQL Server;Server={server};Database={database};UID={username};PWD={password}')

    # Ejecutar la consulta SQL
    cursor = cnxn.cursor()
    cursor.execute("SELECT COD_PRODUCTOS, NOMBRE, DESCRIPCION, STOCK, VALOR , FECHA_EXPEDICION , FECHA_COMPRA ,FECHA_VENCIMIENTO , MARCA FROM dbo.productos WHERE COD_PRODUCTOS = ? or NOMBRE = ? or MARCA = ?", (buscar, buscar1, buscar2))

    data = cursor.fetchall()

    # Limpiar la tabla
    table = entrar.table_BUSCAR
    table.clearContents()

    # Cargar los nuevos datos en la tabla
    table.setRowCount(len(data))
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            table.setItem(i, j, QtWidgets.QTableWidgetItem(str(item)))


            
def reportes():
   # Conexión a la base de datos
    server = 'DESKTOP-A779937'
    database = 'BD_LOGIN4'
    username = 'sa'
    password = '123456'
    cnxn = pyodbc.connect(f'Driver=SQL Server;Server={server};Database={database};UID={username};PWD={password}')

    # Consulta a la base de datos
    query2= 'select COD_PRODUCTOS,NOMBRE, STOCK , VALOR , ACCION from dbo.reportes '
    cursor = cnxn.cursor()
    cursor.execute(query2)
    data = cursor.fetchall()

    # Cargar los datos en la tabla de la interfaz gráfica
    table = entrar.table_REPORTE
    table.setColumnCount(len(data[0]))
    table.setRowCount(len(data))
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            table.setItem(i, j, QtWidgets.QTableWidgetItem(str(item)))


def sumaa():
    nombre=entrar.line_agre_dismi_1.text()
    stock = entrar.line_STOCK_AGRE_DISMI.text()
    cantidad = int(entrar.line_CANTIDAD_AGRE_DISMI.text())
    # Conexion base de datos
    server = 'DESKTOP-A779937'
    database = 'BD_LOGIN4'
    username = 'sa'
    password = '123456'
    cnxn = pyodbc.connect(f'Driver=SQL Server;Server={server};Database={database};UID={username};PWD={password}')

    # Insertar los datos del producto en la base de datos
    cursor = cnxn.cursor()
    cursor.execute("update dbo.productos set STOCK = STOCK + " + str(cantidad) + "  where NOMBRE=? ", ( nombre))
    cnxn.commit()

    # Mostrar mensaje de éxito
    entrar.label_AGREGAR_3.setText("Producto actualizado exitosamente")
    QTimer.singleShot(10000, lambda: entrar.label_AGREGAR_3.setText(""))

    # Limpiar los campos de entrada
    entrar.line_STOCK_AGRE_DISMI.setText("")
    entrar.line_CANTIDAD_AGRE_DISMI.setText("")

def buscar_ag_dm():
    
    nombre=entrar.line_agre_dismi_1.text()

    # Conexion base de datos
    server = 'DESKTOP-A779937'
    database = 'BD_LOGIN4'
    username = 'sa'
    password = '123456'
    cnxn = pyodbc.connect(f'Driver=SQL Server;Server={server};Database={database};UID={username};PWD={password}')

    # Insertar los datos del producto en la base de datos
    cursor = cnxn.cursor()
    cursor.execute("SELECT STOCK FROM dbo.productos WHERE  NOMBRE = ? ", (nombre))
    
    data = cursor.fetchall()
    entrar.line_STOCK_AGRE_DISMI.setText(str(data[0][0]))
    
    entrar.line_CANTIDAD_AGRE_DISMI.setText("")

def rest():
    nombre=entrar.line_agre_dismi_1.text()
    stock = entrar.line_STOCK_AGRE_DISMI.text()
    cantidad = int(entrar.line_CANTIDAD_AGRE_DISMI.text())
    # Conexion base de datos
    server = 'DESKTOP-A779937'
    database = 'BD_LOGIN4'
    username = 'sa'
    password = '123456'
    cnxn = pyodbc.connect(f'Driver=SQL Server;Server={server};Database={database};UID={username};PWD={password}')

    # Insertar los datos del producto en la base de datos
    cursor = cnxn.cursor()
    cursor.execute("update dbo.productos set STOCK = STOCK - " + str(cantidad) + "  where NOMBRE=? ", ( nombre))
    cnxn.commit()

    # Mostrar mensaje de éxito
    entrar.label_AGREGAR_3.setText("Producto actualizado exitosamente")
    QTimer.singleShot(10000, lambda: entrar.label_AGREGAR_3.setText(""))

    # Limpiar los campos de entrada
    entrar.line_STOCK_AGRE_DISMI.setText("")
    entrar.line_CANTIDAD_AGRE_DISMI.setText("")
    
def exportar():
    server = 'DESKTOP-A779937'
    database = 'BD_LOGIN4'
    username = 'sa'
    password = '123456'
    cnxn = pyodbc.connect(f'Driver=SQL Server;Server={server};Database={database};UID={username};PWD={password}')

    # Insertar los datos del producto en la base de datos
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM dbo.productos')
    data = cursor.fetchall()
    df = pd.DataFrame(data)
    cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'productos'")
    column_names = [column[0] for column in cursor.description]
    df.columns = column_names
    df.to_excel('datos.xlsx', index=False)
    
def gui_entrar():
    login.hide()
    entrar.tabWidget.tab()
    entrar.show()


def gui_error():
    login.hide()
    error.show()


def gui_registro():
    login.hide()
    registro.show()


def regresar_entrar():
    entrar.hide()
    login.label_5.setText("")
    login.show()    

def regresar_error():
    error.hide()
    login.label_5.setText("")
    login.show() 
    error.pushButton.setEnabled(False)
    QtCore.QTimer.singleShot(10000, lambda: error.pushButton.setEnabled(True))
error.pushButton.clicked.connect(regresar_entrar)

def gui_registro():
    # Obtener los valores ingresados por el usuario 
    print("entro al registro")
    nombre = registro.lineEdit.text()
    apellido = registro.lineEdit_2.text()
    direccion = registro.lineEdit_3.text()
    rol = registro.lineEdit_4.text()
    numero = registro.lineEdit_5.text()
    usuario = registro.lineEdit_6.text()
    contrasena = registro.lineEdit_7.text()

    # Validar los valores ingresados por el usuario
    if len(nombre) == 0 or len(apellido) == 0 or len(direccion) == 0 or len(rol) == 0 or len(numero) == 0 or len(usuario) == 0 or len(contrasena) == 0:
        registro.label_12.setText("Ingrese todos los datos")
        registro.show()
        return

    # Conectar a la base de datos
    server = 'DESKTOP-A779937'
    database = 'BD_LOGIN4'
    username = 'sa'
    password = '123456'
    cnxn = pyodbc.connect(f'Driver=SQL Server;Server={server};Database={database};UID={username};PWD={password}')

    # Verificar si el usuario ya está registrado
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM registro_usuarios WHERE usuario = ?", (usuario,))
    rows = cursor.fetchall()
    if len(rows) > 0:
        registro.label_12.setText("El usuario ya está registrado")
        registro.show()
        return

    # Insertar los datos del registro en la tabla
    try:
        cursor = cnxn.cursor()
        cursor.execute("INSERT INTO registro_usuarios (nombre, apellido, direccion, rol, numero, usuario, contrasena) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (nombre, apellido, direccion, rol, numero, usuario, contrasena))
        cnxn.commit()
        # Validar que se haya insertado el registro correctamente
        if cursor.rowcount == 1:
            # Si todo está bien, mostrar la ventana de éxito
            exito.show()
            registro.hide()
        else:
            registro.label_12.setText("Error al insertar registro")
            registro.show()

    except Exception as e:
        registro.label_12.setText("Error al insertar registro")
        registro.show()
        print(str(e))

    # Cerrar la conexión
    cursor.close()
    cnxn.close()

def regresar_registro():
    registro.hide()
    registro.label_12.setText("")
    login.show()  

def regresar_exito():
    exito.hide()
    login.show()

def regresar_login(self):
    # Ocultar la ventana actual y mostrar la ventana de login
    self.exito.hide()
    self.login.show()


def salir():
    app.exit()


login.pushButton.clicked.connect(gui_login)
login.pushButton_2.clicked.connect(gui_registro)
login.pushButton_3.clicked.connect(salir)  

entrar.Button_AGREGAR.clicked.connect(agregar_producto)
entrar.Button_SALIR.clicked.connect(salir)
entrar.ButtoN_REFRESCAR.clicked.connect(refrescar_tabla)
entrar.Button_ACTUALIZAR.clicked.connect(actualizar_producto)
entrar.Button_ELIMINAR.clicked.connect(eliminar_producto)
entrar.Button_BUSCAR.clicked.connect(buscar_producto)
entrar.bt_MOSTRAR_REPORTE.clicked.connect(reportes)
entrar.Button_BUSCAR_PRODUC.clicked.connect(buscar_boton_act_produc)
entrar.bt_BUSCAR_SUM_REST.clicked.connect(buscar_ag_dm)
entrar.bt_agregar.clicked.connect(sumaa)
entrar.bt_disminuir.clicked.connect(rest)
entrar.bt_exportar.clicked.connect(exportar)
error.pushButton.clicked.connect(regresar_error)
error.pushButton_3.clicked.connect(salir)

registro.pushButton.clicked.connect(regresar_registro)
registro.pushButton_2.clicked.connect(regresar_registro)
registro.pushButton.clicked.connect(gui_registro)
registro.pushButton_3.clicked.connect(salir) 

exito.pushButton.clicked.connect(regresar_exito)

login.show()
app.exec()
