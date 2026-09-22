import subprocess
def target_scan(target, level):
    if (level == "Basic"):
        command = ["nmap", target]
    elif (level == "Normal"):
        command = ["nmap", "-sV", target]
    else: 
        command = ["nmap", "-A", target] 

    result = subprocess.run(command, capture_output = True, text = True)
    
    return result.stdout

