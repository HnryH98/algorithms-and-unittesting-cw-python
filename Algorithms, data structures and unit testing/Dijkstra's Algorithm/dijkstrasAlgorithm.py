'''Create undirected, weighted graphs and perform dijkstras on them.'''

class Node:
    '''This class is used to initiate and store the nodes and their weighted edges. 
     Attributes:
     nodeID is the id used to identify the node
     connectedToList shows the nodes that the instance has an edge with as keys and their weights as values
    '''
    def __init__(self, name):
        self.nodeID = name
        self.connectedToList = {}#stores nodes the instance is connected to as keys & their weights as values
    
    
    def joinNode(self, other, weight):
        ''''Creates a weighted edge with another node if they do not already have 
        and edge between them '''
        if self.nodeID == other.nodeID:#validation against joining to self
            print("you can't join the node to itself")
            return 0
        
        if other.nodeID not in self.connectedToList:#validation if edge already exists
            self.connectedToList[other.nodeID]=weight
            other.connectedToList[self.nodeID]=weight
            print("We made an edge between:", self.nodeID,"and:", other.nodeID,"with weight:", weight)
            return 1
        else: 
            print("Edge already exists")
            return 0

   
    def connectedToListGetter(self, neighbour=None):
        '''Returns the connectedToList'''
        return(self.connectedToList)
 
            
    def edgeWeightGetter(self, neighbour):
        '''Returns the edge weight'''
        return(self.connectedToList[neighbour])#return edge weight
    
class Graph:
    '''This class initiates and stores the nodes and their edges. Once a graph is created, Dijksta can be performed
    Attributes:
         graphNodes: stores all nodes that have been added to the graph. 
        nodeIDs keys used to access the nodes which are stores as values
    ''' 
    def __init__ (self):
        self.graphNodes = {}#stores all nodes that have been added to the graph. nodeIDs keys used to access
        

    def makeNode(self, nodeID):
        '''Makes a new node in the graph if a node with the same ID hasn't already been made.
            Also ensures that nodeID is a positive integer. 
            Then uses the Node Class to initate the new node.
        '''        
        if isinstance(nodeID, int) == False or nodeID<0:#nodeID positive integer validation
            print("The node must be a positive integer")
            return 0
        if nodeID in self.graphNodes:#nodeId in already made validation
            print("This graph already has a node with this ID")
            return 0
        newNode = Node(nodeID)
        self.graphNodes[nodeID] = newNode
        print("We made a new node: ", nodeID)
        return 1 
    
    def makeEdge(self,nodeID1, nodeID2, weight):
        '''This function checks that both the nodes exit and then uses the Node classes' joinNode function
        to create a weighted edge between two nodes in the graph .        
        '''
        if nodeID1 not in self.graphNodes or nodeID2 not in self.graphNodes:#node doesn't exist validation
            print("Atleast one of these nodes do not exist")
            return 0
        if isinstance(weight, int) == False:#validates that weight is an integer
            print("Weight must be an integer")
            return 0
            
        else:
            returnVal = self.graphNodes[nodeID1].joinNode(self.graphNodes[nodeID2], weight)
            return returnVal


    def dijsktra(self, startNodeID, endNodeID):
        '''uses Dijkstra's algorithm to find the shortest path between two nodes:#startNodeID and endNodeID        
        '''
        unMarkedNodes = set(self.graphNodes)                               
        if startNodeID not in unMarkedNodes or endNodeID not in unMarkedNodes:#check node exists validation
            print("Either the end or start node does not exist")
            return 0
        predecessor = {} #Key: previous node, Value: current node. (to store paths)
        weightFromSource = {}#stores tentative weight to each node from source node 
        weightFromSource[startNodeID]=0        
        visited = set()#nodes that have been visited
        visited={startNodeID}


        while len(unMarkedNodes)>0:#while unmarked nodes exist
            minWeightNode = None #unmarked node with the min weighted edge from source.
            
           
            for node in unMarkedNodes.intersection(visited):#for visited unmarked nodes
                if minWeightNode == None:
                    minWeightNode = node
                elif weightFromSource[node] < weightFromSource[minWeightNode]:
                    minWeightNode = node

            if minWeightNode == None: #no more nodes left to improve
                break 

            unMarkedNodes.remove(minWeightNode)
            tentativeWeight = weightFromSource[minWeightNode]
            
            
            for neighbour in self.graphNodes[minWeightNode].connectedToListGetter():
                neighbourWeight = tentativeWeight + self.graphNodes[minWeightNode].edgeWeightGetter(neighbour)#
                if neighbour not in visited or neighbourWeight < weightFromSource[neighbour]:
                    predecessor[neighbour] = minWeightNode
                    weightFromSource[neighbour] = neighbourWeight
                    visited.add(neighbour)
                   
           
        path=[]
        try:
            pathWeight = weightFromSource[endNodeID]
            path.append(endNodeID)
            findPredecessor = endNodeID
            #uses the predecessor dictionary to make the path from end to source
            while findPredecessor!=startNodeID:
                for i in predecessor:
                    if i == findPredecessor:
                        path.insert(0,predecessor[i])
                        findPredecessor = predecessor[i]
        except KeyError:#No path from start to end node (validation)
            print("No path from start to end")
            return 0
        print("Path",path)
        print("Weight: ",pathWeight)
        return path


    
'''

a = Graph()
a.makeNode(1)
a.makeNode(2)
a.makeNode(3)
a.makeNode(4)
a.makeNode(5)
a.makeNode(6)
a.makeNode(7)

 

a.makeEdge(1, 2, 3)
a.makeEdge(1, 3, 5)
a.makeEdge(1, 4, 6)
a.makeEdge(2, 4, 2)
a.makeEdge(3, 4, 2)
a.makeEdge(3, 5, 6)
a.makeEdge(3, 6, 3)
a.makeEdge(3, 7, 7)
a.makeEdge(4, 6, 9)
a.makeEdge(5, 6, 5)
a.makeEdge(5, 7, 2)
a.makeEdge(6, 7, 1)
a.dijsktra(1, 7)
'''
