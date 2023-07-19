import socket
from zlib import decompress
import pygame

WIDTH = 800
HEIGHT = 600

def recvall(conn, length):
    """ Retreive all pixels. """
    buf = b''
    while len(buf) < length:
        data = conn.recv(length - len(buf))
        if not data:
            return data
        buf += data
    return buf

def main(host='', port=6969):
    ''' machine lhost'''
    sock = socket.socket()
    sock.bind((host, port))
    print("Listening ....")
    sock.listen(5)
    conn, addr = sock.accept()
    print("Accepted ....", addr)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    watching = True
    
    try:
        while watching:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    watching = False
                    break

            # Retreive the size of the pixels length, the pixels length and pixels
            size_len = int.from_bytes(conn.recv(1), byteorder='big')
            size = int.from_bytes(conn.recv(size_len), byteorder='big')
            pixels = decompress(recvall(conn, size))

            # Create the Surface from raw pixels
            img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')

            # Display the picture
            pygame.display.set_caption("Remarca")
            screen.blit(img, (0,0))
            pygame.display.flip()
            clock.tick()
    finally:
        print("PIXELS: ", pixels)
        sock.close()

if __name__ == "__main__":
    main()
