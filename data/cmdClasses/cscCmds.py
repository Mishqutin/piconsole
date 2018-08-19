class execClass:
    def cmdExec(line):
        global config
        if len(line)==0:
            return False
        elif line[0]=="/":
            args = line[1:].split()
            if args[0]=="host":
                config["users"][ClientIP]["cscConfig"]["host"] = args[1]
            elif args[0]=="port":
                config["users"][ClientIP]["cscConfig"]["port"] = int(args[1])
            elif args[0]=="pass":
                config["users"][ClientIP]["cscConfig"]["entryCode"] = args[1]
            saveConfig(config)
        else:
            cscCmds.client(line)

    ccConfig = {"name": config["users"][ClientIP]["name"],   "entryCode": config["users"][ClientIP]["cscConfig"]["entryCode"]}

    IP = (config["users"][ClientIP]["cscConfig"]["host"],    config["users"][ClientIP]["cscConfig"]["port"])

    def client(x):
        #if x[0]=="/":
            #reconnect(x[1:].split())
            #return 0

        # Connect to host
        try:
            s = socket.socket()
            s.connect(cscCmds.IP)
        except:
            print("Could not connect to server")
            return 1

        s.send(( cscCmds.ccConfig["name"]+"@"+cscCmds.ccConfig["entryCode"] ).encode())
        reply = (s.recv(16)).decode("ASCII")
        if reply!="ok":
            print("Access denied.")
            s.close()
            return 2


        # Send command as byte string
        s.send(x.encode())

        # Loop will end after disconnection
        while True:
            try:
                # Receive text and save as string
                txt = (s.recv(65536)).decode("ASCII")

                # Receiving empty string means that socket's closed
                if txt=="": break
                # Execute requested script from /scripts
                elif txt[0:3]=="#//":
                    # Script file name
                    cmd = txt.split()[0][3:]
                    # Additional arguments
                    args = txt.split()[1:]

                    # Script existence check
                    if os.path.isfile("scripts/{}.py".format(cmd)):
                        # Load script
                        f = open("scripts/{}.py".format(cmd), 'r')
                        code = f.read()
                        f.close()

                        # Execute it
                        exec(code, globals())
                    # Invalid script name
                    else:
                        print("Client: Invalid script file")
                # If received simple string then print it out to console
                else:
                    print(txtToHtml(txt))
            # If got any error (mainly by socket being closed) break the loop
            except: break

        # Disconnect
        s.close()
