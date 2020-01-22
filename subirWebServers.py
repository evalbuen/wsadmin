import threading
import time
import sys as syspython
import java.lang.System  as  sys


class MyThread( threading.Thread ):
    threadID = 0

    def __init__(self, thread_id, ihs, node):
        threading.Thread.__init__( self )
        self.threadID = thread_id
        self.ihs = ihs
        self.node = node

    def run(self):
        print( "Inicia el proceso de subida de los WebServer a las " + time.ctime() )
        print( "Cellname: " + CellName )
        print( "Node: " + self.node )
        print( "IHS: " + self.ihs )
        AdminControl.invoke( mbean, 'start', '[%s %s %s]' % (CellName, self.node, self.ihs) )
        time.sleep( self.threadID )


mbean = AdminControl.queryNames( 'WebSphere:type=WebServer,*' )
CellName = AdminControl.getCell()

if __name__ == "__main__":
    threads = []
    thread_id = 0
    lineSeparator = sys.getProperty( 'line.separator' )
    webservers = []
    file = open( "/tmp/estado_ihs.txt", "r" )
    linea = file.readlines()
    print( linea )

    try:
        for fila in linea:
            array = fila.split( '|' )
            webserver = array[0].strip()
            print( webserver )
            node = array[1].strip()
            print( node )
            thread = MyThread( thread_id, webserver, node )
            threads.append( thread )
            time.sleep( 3 )
            thread_id = thread_id + 1
    except:
        print( "........YOU CANT HANDLE THE TRUE", syspython.exc_info() )

# start each thread roughly at the same time
for i in threads:
    i.start()

# synchronize all threads
for i in threads:
    i.join()

print( "Finaliza el proceso de subida de los WebServer a las " + time.ctime() )
