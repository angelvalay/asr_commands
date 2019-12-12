import sys
import serial, time
from scripts.check_asr import get_command


def to_int(command):
    if command == 'avanza':
        return 8
    elif command == 'detente':
        return 5
    elif command == 'derecha':
        return 6
    elif command == 'izquierda':
        return 4
    elif command == 'gira':
        return 0
    else:
        return -1

def execute_com(command):
    print(command)
    arduino = serial.Serial("/dev/ttyUSB0", 115200)
    if command == 8:
        arduino.write(b'8')
        time.sleep(4)
        arduino.write(b'5')
    else:
        arduino.write(str(command).encode())
    arduino.close()


def main():
    execute_com(to_int(get_command(sys.argv[1])))

if __name__ == "__main__":
    main()