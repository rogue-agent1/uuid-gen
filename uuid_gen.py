#!/usr/bin/env python3
"""uuid_gen - UUID v4/v1 generator and parser."""
import sys,os,time,random
def uuid4():
    b=bytearray(os.urandom(16));b[6]=(b[6]&0x0f)|0x40;b[8]=(b[8]&0x3f)|0x80
    h=b.hex();return f"{h[:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:]}"
def uuid1():
    t=int((time.time()+12219292800)*1e7);tl=t&0xffffffff;tm=(t>>32)&0xffff;th=(t>>48)&0x0fff|0x1000
    cs=random.randint(0,0x3fff)|0x8000;node=random.getrandbits(48)|0x010000000000
    return f"{tl:08x}-{tm:04x}-{th:04x}-{cs:04x}-{node:012x}"
def parse(u):
    u=u.replace("-","")
    if len(u)!=32:return None
    ver=int(u[12],16);variant=int(u[16],16)
    return{"version":ver,"variant":"RFC4122" if 8<=variant<=0xb else "other",
           "hex":u,"time_low":u[:8],"time_mid":u[8:12],"time_hi":u[12:16]}
if __name__=="__main__":
    cmd=sys.argv[1] if len(sys.argv)>1 else "v4"
    if cmd=="v4":
        n=int(sys.argv[2]) if len(sys.argv)>2 else 1
        for _ in range(n):print(uuid4())
    elif cmd=="v1":print(uuid1())
    elif cmd=="parse":
        info=parse(sys.argv[2])
        if info:
            for k,v in info.items():print(f"  {k}: {v}")
