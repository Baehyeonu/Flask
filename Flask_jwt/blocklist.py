#블록리스트 관리

BLOCKLIST = set()

def add_to_blocklist(jti):
    BLOCKLIST.add(jti)

def remove_from_blocklist(jti):
    BLOCKLIST.discard(jti)