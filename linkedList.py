class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def insfront(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def insback(self, newdata=None):
        curr = self.headval
        while curr.nextval is not None:
            curr = curr.nextval
        curr.nextval = Node(newdata)

    def insmiddle(self, middleval, newdata):
        curr = self.headval
        while curr.dataval != middleval:
            if curr.nextval == None:
                return "middle val not found"
            curr = curr.nextval

    def delend(self):
        curr = self.headval
        while curr.nextval.nextval is not None:
            curr = curr.nextval
        curr.nextval = None

    def delhead(self):
        self.headval = self.headval.nextval

    def deldata(self, data):
        curr = self.headval
        if curr.dataval == data:
            self.delhead()
        else:
            while curr.nextval != None and curr.nextval.dataval != data:
                curr = curr.nextval
            if curr.nextval == None:
                return "value not found"
            curr.nextval = curr.nextval.nextval


list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
list1.headval.nextval = e2
e2.nextval = e3
list1.insback("Thurs")
list1.insfront("Sun")
list1.delend()
list1.delhead()
list1.deldata("Tue")
list1.deldata(None)
list1.deldata("Mon")
list1.listprint()
