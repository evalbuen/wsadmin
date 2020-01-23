import re
import sys as syspython
import threading
import time

import java.lang.System  as  sys


class MyThread( threading.Thread ):

    def __init__(self, ihs, node):
        threading.Thread.__init__( self )
        self.ihs = ihs
        self.node = node

    def run(self):
        self.detenerweb()

    def detenerweb(self):
        #        print( "Deteniendo el WebServer  " + self.node + " - " + self.ihs )
        #        print( "Fecha y hora actuales: " + time.ctime() )
        AdminControl.invoke( mbean, 'stop', '[%s %s %s]' % (CellName, self.node, self.ihs) )


def guardarfile():
    file = open( "/tmp/estado_ihs.txt", "w" )
    #    print( webservers )
    for i in range( 0, len( webservers ) ):
        file.write( webservers[i] + '\n' )
    file.close()

print( "Inicia el proceso de bajada de los WebServer a las " + time.ctime() )
mbean = AdminControl.queryNames( 'WebSphere:type=WebServer,*' )
CellName = AdminControl.getCell()

if __name__ == "__main__":
    threads = []
    lineSeparator = sys.getProperty( 'line.separator' )
    webservers = []
    listado = AdminConfig.list( 'WebServer' ).split()

    try:
        for web in listado:
            datos = re.search( "(\w+)\(.+nodes\/(\w.+)\/servers", web )
            sihs = datos.group( 1 )
            nihs = datos.group( 2 )
            stateihs = AdminControl.invoke( mbean, 'status', '[%s %s %s]' % (CellName, nihs, sihs) )
            #            print( "El IHS es: " + sihs + " del nodo: " + nihs )
            if stateihs == 'RUNNING':
                linea = sihs + "|" + nihs
                webservers.append( linea )
                t1 = MyThread( sihs, nihs )
                t1.start()
    except:
        print( "........YOU CANT HANDLE THE TRUE", syspython.exc_info() )
    guardarfile()

# start each thread roughly at the same time
for i in threads:
    i.start()

# synchronize all threads
for i in threads:
    i.join()

print( "Finaliza el proceso de bajada de los WebServer a las " + time.ctime() )
