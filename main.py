import db
import mfrc522
import network
import speaker
import squeezebox
import squeezebox
import time
import ujson
from machine import Pin, PWM


def read(reader):
    while True:
        stat, tag_type = reader.request(reader.REQIDL)
        if stat == reader.OK:
            stat, raw_uid = reader.anticoll()
            if stat == reader.OK:
                return '%02x%02x%02x%02x' % (
                        raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
    time.sleep(1)


def make_reader():
    return mfrc522.MFRC522(14, 13, 12, 2, 15)


def load_config():
    with open('config.json', 'r') as f:
        return ujson.load(f)

def connect(client, ssid, password):
    if not client.active():
        print("Activating WIFI Station mode")
        client.active(True)
    if not client.isconnected():
        print("Connecting to network")
        client.connect(ssid, password)
        while not client.isconnected():
            pass
    print("network config:", client.ifconfig())
    return client


def program_tracks(reader, sounder, config):
    speaker.ack_sound(sounder)
    print("Programming tracks")

    tracks = squeezebox.read_current_playlist(
        config['host'], config['port'], config['player_id'])
    print("tracks: %s" % tracks)

    speaker.ack_sound(sounder)

    card_id = None
    while not card_id or card_id == config['master_card']:
        card_id = read(reader)
    db.save(card_id, {'tracks': tracks})
    print("save to card %s" % card_id)

    speaker.success_sound(sounder)
    time.sleep(5)

def main():
    config = load_config()
    reader = make_reader()
    sounder = PWM(Pin(4))
    network.WLAN(network.AP_IF).active(False) # disable access point
    client = network.WLAN(network.STA_IF)
    connect(client, config['ssid'], config['password'])
    while True:
        try:
            if not client.isconnected():
                connect(client, config['ssid'], config['password'])

            card_id = read(reader)

            if card_id == config['master_card']:
                print("master card detected")
                program_tracks(reader, sounder, config)
            elif card_id == config['pause_card']:
                print("pausing")
                squeezebox.pause(
                        config['host'],
                        config['port'],
                        config['player_id'])
                speaker.success_sound(sounder)
            else:
                print("card %s read" % card_id)
                speaker.ack_sound(sounder)
                data = db.load(card_id)
                if data and 'tracks' in data:
                    print("playing %s" % data['tracks'])
                    squeezebox.play(
                        config['host'],
                        config['port'],
                        config['player_id'],
                        data['tracks'])
                    speaker.success_sound(sounder)
        except Exception as e:
            speaker.fail_sound(sounder)
            print("EXCEPTION: %s" % e)
            time.sleep(5)

if __name__ == '__main__':
    main()

