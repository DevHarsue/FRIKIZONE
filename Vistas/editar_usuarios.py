from submain import MainWindow
from Validacion.validador import Validador
from Validacion.hash import texto_a_hash,texto_a_hash_salt
from conexion_bd.tablas import TablaUsuarios

class VistaEditarUsuarios:
    def __init__(self, ventana: MainWindow):
        self.ventana = ventana
        self.ui = ventana.ui
        self.validador = Validador()
        self.validador.usuarios(self.ui.line_usuario)
        self.ui.boton_buscar_usuario.pressed.connect(self.buscar)
        self.ui.boton_actualizar_usuario.pressed.connect(self.actualizar)
        self.ui.boton_borrar_usuario.pressed.connect(self.borrar)
        self.ui.line_usuario.textChanged.connect(self.reiniciar)
    
    def buscar(self):
        usuario = self.ui.line_usuario.text().upper()
        if usuario =="":
            self.ventana.mostrar_mensaje("Usuario Vacio","El campo usuario no puede estar vacio")
            return 0
        
        usuario = TablaUsuarios().select_usuario(texto_a_hash(usuario))
        if not bool(usuario):
            self.ventana.mostrar_mensaje("Usuario no encontrado","El usuario no existe")
            return 0
    
        self.usuario = usuario[0]
        
        if self.ventana.rol != texto_a_hash_salt("SUPERADMIN"):
            if self.usuario.usuario_rol == texto_a_hash_salt("SUPERADMIN"):
                self.ventana.mostrar_mensaje("Sin Permisos","No tienes los permisos para editar este usuario")
                return 0
        
        self.ui.line_contrasena.setEnabled(True)
        self.ui.line_confirmar.setEnabled(True)
        self.ui.boton_actualizar_usuario.setEnabled(True)
        if self.usuario.usuario_rol != texto_a_hash_salt("SUPERADMIN"):
            self.ui.boton_borrar_usuario.setEnabled(True)
    
    def actualizar(self):
        contrasena = self.ui.line_contrasena.text()
        confirmar = self.ui.line_confirmar.text()
        
        if contrasena=="" or confirmar=="":
            self.ventana.mostrar_mensaje("Campos Vacios","Rellene todos los campos")
            return 0
        
        if not self.validador.comprobar_contraseña(contrasena):
            self.ventana.mostrar_mensaje("Contraseña Invalida", "La contraseña debe:\n-Conteneral menos una letra mayuscula y una minuscula\n-Contener dos digitos\n-Contener un caracter especial\n-Ser minima de 8 caracteres")
            return 0
        
        if contrasena!=confirmar:
            self.ventana.mostrar_mensaje("Contraseñas Diferentes","Las contraseñas no coinciden")
            return 0
        
        self.ventana.preguntar("Actualizar Usuario","¿Estas seguro de actualizar el usuario?")
        if not self.ventana.respuesta:
            return 0
        
        TablaUsuarios().update(self.usuario.id,{"usuario_contraseña":texto_a_hash(contrasena)})
        self.ventana.mostrar_mensaje("Usuario Actualizada","Usuario Actualizado Correctamente")
        self.reiniciar()
    
    def borrar(self):
        self.ventana.preguntar("Borrar Usuario","¿Estas seguro de borrar usuario?")
        if not self.ventana.respuesta:
            return 0
        TablaUsuarios().delete(self.usuario.id)
        self.ventana.mostrar_mensaje("Usuario Borrado","Usuario Borrado Correctamente")
        self.reiniciar()
    
    def reiniciar(self):
        self.ui.line_contrasena.setEnabled(False)
        self.ui.line_confirmar.setEnabled(False)
        self.ui.boton_actualizar_usuario.setEnabled(False)
        self.ui.boton_borrar_usuario.setEnabled(False)
        self.ui.line_contrasena.setText("")
        self.ui.line_confirmar.setText("")
