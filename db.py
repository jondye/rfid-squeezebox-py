import ujson

def load(key):
    try:
        with open("%s.json" % key, 'r') as f:
            return ujson.load(f)
    except OSError:
        return None

def save(key, data):
    with open("%s.json" % key, 'w') as f:
        f.write(ujson.dumps(data))
