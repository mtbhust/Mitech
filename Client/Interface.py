# https://pygobject.readthedocs.io/en/latest/getting_started.html
import gi 
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import Client
import subprocess

class userinput(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Demo ")
        self.set_border_width(5)
        self.set_size_request(500,20)

        #Big box
        self.BOX = Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing = 3)
        self.add(self.BOX)
        ip_port_box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 3)

        #Ip_address enter

        self.server_ip = Gtk.Entry()
        self.server_ip.set_text("Enter Server Ip Address")
        self.server_ip.set_size_request(25,1)
        ip_port_box.pack_start(self.server_ip, True,True, 0)


        #Port enter
        self.socket_port = Gtk.Entry()
        self.socket_port.set_text("Enter Socket Port")
        self.socket_port.set_size_request(7,1)
        self.socket_port.set_visibility(True)
        ip_port_box.pack_start(self.socket_port, True, True,0)

        #Password box
        self.password = Gtk.Entry()
        self.password.set_size_request(10,1)
        self.password.set_text("password")
        self.password.set_visibility(False)

        ip_port_box.pack_start(self.password, True,True, 0)

        #Connect Button
        self.connect_button = Gtk.Button(label = "Connect")
        self.connect_button.connect("clicked", self.check_status)
        ip_port_box.pack_end(self.connect_button,True,True,0)

     

        self.BOX.add(ip_port_box)

        #Connection status

        self.connection_status = Gtk.Label()
        self.connection_status.set_label("Please connect")
        self.BOX.add(self.connection_status)

        self.command_box = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 3)
        self.command_box.set_size_request(500,1)
        #Command input
        self.input1 = Gtk.Entry()
        self.input1.set_text("Command")
        self.input1.set_size_request(25,1)
        self.command_box.pack_start(self.input1,True,True,0)
        self.BOX.pack_start(self.command_box,True, True, 0)
        
        #Sending button
        self.input_signal = Gtk.Button(label = "Send Request")
        self.input_signal.connect("clicked", self.server_response)
        self.command_box.pack_end(self.input_signal,True,True,0)

        #Server output(label)
        self.server_output = Gtk.Label()
        self.server_output.set_label("")
        self.BOX.pack_start(self.server_output,True, True, 0)
    
    #Connect Button Activation, check status
    def check_status(self,widget ):
        self.connection_status.set_label(Client.client.check_connection(self.server_ip.get_text(), self.socket_port.get_text(),self.password.get_text()))

    #Data sending button
    def server_response(self,widget):
        self.server_output.set_label(Client.client.response(self.input1.get_text(),self.server_ip.get_text(), self.socket_port.get_text(), self.password.get_text()))
        
    # def dev_input(self): #command line
    
    # def sever_output(self):
    
window = userinput()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()