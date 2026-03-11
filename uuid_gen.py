#!/usr/bin/env python3
"""UUID generator — v1, v4, v5, and ULID."""
import sys, uuid, time, random, string
def ulid():
    t = int(time.time() * 1000)
    ts = ""
    for _ in range(10):
        ts = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"[t & 31] + ts; t >>= 5
    rand = "".join(random.choice("0123456789ABCDEFGHJKMNPQRSTVWXYZ") for _ in range(16))
    return ts + rand
if __name__ == "__main__":
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    kind = sys.argv[1] if len(sys.argv) > 1 else "v4"
    for _ in range(n):
        if kind == "v1": print(uuid.uuid1())
        elif kind == "v4": print(uuid.uuid4())
        elif kind == "v5": print(uuid.uuid5(uuid.NAMESPACE_DNS, sys.argv[3] if len(sys.argv) > 3 else "example.com"))
        elif kind == "ulid": print(ulid())
        else: print(uuid.uuid4())
