
#author @shubhamphl

class graphs:
    graph={}

    def switch(self):
        ch=9
        while ch!=0:
            print("Enter your choice from the following: " )
            print("1: To insert a new node")
            print("2: To insert a new edge")
            print("3: To delete a node")
            print("4: To delete an edge")
            print("5: To print the graph")
            print("6: To traverse Breadth First Search")
            print("7: To traverse Depth First Search")
            print("0: To exit from the main menu")
            ch=int(input(ch))
            if ch==1:
                self.addnode()

            elif ch==2:
                self.addedge()

            elif ch==3:
                self.deletenode()

            elif ch==4:
                self.delete_edge()

            elif ch==5:
                self.printgraph()

            elif ch==6:
                self.bfs()

            elif ch==7:
                self.dfs()

            elif ch==0:
                exit(0)

            else:
                pass


    def addnode(self):
        print("Enter the node you want to insert: ")
        node=int(input())
        if node not in self.graph:
            self.graph[node]=[]
            print("Node added successfully!")

        else:
            print("node already exists!")
        self.switch()


    def printgraph(self):
        print("The graph is: ")
        print(self.graph)
        self.switch()


    def addedge(self):
        print("enter the starting vertex: ")
        s=int(input())
        print("enter the ending vertex: ")
        e=int(input())
        if s in self.graph:
            if e in self.graph:
                self.graph[s].append(e)
                print("edge successfully added!")
            else:
                print("invalid vertex entered!")
        else:
            print("invalid vertex entered!")

        self.switch()

    def deletenode(self):
        print("Enter the node for deletion: ")
        n=int(input())
        if n in self.graph:
            for node in self.graph:
                for neighbour in self.graph[node]:
                    self.graph[node].remove(neighbour)

            self.graph.__delitem__(n)
            self.switch()
            print("node successfully deleted!")
        else:
            print("invalid node entered!")
        self.switch()
        

    def delete_edge(self):
        print("enter the starting node: ")
        s=int(input())
        print("enter the ending node")
        e=int(input())
        if e in self.graph[s]:
            self.graph[s].remove(e)
            print("edge deleted successfully!")
        else:
            print("no such edge found!")
        self.switch()

    def bfs(self):
        if len(self.graph) !=0:
            print("Enter the source vertex for BFS: ")
            s=int(input())
            if s in self.graph:
                print("Breadth First Search order of the graph is: ")

                queue=[]
                v={}
                for j in self.graph:
                    v[j]=False
                flag=-1
                queue.append(s)
                flag=flag+1
                v[s]=True
                print(s, end="   ")
                while flag!=-1:
                    for neighbour in self.graph[s]:
                            if v[neighbour]==False:
                                print(neighbour,end="   ")
                                queue.append(neighbour)
                                flag+=1
                                v[neighbour]=True


                    queue.pop(0)
                    flag = flag - 1
                    if flag>=0:
                        s = queue[0]
                    else:
                        for j in self.graph:
                            v[j] = False
                        print()
                        pass

            else:
                print("invalid node to traverse!")
        else:
            print("no node to traverse!")
        self.switch()



    def dfs(self):
        if len(self.graph) !=0:
            print("Enter the source vertex for DFS: ")
            s=int(input())
            if s in self.graph:
                print("Depth First Search order of the graph is: ")
                found=0
                stack=[]
                vs={}
                for j in self.graph:
                    vs[j]=False
                flag=-1
                stack.append(s)
                flag=flag+1
                vs[s]=True
                print(s, end="   ")
                while len(stack)!=0:
                    found=0
                    for neighbour in self.graph[s]:
                        if vs[neighbour] == False:
                            print(neighbour, end="   ")
                            stack.append(neighbour)
                            vs[neighbour] = True
                            found=1
                            s=neighbour
                            break

                    if found==1:
                        s=neighbour

                    if found==0:
                        stack.pop()
                        if len(stack)>0:
                            s = stack[len(stack) - 1]
                        else:
                            for j in self.graph:
                                vs[j] = False
                            print()
                            pass



            else:
                print("invalid node to traverse!")
        else:
            print("no node to traverse!")
        self.switch()


g=graphs()
g.switch()


