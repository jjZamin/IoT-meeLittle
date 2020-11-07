import paho.mqtt.client as mqtt
import time

## By Ghennadie Mazin

class PAHOclient():
    def __init__(self, parent, broker="", client="", user="", password=""):
        self.parent = parent

        self.BROKER_ID = broker
        self.CLIENT_ID = client
        self.USER = user
        self.PASSWORD = password
        self.clean_session_on = False
        self.client = mqtt.Client()
        self.DISCONNECTED = False
        self.TOPIC = ""
        self.MSG = ""

        self.RECV_message = ""
        self.RECV_topic = ""

    ### ADDING MSG CALLBACKS:
    def add_msg_callback(self, sub, callback):
        self.client.message_callback_add(sub, callback)
    def remove_msg_callback(self, sub):
        self.client.message_callback_remove(sub)
    ###



    ###############################################################
    #_ONfuncs
    def on_log(self, client, userdata, level, buf):
        print("log: " + buf)

    def return_is_connected(self):
        if(self.DISCONNECTED == False):
            return True
        else:
            return False

    def on_connect(self, client, userdata, flags, rc):
            if rc == 0:
                print("connected: [ OK ]")
                self.DISCONNECTED = False
                self.return_is_connected()
            else:
                print("connection failed, code: ", rc)
                self.DISCONNECTED = True
                self.return_is_connected()

    def on_disconnect(self, client, userdata, rc):
        self.DISCONNECTED = True
        if rc != 0:
            print("disconnected: [ OK ]")
            self.return_is_connected()
        else:
            print("still connected, code: ", rc)  
    
    def return_topic_message(self):
        self.parent.ON_RECEIVE(self.RECV_topic, self.RECV_message)
        
    def on_message(self, client, userdata, msg): 
        self.RECV_message = str(msg.payload.decode("utf-8", "ignore"))
        self.RECV_topic = msg.topic
        self.return_topic_message()

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribed to: " + str(self.TOPIC) + "[ OK ]")

    def on_publish(self, client, userdata, mid):
        pass

    def on_unsubscribe(self, client, userdata, mid):
        pass
    ###############################################################
    


    #_SETs
    def set_password(self, password):
        self.PASSWORD = password
    def set_user(self, user):
        self.USER = user
    def set_brokerID(self, broker_id):
        self.BROKER_ID = broker_id
    def set_clientID(self, client_ID):
        self.CLIENT_ID = client_ID
    def clean_session(self, clean_session_on):
        self.clean_session_on = clean_session_on
    def set_reconnect_time(self, min_delay=1, max_delay=8):
        self.client.reconnect_delay_set(min_delay, max_delay)
    def set_will(self, topic, msg):
        self.client.will_set(topic, msg)
    def set_topic(self, topic):
        try:
            self.TOPIC = topic
        except:
            pass
    def set_message(self, msg):
        self.MSG(msg)


    #_INITS
    def INIT_USR_PASS(self):
        self.client.username_pw_set(username=self.USER, password=self.PASSWORD)
    def INIT_CLIENT(self):
        try:
            self.client = mqtt.Client(self.CLIENT_ID, self.clean_session_on)
            time.sleep(1)
        except:
            pass

    def REINIT_CLIENT(self):
        self.client.reinitialise(self.CLIENT_ID, self.clean_session_on)
        time.sleep(3)
    def INIT_LOOP(self):
        self.client.loop_start()
        time.sleep(3)
    def END_LOOP(self):
        self.client.loop_stop()
        time.sleep(3)
            
    #_set_all_ONS
    def set_on_funcs(self):
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_log = self.on_log
        self.client.on_message = self.on_message
        self.client.on_subscribe = self.on_subscribe
        self.client.on_publish = self.on_publish
        self.client.on_unsubscribe = self.on_unsubscribe

    #_CONNECTS
    def connect_to_broker(self):
        self.client.connect(self.BROKER_ID)
        time.sleep(1)
    def disconnect_from_broker(self):
        self.client.disconnect()
        time.sleep(1)
    def reconnect_to_last_broker(self):
        self.client.reconnect()
        time.sleep(1)

    #_PUBLISH
    def publish_instant(self, topic, msg):
        self.client.publish(topic, msg)

    def publish_set(self):
        self.client.publish(self.TOPIC, self.MSG)

    #_SUBSCRIBE
    def subscribe_to_topic_instant(self, topic):
        self.client.subscribe(topic)
        time.sleep(1)
    def subscribe_to_topic(self):
        self.client.subscribe(self.TOPIC)
        time.sleep(1)
    def unsubscribe_topic_instant(self, topic):
        self.client.unsubscribe(topic)
        time.sleep(1)
    def unsubscribe_topic(self):
        self.client.unsubscribe(self.TOPIC)
        time.sleep(1)