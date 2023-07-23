import pyshark

capture = pyshark.LiveCapture(output_file="packets/pyshark.pcap", interface="en0")
capture.sniff(timeout=20)

print(capture)
