#!/usr/bin/env python3
"""UUID generator — v1 (time), v4 (random), v5 (name-based SHA1)."""
import sys, time, random, hashlib

def uuid4(rng=None):
    r = rng or random
    b = [r.randint(0,255) for _ in range(16)]
    b[6] = (b[6] & 0x0f) | 0x40  # version 4
    b[8] = (b[8] & 0x3f) | 0x80  # variant 1
    h = bytes(b).hex()
    return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:]}"

def uuid1():
    ts = int((time.time() + 12219292800) * 10000000)
    time_low = ts & 0xFFFFFFFF
    time_mid = (ts >> 32) & 0xFFFF
    time_hi = ((ts >> 48) & 0x0FFF) | 0x1000
    clock_seq = random.randint(0, 0x3FFF) | 0x8000
    node = random.getrandbits(48) | 0x010000000000
    return f"{time_low:08x}-{time_mid:04x}-{time_hi:04x}-{clock_seq:04x}-{node:012x}"

def uuid5(namespace, name):
    ns_bytes = bytes.fromhex(namespace.replace("-",""))
    h = hashlib.sha1(ns_bytes + name.encode()).digest()
    b = bytearray(h[:16])
    b[6] = (b[6] & 0x0f) | 0x50
    b[8] = (b[8] & 0x3f) | 0x80
    hx = bytes(b).hex()
    return f"{hx[:8]}-{hx[8:12]}-{hx[12:16]}-{hx[16:20]}-{hx[20:32]}"

def is_valid(uuid_str):
    parts = uuid_str.split("-")
    if len(parts) != 5: return False
    lengths = [8, 4, 4, 4, 12]
    return all(len(p) == l for p, l in zip(parts, lengths))

def version(uuid_str):
    return int(uuid_str.split("-")[2][0])

def test():
    random.seed(42)
    u4 = uuid4(random.Random(42))
    assert is_valid(u4)
    assert version(u4) == 4
    u1 = uuid1()
    assert is_valid(u1)
    assert version(u1) == 1
    DNS_NS = "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
    u5 = uuid5(DNS_NS, "example.com")
    assert is_valid(u5)
    assert version(u5) == 5
    assert uuid4() != uuid4()
    print("  uuid_gen: ALL TESTS PASSED")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else: print(f"UUID v4: {uuid4()}")
