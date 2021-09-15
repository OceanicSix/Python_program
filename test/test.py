import sys
sys.stdout.buffer.write(bytes.fromhex("AABBCC12")+ b"%.8x"*24 )