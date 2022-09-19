import os
import hmac
from hashlib import sha1


def generate_device_id() -> str:
    identifier = os.urandom(20)
    key = bytes.fromhex("02b258c63559d8804321c5d5065af320358d366f")
    mac = hmac.new(key, b"\x42" + identifier, sha1)
    return f"42{identifier.hex()}{mac.hexdigest()}"


print(generate_device_id())