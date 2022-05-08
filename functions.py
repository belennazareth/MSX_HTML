import json

def checkmsx():
    
    try:
        f = open ("MSX.json")
        info = json.load (f)
        f.close
        return info
    
    except:
        print("ERROR")