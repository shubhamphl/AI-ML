
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
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)]=manhat_distance

            s = self.swap_nodes(list_pzl.copy(), 0, 3)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance


        if first_pzl[1] == 0:

            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 1, 0)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance


            s = self.swap_nodes(list_pzl.copy(), 1, 2)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance


            s = self.swap_nodes(list_pzl.copy(), 1, 4)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance



        if first_pzl[2] == 0:

            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 2, 1)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance


            s = self.swap_nodes(list_pzl.copy(), 2, 5)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance

        if first_pzl[3] == 0:

            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 3, 0)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance


            s = self.swap_nodes(list_pzl.copy(), 3, 4)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance



            s = self.swap_nodes(list_pzl.copy(), 3, 6)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance



        if first_pzl[4] == 0:

            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 4, 1)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance



            s = self.swap_nodes(list_pzl.copy(), 4, 3)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance


            s = self.swap_nodes(list_pzl.copy(), 4, 5)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance


            s = self.swap_nodes(list_pzl.copy(), 4, 7)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance

        if first_pzl[5] == 0:

            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 5, 2)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance



            s = self.swap_nodes(list_pzl.copy(), 5, 4)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance


            s = self.swap_nodes(list_pzl.copy(), 5, 8)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance



        if first_pzl[6] == 0:


            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 6, 3)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance


            s = self.swap_nodes(list_pzl.copy(), 6, 7)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance


        if first_pzl[7] == 0:
            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 7, 4)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance



            s = self.swap_nodes(list_pzl.copy(), 7, 6)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance



            s = self.swap_nodes(list_pzl.copy(), 7, 8)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance


        if first_pzl[8] == 0:


            graph[first_pzl] = []
            s = self.swap_nodes(list_pzl.copy(), 8, 5)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance



            s = self.swap_nodes(list_pzl.copy(), 8, 7)
            if not visited_pzl.__contains__((tuple(s))):
                manhat_distance = self.find_manhatten(s)
                distance[tuple(s)] = manhat_distance


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

    def find_manhatten(self,s):
        manhat_distance=0
        d2 = [[0] * 3, [0] * 3, [0] * 3]
        k = 0
        for i in range(3):
            for j in range(3):
                d2[i][j] = s[k]
                k = k + 1


        for i in range(3):
            for j in range(3):
                element=d2[i][j]
                for k in range(3):
                    for l in range(3):
                        if element==final2d[k][l]:
                            manhat_distance=manhat_distance+abs(k-i)+abs(l-j)

        return manhat_distance


pzl=puzzle()
print("Starting 8 - puzzle game...")
a=print("Enter the initial sequence of 9 nodes with empty node as 0: ")
init_pzl=[8,3,5,4,1,6,2,7,0]#/ 1,2,3,8,0,4,7,6,5/ 8,3,5,4,1,6,2,7,0/1,4,2,6,5,8,7,3,0
parents={}
final_pzl=[1,2,3,8,0,4,7,6,5]#/ 2,8,1,0,4,3,7,6,5/1,2,3,8,0,4,7,6,5/1,2,0,3,4,5,6,7,8
final2d=[[1,2,3],[8,0,4],[7,6,5]]
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

#............................................for user input


sys.setrecursionlimit(5000)
print("Game is running...")
print("...")
pzl.find_states(tuple(init_pzl))



