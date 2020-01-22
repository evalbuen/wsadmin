import re
import sys as syspython
import time

import java.lang.System  as  sys

year, month, day, hour, min = map( int, time.strftime( "%Y %m %d %H %M" ).split() )

div = "\n********************************************************************************\n"


def guardarfile():
    file = open( "/tmp/estado_aplicaciones.txt", "w" )
    for i in range( 0, len( applications ) ):
        file.write( applications[i] + '\n' )
    file.close()


if __name__ == '__main__':

    print( "Inicia el proceso de listado: " + time.ctime() + "\n" )

    lineSeparator = sys.getProperty( 'line.separator' )
    Servidores = AdminTask.listServers( '-serverType APPLICATION_SERVER' ).split( lineSeparator )
    applications = []
    try:
        for Servidor in Servidores:
            datos = re.search( ".+c.+\/(\S.+)\/n.+s\/(\S.+)\/s.+s\/(\S.+)\|", Servidor )
            nombreCelda = datos.group( 1 )
            nombreNodo = datos.group( 2 )
            nombreServidor = datos.group( 3 )
            sid = AdminConfig.getid( "/Node:" + nombreNodo + "/Server:" + nombreServidor )
            if sid:
                estadoServidor = "RUNNING"
            else:
                estadoServidor = "STOPPED"
            text1 = (div +
                     "Servidor: " + nombreServidor + " - Nodo: " + nombreNodo + " - Estado: " + estadoServidor + div)
            print( text1 )
            applications.append( text1 )
            aplicaciones = AdminApp.list(
                "WebSphere:cell=" + nombreCelda + ",node=" + nombreNodo + ",server=" + nombreServidor ).split(
                lineSeparator )
            for aplicacion in aplicaciones:
                sidapp = AdminControl.queryNames(
                    "WebSphere:type=Application,name=" + aplicacion + ",process=" + nombreServidor + ",*" )
                if sidapp:
                    estadoAplicaciones = "RUNNING"
                else:
                    estadoAplicaciones = "STOPPPED"
                text2 = (
                        "La aplicacion: " + aplicacion + " se encuentra en estado: " + estadoAplicaciones)
                print( text2 )
                applications.append( text2 )
    except:
        print( "FAAAAACK ------> FULL!", syspython.exc_info() )
text3 = ("\n" + div + "\n" + "Finaliza el proceso de listado: " + time.ctime() + "\n" + div)
applications.append( text3 )
print( text3 )
guardarfile()
