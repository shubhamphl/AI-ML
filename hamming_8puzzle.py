
import sys
class puzzle:
    count=0
    def check_goal(self,pzl1,pzl2):

        if pzl1==tuple(pzl2):
            print("goal achieved!")
            for j in visited_pzl:
                print(j)
            exit(0)


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
                ham_distance = self.find_hamming(s)
                distance[tuple(s)]=ham_distance

            s = self.swap_nodes(list_pzl.copy(), 0, 3)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance


        if first_pzl[1] == 0:

            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 1, 0)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance


            s = self.swap_nodes(list_pzl.copy(), 1, 2)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance


            s = self.swap_nodes(list_pzl.copy(), 1, 4)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance



        if first_pzl[2] == 0:

            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 2, 1)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance


            s = self.swap_nodes(list_pzl.copy(), 2, 5)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance

        if first_pzl[3] == 0:

            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 3, 0)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance


            s = self.swap_nodes(list_pzl.copy(), 3, 4)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance



            s = self.swap_nodes(list_pzl.copy(), 3, 6)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance



        if first_pzl[4] == 0:

            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 4, 1)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance



            s = self.swap_nodes(list_pzl.copy(), 4, 3)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance


            s = self.swap_nodes(list_pzl.copy(), 4, 5)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance


            s = self.swap_nodes(list_pzl.copy(), 4, 7)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance

        if first_pzl[5] == 0:

            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 5, 2)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance



            s = self.swap_nodes(list_pzl.copy(), 5, 4)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance


            s = self.swap_nodes(list_pzl.copy(), 5, 8)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance



        if first_pzl[6] == 0:


            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 6, 3)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance


            s = self.swap_nodes(list_pzl.copy(), 6, 7)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance


        if first_pzl[7] == 0:
            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 7, 4)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance



            s = self.swap_nodes(list_pzl.copy(), 7, 6)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance



            s = self.swap_nodes(list_pzl.copy(), 7, 8)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance


        if first_pzl[8] == 0:


            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 8, 5)
            if not visited_pzl.__contains__((tuple(s))):
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance



            s = self.swap_nodes(list_pzl.copy(), 8, 7)
            if not visited_pzl.__contains__((tuple(s))):             #hvvjyvj
                ham_distance = self.find_hamming(s)
                distance[tuple(s)] = ham_distance


        v=min(distance.values())
        for key,value in distance.items():
            if v==value:
                s=key
                break
        graph[first_pzl].append(s)
        visited_pzl.append(tuple(s))
        distance.clear()
        self.count+=1
        self.check_goal(s, final_pzl)
        self.find_states(s)

    def find_hamming(self,s):
        ham_distance=0
        for i in range(9):
            if not s[i]==final_pzl[i]:
                ham_distance+=1

        return ham_distance

pzl=puzzle()
print("Starting 8 - puzzle game...")
a=print("Enter the initial sequence of 9 nodes with empty node as 0: ")
init_pzl=[1,2,5,3,4,0,6,7,8]#8,3,5,4,1,6,2,7,0
parents={}
final_pzl=[1,4,2,3,7,5,6,0,8]#1,2,3,8,0,4,7,6,5
graph={}
path=[]
distance={}


# ..........................................for user input
# i=0


# while i!=9:
#     temp=int(input())
#     while init_pzl.__contains__(temp):
#         print("Redundant node found! please enter the node again: ")
#         temp = int(input())
#     init_pzl.append(temp)
#     i+=1
visited_pzl=[tuple(init_pzl)]
#
# i=0
#
# print("Enter the goal sequence of 9 nodes with empty node as 0")
# while i!=9:
#     temp=int(input())
#     while final_pzl.__contains__(temp):
#         print("Redundant node found! please enter the node again: ")
#         temp = int(input())
#     final_pzl.append(temp)
#     i+=1


#.................................................for user input
sys.setrecursionlimit(5000)
print("Game is running...")
print("...")
pzl.find_states(tuple(init_pzl))



