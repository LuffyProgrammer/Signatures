import os
from hashlib import sha1


def generate_device_id() -> str:
    identifier = os.urandom(20)
    key = bytes.fromhex("e9af2d7f431e87a4f8c7b6f45efc04b7e5f0ea4f")
    final = bytes.fromhex("01") + identifier + key
    return f"01{identifier.hex().upper()}{sha1(final).hexdigest().upper()}"


print(generate_device_id())