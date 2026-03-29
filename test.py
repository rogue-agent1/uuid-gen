from uuid_gen import uuid4, uuid5, uuid1_like, is_valid_uuid, uuid_version
u = uuid4()
assert len(u) == 36 and u.count("-") == 4
assert is_valid_uuid(u)
assert uuid_version(u) == 4
DNS_NS = "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
u5 = uuid5(DNS_NS, "example.com")
assert uuid_version(u5) == 5
u5b = uuid5(DNS_NS, "example.com")
assert u5 == u5b  # deterministic
u1 = uuid1_like()
assert is_valid_uuid(u1)
assert uuid_version(u1) == 1
assert not is_valid_uuid("not-a-uuid")
assert uuid4() != uuid4()
print("uuid_gen tests passed")
