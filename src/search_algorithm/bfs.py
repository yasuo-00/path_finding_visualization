import painter
from collections import deque


#returns last node (destination_node)
def bfs(origin_node, dest_node, board, screen):
    #put origin node on open_nodes_list (first to be expanded)
    open_nodes=deque()
    closed_nodes=list()
    open_nodes.append(origin_node)
    curr_node=None
    
    #may have some bugs (check later)
    #implement search painter for dfs
    while len(open_nodes)>0:
        curr_node=open_nodes.popleft()
        painter.paint_search(screen,curr_node.pos, board)
        print(curr_node.pos)
        if curr_node is dest_node:
            print('found')
            return curr_node
        #print(curr_node.pos)
        for node in curr_node.neighbour_list:
            if node not in closed_nodes:
                if node not in open_nodes:
                    #print('entered')
                    node.parent_node=curr_node
                    #print(node.parent.pos)
                    open_nodes.append(node)
        closed_nodes.append(curr_node)

    #if no possible path was found
    return None