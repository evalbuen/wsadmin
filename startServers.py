import threading
import time

year, month, day, hour, min = map( int, time.strftime( "%Y %m %d %H %M" ).split() )

# lock to synchronize the message printing
lock = threading.Lock()


def tprint(msg):
    global lock
    lock.acquire()
    print( msg )
    lock.release()


# first step, extend the Thread object
class Test( threading.Thread ):
    threadID = 0

    # second step, override the constructor
    def __init__(self, thread_id, node, server):
        self.threadID = thread_id
        self.node = node
        self.server = server
        # make sure you invoke the parent constructor
        threading.Thread.__init__( self )

    # third step, implement the run(), which will be invoked
    # at the notation: thread.start()
    def run(self):
        print("Ingresa a subir el appserver: " + self.server)
#        AdminControl.startServer( self.server, self.node )
        time.sleep( self.threadID )


print( "Inicia el proceso de subida: " + time.ctime() )

if __name__ == "__main__":
    threads = []
    thread_id = 0
    file = open( "/tmp/estado.txt", "r" )
    linea = file.readlines()
    for fila in linea:
        array = fila.split( '|' )
        server = array[0].strip()
        node = array[1].strip()
        thread = Test( thread_id, node, server )
        threads.append( thread )
        time.sleep( 3 )
        thread_id = thread_id + 1

    # start each thread roughly at the same time
    for i in threads:
        i.start()

    # synchronize all threads
    for i in threads:
        i.join()

    tprint( "Finaliza el proceso de subida " + time.ctime() )
