from message import Message
import queue
THRES = 5
class Aggregator:
    def __init__(self, id):
        self.id = id
        self.server_id = 1
        self.parent = -1
        self.msg_count = 0
        self.children = []
        self.child_count = 0
        self.queue_length = 0
        self.queue = []
        self.message_storage = [None]*10

    # def send_msg(self, node_objects):
        # self.msg_count = self.msg_count+1
        # msg = Message(f"Hello_{self.msg_count}_({self.id})")
        # msg.sender_ip = self.id
        # msg.sender_mac = self.id
        # msg.dest_ip = self.server_id
        # msg.dest_mac = self.server_id
        # if self.parent != -1:
        #     print(f"{self.id} : Sending {msg.message} to {self.server_id} via {self.parent}")
        #     node_objects[self.parent].forward(node_objects, msg)
        # pass

    def send_msg(self, node_objects, init_time):
        msg = Message(f"hello_{self.msg_count}_({self.id})")
        msg.sender_ip = self.id
        msg.sender_mac = self.id
        msg.dest_ip = self.server_id
        msg.dest_mac = self.server_id
        self.msg_count = self.msg_count+1
        msg.init_time = init_time
        msg.nums_send = msg.nums_send + 1
        if self.parent != -1:
            print(f"{self.id} : Sending {msg.message} to {self.server_id} via {self.parent}.")
            print(f"{self.parent} is parent of {self.id}")
            node_objects[self.parent].recive(node_objects, msg)

    
    def recive(self, node_objects, msg):
        # self.msg_count = self.msg_count+1
        # self.msg = Message(f"Hello_{self.msg_count}")
        # msg.sender_mac = self.id
        # msg.dest_mac = self.parent

        if msg.aggregated == 1:
            msg.sender_mac = self.id
            msg.dest_mac = self.parent
            msg.nums_rec = msg.nums_rec + 1
            self.message_storage[msg.sender_ip] = msg
            return
         
        self.queue_length = self.queue_length + 1
        self.queue.append(msg)

        if self.queue_length == THRES:
            AggMsg = Message(f"Aggrigator @ {self.id}")
            AggMsg.aggregated = 1
            AggMsg.init_time = self.queue[0].init_time
            AggMsg.dest_mac = self.parent
            AggMsg.sender_mac = self.id
            AggMsg.dest_ip = msg.dest_ip
            # msg_temp = msg
            while(self.queue_length):
                msg = self.queue.pop(0)
                AggMsg.combined_msgs.append(msg)
                AggMsg.combined_msgs_count += 1
                # msg_temp = msg
                # AggMsg.nums_send = AggMsg.nums_send + msg.nums_send
                AggMsg.nums_rec = AggMsg.nums_rec + msg.nums_rec
                AggMsg.sender_ip = msg.sender_ip
                self.queue_length = self.queue_length - 1
            self.message_storage[AggMsg.sender_ip] = AggMsg
        
        # print(f"{self.id} : recived msg from {msg.sender_ip} to send to {msg.dest_ip}, rightnow i have it.")

        # print(f"{self.id} : recived msg from {msg.sender_ip} to send to {msg.dest_ip} via {self.parent}.")
        # self.message_storage[msg.sender_ip] = msg
        # if self.parent != -1:
        #     node_objects[self.parent].forward(node_objects, msg)
    

    def forward(self, node_objects, send_to):
        # self.msg_count = self.msg_count+1
        # self.msg = Message(f"Hello_{self.msg_count}")
        # msg.sender_mac = self.id
        # msg.dest_mac = self.parent
        if(self.message_storage[send_to] == None):
            # print(f"Unofficial {self.id}: i do not have file from {send_to} - shayed merge ho gaya ho")
            return
        # print(f"{self.id} : forwarding msg from {msg.sender_ip} to {msg.dest_ip} via {self.parent}.")
        else:
            # msg retrive kiya
            msg = self.message_storage[send_to]
            msg.nums_send = msg.nums_send + 1
            self.message_storage[send_to] = None
            if self.parent != -1:
                node_objects[self.parent].recive(node_objects, msg)


    def getTrxCount(self):
        return {self.msg_count}