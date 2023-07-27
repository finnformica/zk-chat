import pyshark

capture = pyshark.LiveCapture(output_file="packets/pyshark.pcap", interface="lo0")
capture.sniff(timeout=50)

print(capture)
