
import sys
class puzzle:
    def check_goal(self,pzl1,pzl2):
        if pzl1==pzl2:
            print("goal achieved!")
            p=tuple(pzl2)
            self.parent(p)


    def swap_nodes(self,temp_pzl,a,b):
        temp=temp_pzl[a]
        temp_pzl[a]=temp_pzl[b]
        temp_pzl[b]=temp
        return temp_pzl



    def find_states(self,first_pzl):
        list_pzl = list(first_pzl)
        if first_pzl[0]==0:


            graph[first_pzl]=[]
            s=self.swap_nodes(list_pzl.copy(),0,1)

            if not visited_pzl.__contains__((tuple(s))):

                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s,final_pzl)

            s = self.swap_nodes(list_pzl.copy(), 0, 3)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)

                parents[tuple(s)]=first_pzl
                visited_pzl.append(tuple(s))
            self.check_goal(s, final_pzl)


        if first_pzl[1] == 0:

            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 1, 0)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                parents[tuple(s)]=first_pzl
                visited_pzl.append(tuple(s))
            self.check_goal(s, final_pzl)

            s = self.swap_nodes(list_pzl.copy(), 1, 2)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                parents[tuple(s)]=first_pzl
                visited_pzl.append(tuple(s))
            self.check_goal(s, final_pzl)


            s = self.swap_nodes(list_pzl.copy(), 1, 4)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)




        if first_pzl[2] == 0:

            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 2, 1)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)


            s = self.swap_nodes(list_pzl.copy(), 2, 5)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)


        if first_pzl[3] == 0:

            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 3, 0)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)


            s = self.swap_nodes(list_pzl.copy(), 3, 4)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)


            s = self.swap_nodes(list_pzl.copy(), 3, 6)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)



        if first_pzl[4] == 0:

            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 4, 1)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)] = first_pzl
            self.check_goal(s, final_pzl)


            s = self.swap_nodes(list_pzl.copy(), 4, 3)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)


            s = self.swap_nodes(list_pzl.copy(), 4, 5)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)


            s = self.swap_nodes(list_pzl.copy(), 4, 7)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)

        if first_pzl[5] == 0:

            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 5, 2)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)


            s = self.swap_nodes(list_pzl.copy(), 5, 4)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)


            s = self.swap_nodes(list_pzl.copy(), 5, 8)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)



        if first_pzl[6] == 0:


            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 6, 3)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)


            s = self.swap_nodes(list_pzl.copy(), 6, 7)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)



        if first_pzl[7] == 0:
            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 7, 4)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)


            s = self.swap_nodes(list_pzl.copy(), 7, 6)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)


            s = self.swap_nodes(list_pzl.copy(), 7, 8)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)


        if first_pzl[8] == 0:


            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 8, 5)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)


            s = self.swap_nodes(list_pzl.copy(), 8, 7)
            if not visited_pzl.__contains__((tuple(s))):
                graph[first_pzl].append(s)
                visited_pzl.append(tuple(s))
                parents[tuple(s)]=first_pzl
            self.check_goal(s, final_pzl)

        i = visited_pzl.index(first_pzl)
        k = visited_pzl[i + 1]

        self.find_states(k)

    def parent(self,prt):
        while prt!=tuple(init_pzl):
            path.append(prt)
            self.parent(parents[prt])
        path.append(prt)

        for n in range(len(path)-1,0,-1):
            print(path[n])
        print(path[0])
        exit(0)


pzl=puzzle()
print("Starting 8 - puzzle game...")
a=print("Enter the initial sequence of 9 nodes with empty node as 0: ")
init_pzl=[]
parents={}
final_pzl=[]
graph={}
path=[]

i=0


while i!=9:
    temp=int(input())
    while init_pzl.__contains__(temp):
        print("Redundant node found! please enter the node again: ")
        temp = int(input())
    init_pzl.append(temp)
    i+=1
visited_pzl=[tuple(init_pzl)]

i=0

print("Enter the goal sequence of 9 nodes with empty node as 0")
while i!=9:
    temp=int(input())
    while final_pzl.__contains__(temp):
        print("Redundant node found! please enter the node again: ")
        temp = int(input())
    final_pzl.append(temp)
    i+=1

sys.setrecursionlimit(5000)
print("Game is running...")
print("...")
pzl.find_states(tuple(init_pzl))



