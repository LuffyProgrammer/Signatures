import hmac
import base64
import json
import time
from hashlib import sha1


def generate_signature(data: str) -> str:
    mac = hmac.new(bytes.fromhex("f8e7a61ac3f725941e3ac7cae2d688be97f30b93"), data.encode(), sha1)
    return base64.b64encode(b"\x42" + mac.digest()).decode("utf-8")


payload = json.dumps({
    "timestamp": int(time.time() * 1000)
})

print(generate_signature(payload))