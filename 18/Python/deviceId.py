import os
import hmac
from hashlib import sha1


def generate_device_id() -> str:
    identifier = os.urandom(20)
    key = bytes.fromhex("d19d2cb8468aac9b0ae16be4a6fa464be63760ce")
    mac = hmac.new(key, b"\x18" + identifier, sha1)
    return f"18{identifier.hex()}{mac.hexdigest()}"


print(generate_device_id())