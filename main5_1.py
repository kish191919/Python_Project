# pip install psutil        => Check information on your computer

import psutil

# Output the speed of the CPU
cpu = psutil.cpu_freq()
cpu_current_ghz = round(cpu.current / 1000, 2)
print(f"CPU speed : {cpu_current_ghz} GHZ")

# Output the number of physical cores in the CPU
cpu_core = psutil.cpu_count(logical=False)
print(f"CPU Core : {cpu_core} EA")

# Output the memory information.
memory = psutil.virtual_memory()
memory_total = round(memory.total / 1024**3)
print(f"Memory : {memory_total} GB")

# Output the disk information.
disk = psutil.disk_partitions()
for p in disk:
    print(p.mountpoint, p.fstype, end=' ')
    du = psutil.disk_usage(p.mountpoint)
    disk_total = round(du.total / 1024**3)
    print(f"Disk Size : {disk_total} GB")

# Output the amount of data sent and received over the network.
net = psutil.net_io_counters()
sent = round(net.bytes_sent/1024**2,1)
recv = round(net.bytes_recv/1024**2, 1)
print(f"Sent : {sent} MB  //  Receive : {recv} MB")