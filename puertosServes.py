import java.lang.System  as  sys
import time
import threading
import sys as syspython
import re
from pprint import pprint as pp

year, month, day, hour, min = map( int, time.strftime( "%Y %m %d %H %M" ).split() )


def guardarfile():
    file = open( "/tmp/listado_puertos.txt", "w" )
    for i in range( 0, len( Puertos ) ):
        file.write( Puertos[i] + '\n' )
    file.close()


div = "********************************************************************"
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
                head1=("\n" + div + "\n" + ("Servidor: %s\t-\tNodo: %s" % (sname,nname)))
                Puertos.append(head1)
                head2=( div + "\n" + "Puerto:\t->\tNumero:\n" )
                Puertos.append(head2)
                nodo = ("-nodeName " + nname)
                pts = AdminTask.listServerPorts( sname, nodo ).split( lineSeparator )
                for puerto in pts:
                    datosPuerto = re.search(
                        "\[\[(\S.+) .+\[\[host (\S.*)\].+node (\S.+)\].+\[server (\S.+)\].+\[port (\w+)\].+\]\]",
                        puerto )
                    nombrePuerto = datosPuerto.group( 1 )
                    maquinaPuerto = datosPuerto.group( 2 )
                    nodoPuerto = datosPuerto.group( 3 )
                    servidorPuerto = datosPuerto.group( 4 )
                    numeroPuerto = datosPuerto.group( 5 )
                    text = ("%s\t->\t%s" % (nombrePuerto, numeroPuerto))
                    Puertos.append( text )
    except:
        print( "........YOU CANT HANDLE THE TRUE", syspython.exc_info() )
    cierre = ("\n" + div + "\nFinaliza el proceso de listado de puertos a las " + time.ctime() + "\n" + div + "\n")
    Puertos.append(cierre)
guardarfile()
