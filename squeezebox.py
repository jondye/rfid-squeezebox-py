import socket


def _cmd(host, port, cmd):
    addr = socket.getaddrinfo(host, port)[0][-1]
    s = socket.socket()
    s.connect(addr)
    try:
        s.send(bytes(cmd, 'utf-8'))
        return str(s.readline(), 'utf-8')
    finally:
        s.close()


def play(host, port, player_id, tracks):
    tracks_string=','.join(str(t) for t in tracks)
    cmd = '{id} playlistcontrol cmd:load track_id:{tracks}\n'.format(
            id=player_id,
            tracks=tracks_string)
    _cmd(host, port, cmd)


def read_current_playlist(host, port, player_id):
    cmd = '{id} status 0 100 tags:\n'.format(id=player_id)
    resp = _cmd(host, port, cmd)
    print("READ: %s" % resp)
    playlist = []
    for item in resp.split():
        item = item.split('%3A')
        if item[0] == 'id':
            playlist.append(int(item[1]))
    return playlist
