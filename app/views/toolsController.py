# toolsController.py deals with the 'Tools' page and calls the tool functions used in the page
import logging
import subprocess
import sys
import shutil
import socket

from django.shortcuts import render



logger = logging.getLogger("VeraDemo:toolsController")

# Redirects request based on type
def tools(request):
    if(request.method == "GET"):
        return showTools(request)
    elif(request.method == "POST"):
        return processTools(request)

# Loads the tool webpage    
def showTools(request):
    request.host = ""
    return render(request, 'app/tools.html', {})

# Performs the actions on the tool page, updating output accordingly
def processTools(request):
    host = request.POST.get('host')
    fortunefile = request.POST.get('fortunefile')
    request.file = fortune(fortunefile) if fortunefile else ""
    request.host = host
    request.ping = ping(host) if host else ""
    
    

    return render(request, 'app/tools.html', {"host" : host})

# pings selected host and outputs the result
def ping(host):
    output = ""
    logger.info("Pinging " + host)
    try:
        p = subprocess.Popen(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        stdout, stderr = p.communicate(timeout=5)
    
        output = stdout.decode() if stdout else ""
        logger.info(output)
        logger.info("Exit Code:", p.returncode)
    except subprocess.TimeoutExpired:
        logger.error("Ping timed out")
        output = "ping: unknown host " + host
    except Exception as e:  
        logger.error("Error", e)
        output = "ping: unknown host " + host

    return output


# Produces a fortune based on the submitted selection
def fortune(file):
    cmd = f"/usr/games/fortune {file}"
    output = ""
    logger.info("Entering fortune")
    sys.stdout.flush()

    if shutil.which("fortune") is None:
        sys.stdout.flush()
        return "fortune not found"

    try: 
        p = subprocess.Popen(["bash", "-c", cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            stdout, stderr = p.communicate(timeout=5)
            output = stdout.decode() if stdout else ""
        except subprocess.TimeoutExpired:
            logger.error("Fortune timed out")
        except Exception as e:
            logger.error("Error", e)
    except Exception as e:
        logger.error("Error", e)
        
    return output




   