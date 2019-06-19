api_key = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
device_id = "BOLTxxxxxxx"
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
