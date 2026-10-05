packets=int(input("enter number of packets:"))
boxes=int(input("enter number of boxes"))
box_capacity=int(input("enter box capacity:"))
packed_packets=box_capacity*boxes
left_over_packets=packets-packed_packets
print('packets packed:',packed_packets)
print('packets left:',left_over_packets)