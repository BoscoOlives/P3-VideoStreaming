# Joan Bosco Olives Florit NIA: 217056
import os


def hls(path):
    # http://underpop.online.fr/f/ffmpeg/help/hls-2.htm.gz
    os.system('ffmpeg -i '+path+' -c:v h264 -flags +cgop -g 30 -hls_time 1 out.m3u8')


def fragment(path):
    # Exercise 2
    # Fragments of 2000ms of the input video
    os.system('mp4fragment --fragment-duration 2000 '+path+' fragmented.mp4')
    # encryption example of https://www.bento4.com/developers/dash/encryption_and_drm/
    os.system('mp4encrypt --method '
              'MPEG-CENC --key '
              '1:a0a1a2a3a4a5a6a7a8a9aaabacadaeaf:0123456789abcdef --property '
              '1:KID:121a0fca0f1b475b8910297fa8e0a07e --key '
              '2:a0a1a2a3a4a5a6a7a8a9aaabacadaeaf:aaaaaaaabbbbbbbb --property '
              '2:KID:121a0fca0f1b475b8910297fa8e0a07e '
              'fragmented.mp4 '
              'encrypted.mp4')
    # dash file, this creats 'output' folder, if one already exists, delete this
    os.system('mp4dash --mpd-name mpdVideo.mpd encrypted.mp4')


def stream(path):
    # Exercise 3
    os.system('ffmpeg -re -i '+path+' -f mulaw -f mpegts udp://127.0.0.1:1234')
    # use ffplay.exe -i udp://127.0.0.1:1234 to play stream


def play_chunk(path):
    os.system('ffplay ' + path)

def main():
    path = 'BBB_10sec.mp4'
    while True:
        n = input("ENTER NUMBER\n1.- HLS\n2.- Stream in LOCAL\n3.- Fragment + Encrypt + DASH\n4.- Visualize Chunk"
                  "\n5.- Exit\n")
        n = int(n)
        # menu with case's
        match n:  # match function only works in python 3.10 or superior
            case 1:
                print("HLS Encoding")
                hls(path)

            case 2:
                print("Stream in LOCAL\n")
                print('This is an example for visualize this stream using Terminal: \n'
                      'ffplay.exe -i udp://127.0.0.1:1234 to play stream')
                stream(path)
                print('This is an example for visualize this stream using Terminal: '
                      'ffplay.exe -i udp://127.0.0.1:1234 to play stream')

            case 3:
                print("Fragment + Encrypt + DASH")
                fragment(path)

            case 4:
                chunk = input("Enter chunk link for visualize: ")
                play_chunk(chunk)
            case 5:
                print("Exit")
                return
            case _:
                print("You are introduced an invalid input, choose [1, 2, 3, 4 or 5 ]")
                main()


if __name__ == '__main__':

    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
