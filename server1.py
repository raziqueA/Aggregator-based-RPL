class Server:
    def __init__(self, id):
        self.id = id
        self.children = []
        self.message_storage = {} 
        self.total_time = 0
        self.total_msg = 0
        self.total_hidden_msg_count = 0
        self.total_hidden_time = 0
        self.message_storage = {}
        self.node_wize_total_msg = {}
        self.node_wize_total_time = {}
        self.total_rec_for_energy = 0
        self.total_send_for_energy = 0

    
    def forward(self, object_nodes, msg):
        print(f"{self.id} : received message from {msg.sender_ip} and the Message reads as: {msg.message}")
        if msg.aggregated == 1:
            print(f"and the message is aggregated one.")
    def recive(self, node_objects, msg):
        print(f"{self.id} : received message from {msg.sender_ip} at server and the Message reads as: {msg.message}.")
        msg.nums_rec = msg.nums_rec + 1
        self.message_storage[msg.sender_ip] = msg
    
    def server_received_log(self, rec_time, src_id):
        # if src_id in self.message_storage and self.message_storage[src_id] != None:
        if src_id in self.message_storage and self.message_storage[src_id] != None: 
            self.total_msg += 1
            if self.message_storage[src_id].aggregated:
                self.total_hidden_msg_count = self.total_hidden_msg_count + self.message_storage[src_id].combined_msgs_count
                for msg in self.message_storage[src_id].combined_msgs:
                    send_time = msg.init_time
                    time_taken = rec_time - send_time
                    self.total_hidden_time += time_taken
                    self.node_wize_total_time[msg.sender_ip] = self.node_wize_total_time.get(msg.sender_ip, 0) + time_taken
                    self.node_wize_total_msg[msg.sender_ip] = self.node_wize_total_msg.get(msg.sender_ip, 0) + 1
                    # self.total_rec_for_energy = self.total_rec_for_energy + msg.nums_rec
                    # self.total_send_for_energy = self.total_send_for_energy + msg.nums_send

                
            else:
                self.total_hidden_msg_count += 1
                send_time = self.message_storage[src_id].init_time
                time_taken = rec_time - send_time 
                self.total_time += time_taken
                self.total_hidden_time += time_taken
             # Check if the key exists before accessing it
                self.node_wize_total_time[src_id] = self.node_wize_total_time.get(src_id, 0) + time_taken
                self.node_wize_total_msg[src_id] = self.node_wize_total_msg.get(src_id, 0) + 1

            self.total_rec_for_energy = self.total_rec_for_energy + self.message_storage[src_id].nums_rec
            self.total_send_for_energy = self.total_send_for_energy + self.message_storage[src_id].nums_send


            print(f"{time_taken}ms is the time taken by {self.message_storage[src_id].message} to reach server from {self.message_storage[src_id].sender_ip}")
            del self.message_storage[src_id]

    def get_node_wize_time(self):
        for key in self.node_wize_total_time:
            print(f"Avg time for {key}: {self.node_wize_total_time[key]/self.node_wize_total_msg[key]} ")
    def get_node_wize_total_msg(self):
        for key in self.node_wize_total_msg:
            print(f"Total msgs send by {key}: {self.node_wize_total_msg[key]} ")

    def total_sending_energy(self):
        print(f"Total energy to send: {self.total_rec_for_energy}")

    def total_reciving_energy(self):
        print(f"Total energy to receive: {self.total_rec_for_energy}")

    def total_msg_rec(self):
        print(f"{self.total_msg}: total messages")
        print(f"{self.total_hidden_msg_count}: total messages included hidden")

    def get_total_time(self):
        tt = 0
        for key in self.node_wize_total_time:
            tt += self.node_wize_total_time[key]
        print(f"Total Time: {tt}")