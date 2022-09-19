import os
import hmac
from hashlib import sha1


def generate_device_id() -> str:
    identifier = os.urandom(20)
    key = bytes.fromhex("76b4a156aaccade137b8b1e77b435a81971fbd3e")
    mac = hmac.new(key, b"\x32" + identifier, sha1)
    return f"32{identifier.hex()}{mac.hexdigest()}"


print(generate_device_id())