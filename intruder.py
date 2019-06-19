api_key = "2ce4c9c7-fdbe-4426-abcc-7bd94cf36fb5"
device_id = "BOLT7487076"
Threshold = 500
from boltiot import Bolt
import json, time
mybolt = Bolt(api_key, device_id)

while True:
#if (int(val["success"]) == 1):
    try:
        inp=mybolt.analogRead('A0')
        print(inp)
        val=json.loads(inp)
        v=val["value"]
        if ( int(v) < Threshold ):
            mybolt.digitalWrite(0,'HIGH')
        else:
            mybolt.digitalWrite(0,'LOW')
        time.sleep(30)
    except KeyboardInterrupt:
        break
