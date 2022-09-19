import hmac
import base64
import json
import time
from hashlib import sha1


def generate_signature(data: str) -> str:
    mac = hmac.new(bytes.fromhex("fbf98eb3a07a9042ee5593b10ce9f3286a69d4e2"), data.encode(), sha1)
    return base64.b64encode(b"\x32" + mac.digest()).decode("utf-8")


payload = json.dumps({
    "timestamp": int(time.time() * 1000)
})

print(generate_signature(payload))