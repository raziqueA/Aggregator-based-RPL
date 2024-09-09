from server1 import Server
from client import Client
from message import Message
from Aggregator import Aggregator

num_server = int(input("Enter number of servers: "))
num_client = int(input("Enter number of clients: "))
num_aggregator = int(input("Enter number of Aggregators: "))
# num_server = 1
# num_client = 4
# num_aggregator = 2
nodes = []
nodes.append(0)
node_object = []
node_object.append(None)
i = 1
agg_index = []
print("Enter the indices of Aggregators: ")
for j in range(num_aggregator):
    index = int(input())
    agg_index.append(index)
# nodes = [i for ab in range(num_server)]
for n in range(num_server):
    node_object.append(Server(i))
    nodes.append(i)
    i=i+1

# for n in range(num_aggregator):
    # node_object.append(Aggregator(i))
    # nodes.append(i)
    # i=i+1

for n in range(num_client + num_aggregator):
    if i in agg_index:
        node_object.append(Aggregator(i))
        nodes.append(i)
    else:
        node_object.append(Client(i))
        nodes.append(i)
    i=i+1
# 1->2->3

list =[[0 for i in range(len(nodes)+2)] for j in range(len(nodes)+2)]
print(nodes)
def addEdges():
    nums_egdes = int(input("No. of edges: "))
    # nums_egdes = 4
    while(nums_egdes):
        nums_egdes=nums_egdes-1
        src = int(input("Enter Source. "))
        dest = int(input("Enter Dest. "))
        list[src][dest] = list[dest][src] = 1
        if dest != 1:
            node_object[dest].parent = src
            node_object[src].children.append(dest)

addEdges()

input_file = "logLatesta0.txt"

def new_func(node_object, i):
    return node_object[i].getTrxCount()

def len_of_time(line):
    i = 0
    while (line[i] >='0' and line[i]<='9'):
        i=i+1
    return i

def get_time(line, i):
    return int(line[0:i])

temp = 0
with open(input_file, "r") as infile:
    for line in infile:
        # print(f"{temp+1}: {line}")
        time_len = len_of_time(line)
        time_ms = get_time(line, time_len)
        ID = f"{line[time_len+1]}{line[time_len+2]}{line[time_len+3]}{line[time_len+4]}"
        if line[time_len+25] == 'S':
            # print("S")
            i = int(line[time_len+4])
            _to = f"{line[-17:-2]}"
            txn_count = new_func(node_object, i)
            print(f"{ID} Sending request {txn_count} to {_to}")
            node_object[i].send_msg(node_object, time_ms)
            
        if line[time_len+25] == 'R':
            # print("R")
            i = int(line[time_len+4])
            # print(f"{ID} --R--")
            node_object[1].server_received_log(time_ms, int(line[-2]))
            # node_object[1].recived(node_object)

        if line[time_len+25] == 'e':
            # print("e")
            i = int(line[time_len+4])
            node_from = int(line[time_len+61])
            # print(node_from)
            # print(f"{ID} --e--")
            node_object[i].forward(node_object, node_from)
        # if temp == 11:
        #     break
        # temp = temp + 1

print(f"Total messages recived: {node_object[1].total_msg}")
print(f"Total time taken: {node_object[1].total_time} ms")
avg_time = node_object[1].total_time/node_object[1].total_msg
print(f"Avg time: {avg_time} ms")

node_object[1].get_node_wize_time()
node_object[1].get_node_wize_total_msg()

node_object[1].total_sending_energy()
node_object[1].total_reciving_energy()

node_object[1].total_msg_rec()

node_object[1].get_total_time()