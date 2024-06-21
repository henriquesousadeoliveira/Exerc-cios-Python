conectores1 = [int(x) for x in input().split()]
conectores2 = [int(x) for x in input().split()]
eh_compativel = True
for i in range(0, len(conectores1)):
    if conectores1[i] == conectores2[i]:
        eh_compativel = False
        break
if eh_compativel:
    print("Y")
else:
    print("N")