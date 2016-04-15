from HttpServer import Run_Server



if __name__ == '__main__':
        try:
            Run_Server()
        except KeyboardInterrupt:
            print "HTTP Server Stopped"
