class Message:
    def __init__(self, message):
        self.message = message
        self.sender_ip = -1
        self.dest_ip = -1
        self.sender_mac = -1
        self.dest_mac = -1
        self.hops = []
        self.init_time = -1
        self.reach_time = -1
        self.nums_send = 0
        self.nums_rec = 0
        self.aggregated = 0
        self.combined_msgs_count = 0
        self.combined_msgs = []