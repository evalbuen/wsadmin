import time
import sys as syspython
import java.lang.System  as  sys
import re

year, month, day, hour, min = map( int, time.strftime( "%Y %m %d %H %M" ).split() )

# Variables
mbean = AdminControl.queryNames( 'WebSphere:type=WebServer,*' )
CellName = AdminControl.getCell()

if __name__ == "__main__":
    threads = []
    print( "Reporte generado en: " + time.ctime() )
    lineSeparator = sys.getProperty( 'line.separator' )
    webservers = []
    listado = AdminConfig.list( 'WebServer' ).split()

    try:
        for web in listado:
            datos = re.search( "(\w+)\(.+nodes\/(\w.+)\/servers", web )
            sihs = datos.group( 1 )
            nihs = datos.group( 2 )
            stateihs = AdminControl.invoke( mbean, 'status', '[%s %s %s]' % (CellName, nihs, sihs) )
            print( "El IHS es: " + sihs + " del nodo: " + nihs + " y su estado es: " + stateihs )
    except:
        print( "........YOU CANT HANDLE THE TRUE", syspython.exc_info() )
print( "Finaliza el informe a las " + time.ctime())