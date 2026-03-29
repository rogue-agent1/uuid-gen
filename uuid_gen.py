#!/usr/bin/env python3
"""UUID generator. Zero dependencies."""
import os, time, hashlib

def uuid4():
    b = bytearray(os.urandom(16))
    b[6] = (b[6] & 0x0F) | 0x40  # version 4
    b[8] = (b[8] & 0x3F) | 0x80  # variant 1
    h = b.hex()
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:]}"

def uuid5(namespace, name):
    ns_bytes = bytes.fromhex(namespace.replace("-",""))
    h = hashlib.sha1(ns_bytes + name.encode()).digest()
    b = bytearray(h[:16])
    b[6] = (b[6] & 0x0F) | 0x50; b[8] = (b[8] & 0x3F) | 0x80
    hx = b.hex()
    return f"{hx[:8]}-{hx[8:12]}-{hx[12:16]}-{hx[16:20]}-{hx[20:32]}"

def uuid1_like():
    """Time-based UUID (simplified)."""
    t = int(time.time() * 1e7) + 0x01b21dd213814000
    b = bytearray(16)
    b[0:4] = (t & 0xFFFFFFFF).to_bytes(4, 'big')
    b[4:6] = ((t >> 32) & 0xFFFF).to_bytes(2, 'big')
    b[6:8] = ((t >> 48) & 0x0FFF | 0x1000).to_bytes(2, 'big')
    rand = os.urandom(8); b[8:] = rand
    b[8] = (b[8] & 0x3F) | 0x80
    hx = b.hex()
    return f"{hx[:8]}-{hx[8:12]}-{hx[12:16]}-{hx[16:20]}-{hx[20:]}"

def is_valid_uuid(s):
    s = s.replace("-","")
    if len(s) != 32: return False
    try: int(s, 16); return True
    except ValueError: return False

def uuid_version(s):
    return int(s.replace("-","")[12], 16)

if __name__ == "__main__":
    print(f"v4: {uuid4()}")
    print(f"v1: {uuid1_like()}")
