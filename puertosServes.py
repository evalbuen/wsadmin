import java.lang.System  as  sys
import time
import threading
import sys as syspython
import re

year, month, day, hour, min = map( int, time.strftime( "%Y %m %d %H %M" ).split() )


def guardarfile():
    file = open( "/tmp/estado_web.txt", "w" )
    for i in range( 0, len( Puertos ) ):
        file.write( Puertos[i] + '\n' )
    file.close()


div = "**************************************************"
tipo = "WEB_SERVER"

if __name__ == "__main__":
    lineSeparator = sys.getProperty( 'line.separator' )
    Puertos = []
    Puertos.append( div )
    Puertos.append( div )
    Puertos.append( "Informe generado en " + time.ctime() )
    Puertos.append( div )
    Puertos.append( div + '\n' )

    Servers = AdminTask.listServers().split()
    try:
        for Servidores in Servers:
            datos = re.search( "(\w+)\(.+nodes\/(\w.+)\/servers", Servidores )
            sname = datos.group( 1 )
            nname = datos.group( 2 )
            stype = AdminTask.getServerType( ['-serverName', sname, '-nodeName', nname] )
            if stype != tipo:
                nodo = ("-nodeName " + nname)
                pts = AdminTask.listServerPorts( sname, nodo )
                text = (div + '\n' + "Server: " + sname + " - " + nname + '\n' + "Puertos: " + pts + '\n' + div + '\n')
                Puertos.append( text )
    except:
        print( "........YOU CANT HANDLE THE TRUE", syspython.exc_info() )

guardarfile()

print( "Finaliza el proceso de subida de los WebServer a las " + time.ctime() )
