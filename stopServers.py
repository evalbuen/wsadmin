import sys as syspython
import threading
import time

import java.lang.System  as  sys

year, month, day, hour, min = map( int, time.strftime( "%Y %m %d %H %M" ).split() )


class MyThread( threading.Thread ):

    def __init__(self, thread_id, name, node, server):
        threading.Thread.__init__( self )
        self.thread_id = thread_id
        self.name = name
        self.node = node
        self.server = server

    def run(self):
        self.detener()

    def detener(self):
        print("Llega a detener el appserver: " + self.server)
#        AdminControl.stopServer( self.server, self.node, 'immediate' )


def guardarfile():
    file = open( "/tmp/estado.txt", "w" )
    for i in range( 0, len( servidores ) ):
        file.write( servidores[i] + '\n' )
    file.close()


print( "Inicia el proceso de bajada: " + time.ctime() )

lineSeparator = sys.getProperty( 'line.separator' )
CellName = AdminControl.getCell()
celda = AdminConfig.getid( "/Cell:" + CellName )
nodes = AdminConfig.list( "Node", celda ).split( lineSeparator )

servidores = []
try:
    for node in nodes:
        cname = AdminConfig.showAttribute( celda, 'name' )
        nname = AdminConfig.showAttribute( node, 'name' )
        servs = AdminControl.queryNames( "type=Server,cell=" + cname + ",node=" + nname + ",*" ).split( lineSeparator )

        for server in servs:
            if server:
                sname = AdminControl.getAttribute( server, 'name' )
                ptype = AdminControl.getAttribute( server, 'processType' )
                pid = AdminControl.getAttribute( server, 'pid' )
                state = AdminControl.getAttribute( server, 'state' )

                if ptype != 'NodeAgent' and ptype != 'DeploymentManager':
                    linea = (sname + "|" + nname)
                    servidores.append( linea )
                    t1 = MyThread( 1, "Thread_Stop_" + sname, nname, sname )
                    t1.start()
except:
    print( "........YOU CANT HANDLE THE TRUE", syspython.exc_info() )
guardarfile()
print( "Finaliza el proceso de detencion de servidores: " + time.ctime() )