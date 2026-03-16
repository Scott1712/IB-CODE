#05/03/26

class TicketNode: #Class for a node
    def __init__(self,number):
        self.ticket_number = number
        self.next_person = None #When created, there's no next person

class TicketCounter:
    def __init__(self):
        self.first_person = None #When the counter is created, there's no first person

    def take_ticket(self,number):
        new_node = TicketNode(number)
        if not self.first_person:
            self.first_person = new_node
            return

        last = self.first_person
        while last.next_person:
            last = last.next_person
        last.next_person = new_node

    def serve_next_customer(self):
        if not self.first_person:
            print("There are no customers in the line")
            return

        print("Now serving",self.first_person.ticket_number)
        self.first_person = self.first_person.next_person


pharmacy_line = TicketCounter()
pharmacy_line.take_ticket(101) #Node 1
pharmacy_line.take_ticket(102) #Node 2
pharmacy_line.take_ticket(103) #Node 3
pharmacy_line.serve_next_customer() #Removes 101, Head is now 102