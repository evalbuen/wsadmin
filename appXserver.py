import java.lang.System  as  sys
import time
import sys as syspython

year, month, day, hour, min = map( int, time.strftime( "%Y %m %d %H %M" ).split() )

div = "********************************************************************************"

if __name__ == '__main__':

    print( "Inicia el proceso de listado: " + time.ctime() + "\n" )

    lineSeparator = sys.getProperty( 'line.separator' )
    CellName = AdminControl.getCell()
    celda = AdminConfig.getid( "/Cell:" + CellName )
    nodes = AdminConfig.list( "Node", celda ).split( lineSeparator )
    applications = []
    try:
        for node in nodes:
            cname = AdminConfig.showAttribute( celda, 'name' )
            nname = AdminConfig.showAttribute( node, 'name' )
            servs = AdminControl.queryNames( "type=Server,cell=" + cname + ",node=" + nname + ",*" ).split( lineSeparator )
            for server in servs:
                if server:
                    sname = AdminControl.getAttribute( server, 'name' )
                    ptype = AdminControl.getAttribute( server, 'processType' )
                    sstate = AdminControl.getAttribute( server, 'state' )
                    if ptype != 'NodeAgent' and ptype != 'DeploymentManager':
                        applications.append(
                            "\n" + div + "\n" + "Servidor: " + sname + " - " + "Nodo: " + nname + " Está en estado: " + sstate + "\n" + div )
                        pack1 = "WebSphere:cell=" + CellName + ",node=" + nname + ",server=" + sname
                        applications = AdminApp.list( pack1 ).split()
                        for app in applications:
                            pack2 = "WebSphere:type=Application,name=" + app + ",process=" + sname + ",*"
                            appstate = AdminControl.queryNames( pack2 )
                            if appstate:
                                estadoaplicacion = "RUNNING"
                            else:
                                estadoaplicacion = "STOPPED"
                            applications.append( "Aplicacion: " + app + "se encuentra en estado: " + estadoaplicacion )
    except:
        print( "FAAAAACK ------> FULL!", syspython.exc_info() )
    guardarfile()
    print( "\n" + div + "\n" + "Finaliza el proceso de listado: " + time.ctime() + "\n" + div )
