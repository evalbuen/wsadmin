import java.lang.System  as  sys
import re
import time
import threading
import sys as syspython

year, month, day, hour, min = map( int, time.strftime( "%Y %m %d %H %M" ).split() )

lock = threading.Lock()

div = "********************************************************************************\n"


# def tprint(msg):
#    global lock
#    lock.acquire()
#    print( msg )
#    lock.release()


class MyThread( threading.Thread ):

    def __init__(self, node, server):
        threading.Thread.__init__( self )
        self.node = node
        self.server = server

    def run(self):
        self.detenerNA()

    def detenerNA(self):
        print("Acá llega a detener el nodeagent de: " + self.node)
#        AdminControl.stopServer( self.server, self.node, "immediate" )
        time.sleep( 1 )


def guardarfile():
    file = open( "/tmp/estado_nodes.txt", "w" )
    for i in range( 0, len( ListadoNodos ) ):
        file.write( ListadoNodos[i] + '\n' )
    file.close()


if __name__ == '__main__':

    lineSeparator = sys.getProperty( 'line.separator' )
    CellName = AdminControl.getCell()
    mbean = AdminControl.queryNames( 'WebSphere:type=NodeAgent,mbeanIdentifier=NodeAgent,*' ).split( lineSeparator )
    print( div + "PROGRAMA DE RESPALDO DE NODOS INICIADOS \n" + div )
    ListadoNodos = []
    detenerNodoAgent = []

    try:
        for nodo in mbean:
            datos = re.search( ".+p.+s=(\S.+),p.+,.+de=(\S.+),d.+ll=(\S+.),", nodo )
            snodo = datos.group( 1 )
            nnodo = datos.group( 2 )
            cnodo = datos.group( 3 )
            Linea = ("Agente: " + snodo + " del nodo: " + nnodo + " de la celda: " + cnodo)
            ListadoNodos.append( Linea )
            detenerNodoAgentThread = MyThread( nnodo, snodo )
            detenerNodoAgent.append( detenerNodoAgentThread )
            guardarfile()
    except:
        print( "........FAAAACK!", syspython.exc_info() )

# start each thread roughly at the same time
for i in detenerNodoAgent:
    i.start()

# synchronize all threads
for i in detenerNodoAgent:
    i.join()

print( "Finaliza el proceso de detencion de Agentes de Nodo: " + time.ctime() )
