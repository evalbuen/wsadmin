# ------------------------------------------------------
# get line separator
import java.lang.System  as  sys

lineSeparator = sys.getProperty( 'line.separator' )
cells = AdminConfig.list( 'Cell' ).split()
for cell in cells:
    # ----------------------------------------------------------------
    # lines 13 and 14 find all the nodes belonging to the cell and
    # process them at a time
    # -----------------------------------------------------------------
    nodes = AdminConfig.list( 'Node', cell ).split()
    for node in nodes:
        # --------------------------------------------------------------
        # lines 19-23 find all the running servers belonging to the cell
        # and node, and process them one at a time
        # --------------------------------------------------------------
        cname = AdminConfig.showAttribute( cell, 'name' )
        nname = AdminConfig.showAttribute( node, 'name' )
        servs = AdminControl.queryNames( 'type=Server,cell=' + cname + ',node=' + nname + ',*' ).split()
        print( "Number of running servers on node " + nname + ": %s \n" % (len( servs )) )
        for server in servs:
            # ---------------------------------------------------------
            # lines 28-34 get some attributes from the server to display;
            # invoke an operation on the server JVM to display a property.
            # ---------------------------------------------------------
            sname = AdminControl.getAttribute( server, 'name' )
            ptype = AdminControl.getAttribute( server, 'processType' )
            pid = AdminControl.getAttribute( server, 'pid' )
            state = AdminControl.getAttribute( server, 'state' )
            jvm = AdminControl.queryNames( 'type=JVM,cell=' + cname +
                                           ',node=' + nname + ',process=' + sname + ',*' )
            osname = AdminControl.invoke( jvm, 'getProperty', 'os.name' )
            print( " " + sname + " " + ptype + " has pid " + pid + "; state: " + state + "; on " + osname + "\n" )
            # ---------------------------------------------------------
            # line 40-45 find the applications running on this server and
            # display the application name.
            # ---------------------------------------------------------
            apps = AdminControl.queryNames( 'type=Application,cell=' + cname
                                            + ',node=' + nname + ',process=' + sname + ',*' ).splitlines()
            print( "Number of applications running on " + sname + ": %s \n" % (len( apps )) )
            for app in apps:
                aname = AdminControl.getAttribute( app, 'name' )
                print( aname + "\n" )
                print( "----------------------------------------------------" )
                print( "\n" )
