import hmac
import base64
import json
import time
from hashlib import sha1


def generate_signature(data: str) -> str:
    mac = hmac.new(bytes.fromhex("307c3c8cd389e69dc298d951341f88419a8377f4"), data.encode(), sha1)
    return base64.b64encode(b"\x22" + mac.digest()).decode("utf-8")


payload = json.dumps({
    "timestamp": int(time.time() * 1000)
})

print(generate_signature(payload))