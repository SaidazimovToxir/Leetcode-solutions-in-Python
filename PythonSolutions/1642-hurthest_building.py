# def furthestBuilding(heights, bricks, ladders):
#         heap = []

#         for i in range(len(heights) - 1):
#             diff = heights[i + 1] - heights[i]

#             if diff > 0:
#                 bricks -= diff
#                 # max heap
#                 heap.append(-diff)
#                 heap.sort(reverse=True)  # Sorting in descending order

#                 if bricks < 0:
#                     bricks += -heap[0]
#                     heap.pop(0)  # Removing the largest element
#                     ladders -= 1

#                 if ladders < 0:
#                     return i

#         return len(heights) - 1
    


# heights = [1,5,1,2,3,4,10000]; bricks = 4; ladders = 1
# # heights = [4,2,7,6,9,14,12]; bricks = 5; ladders = 1
# # heights = [4,12,2,7,3,18,20,3,19]; bricks = 10; ladders = 2
# # heights = [14,3,19,3]; bricks = 17; ladders = 0
# print(furthestBuilding(heights, bricks, ladders))


lst = [14,30,103]
lst = sorted(lst, key=lambda x: sum(map(int, str(x))))
print(lst)