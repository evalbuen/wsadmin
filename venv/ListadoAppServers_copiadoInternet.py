Running_Nodes = AdminControl.queryNames( '*:type=Server,name=nodeagent,*' ).split(
    java.lang.System.getProperty( "line.separator" ) )

print( "CELLNAME: ", AdminControl.getCell() )
print( "HOST:     ", AdminControl.getHost() )

ignorelist = ['dmgr', 'nodeagent']
for nod in Running_Nodes:
    NodeName = AdminControl.invoke( nod, "getNodeName()" )
    Running_JVMS = AdminControl.queryNames( '*:type=Server,node=' + NodeName + ',*' ).split(
        java.lang.System.getProperty( "line.separator" ) )
    print( "=====================================================================" )
    print( "NODENAME:", NodeName )
    print( "=====================================================================" )
    print( "--------------------------------------------" )
    print( "<< Running JVMs under the Node >>" )
    print( "--------------------------------------------" )
    for Serv in Running_JVMS:
        print( AdminControl.invoke( Serv, "getName()" ) )
    print( "--------------------------------------------" )
    print( "" )
    print( "" )
    print( "--------------------------------------------" )
    print( "<< Server Runtime Information >>" )
    print( "--------------------------------------------" )

    for JVM in Running_JVMS:
        ServerName = AdminControl.invoke( JVM, "getName()" )
        if ServerName not in ignorelist:
            JVMName = AdminControl.completeObjectName( 'type=JVM,process=' + ServerName + ',*' )
            JVMObject = AdminControl.makeObjectName( JVMName )
            perf = AdminControl.completeObjectName( 'type=Perf,process=' + ServerName + ',*' )
            perfObject = AdminControl.makeObjectName( perf )
            Obj = AdminControl.invoke_jmx( perfObject, "getStatsObject", [JVMObject, java.lang.Boolean( 'false' )],
                                           ['javax.management.ObjectName', 'java.lang.Boolean'] )
            current = Obj.getStatistic( 'HeapSize' ).getCurrent()
            used = Obj.getStatistic( 'UsedMemory' ).getCount()
            usage = float( used ) / float( current ) * 100
            uptime = float( Obj.getStatistic( 'UpTime' ).getCount() ) / 60 / 60 / 24
        print( "--------------------------------------------" )
        print( "ServerName      :", ServerName )
        print( "uptime(in days) :", int( uptime ) )
        print( "--------------------------------------------" )
        print( "CurrentUsage    :", current )
        print( "Usedmemory      :", used )
        print( "Usage in Percent:", int( usage ) )
        print( "--------------------------------------------" )
print( "" )
print( "=====================================================================" )
