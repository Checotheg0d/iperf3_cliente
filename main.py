
import iperf3

client = iperf3.Client()
client.duration = 10
client.server_hostname = '192.168.100.9'
client.port = 5201
client.protocol = 'udp'


print('Connecting to {0}:{1}'.format(client.server_hostname, client.port))
result = client.run()

if result.error:
    print(result.error)
else:
    print('')
    with open ("archivo.txt","a") as txtfile :
        print('///////////////////////////////////////////////////////////', file=txtfile)
        print('Test completed:', file=txtfile)
        print('  started at         {0}'.format(result.time), file=txtfile)
        print('  bytes transmitted  {0}'.format(result.bytes), file=txtfile)
        print('  jitter (ms)        {0}'.format(result.jitter_ms), file=txtfile)
        print('  avg cpu load       {0}%\n'.format(result.local_cpu_total), file=txtfile)

        print('Average transmitted data in all sorts of networky formats:', file=txtfile)
        print('  bits per second      (bps)   {0}'.format(result.bps), file=txtfile)
        print('  Kilobits per second  (kbps)  {0}'.format(result.kbps), file=txtfile)
        print('  Megabits per second  (Mbps)  {0}'.format(result.Mbps), file=txtfile)
        print('  KiloBytes per second (kB/s)  {0}'.format(result.kB_s), file=txtfile)
        print('  MegaBytes per second (MB/s)  {0}'.format(result.MB_s), file=txtfile)

#    try:
 #       file = open ("archivo.txt","w")
  #      file.write('  MegaBytes per second (MB/s)  {0}'.format(result.MB_s))
   # except FileExistsError:
    #    file=open("archivo.txt","w")
     #   file.write('  MegaBytes per second (MB/s)  {0}'.format(result.MB_s))
      #  file.close()