import time


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state   # string
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
    
    def __len__(self):
        if self.parent == None:
            return 0
        else:
            return (1+len(self.parent))
    
    def visualize(self):
        row1 = [self.state[i] for i in range(3)]
        row2 = [self.state[i] for i in range(3,6)]
        row3 = [self.state[i] for i in range(6,9)]
        print(*row1)
        print(*row2)
        print(*row3)


def iterative_deepening(node):
    limit = 0
    while True:
        limit += 1
        result = depth_limited_search(node, limit)
        if result != 'cutoff':
            return result
        
def depth_limited_search(node, limit):
    frontier = []         # list of Node instances
    frontier.append(node)  
    result = 'failure'

    while frontier:
        node = frontier.pop()
        if node.state == goal:
            return node
        elif len(node) >= limit:
            result = 'cutoff'
        elif not is_cycle(node):
            for child in get_children(node):
                frontier.append(child)

    return result

def num_wrong_tiles(node):
    '''Count the num of tiles in wrong location'''
    s = node.state
    h1 = 0
    for i in range(9):
        if s[i] == '0':
            continue
        elif s[i] != goal[i]:
            h1 += 1
    return h1

def manhattan_distance(node):
    '''Calculate the toal manhattan distance for all tiles until goal apears'''
    # each index of tiles refers to a unique coord of row and col
    index2coord = {0:[0,0], 1:[0,1], 2:[0,2],
                    3:[1,0], 4:[1,1], 5:[1,2],
                    6:[2,0], 7:[2,1], 8:[2,2]}
    h2 = 0
    s = node.state
    for i in range(9):
        if s[i] == '0':
            continue
        elif s[i] != goal[i]:
            tile = s[i]     
            goal_x = index2coord[goal.index(tile)][1]
            goal_y = index2coord[goal.index(tile)][0]
            h2 += abs(goal_x - index2coord[i][1]) + abs(goal_y - index2coord[i][0])
    return h2

def astar(node, h):
    frontier = []
    f = node.path_cost + h(node)
    frontier.append((f,node))
    reached = {}
    reached[node.state] = node

    while frontier:
        # pop and return the frontier with min f val
        # print('#### check frontier', frontier)
        frontier.sort(reverse=True, key=lambda x: x[0])
        # print("### check sorted frontier", frontier)
        node = frontier.pop()[1]
        # print('##### check node:', node)
        if node.state == goal:
            return node
        for child in get_children(node):
            s1 = child.state
            if s1 not in reached or child.path_cost < reached[s1].path_cost:
                reached[s1] = child
                f = child.path_cost + h(child)
                frontier.append((f ,child))
    return 'failure'


# def is_cycle(node):
#     if node.parent != None and node.state == root.state:
#         return True
#     return False

def is_cycle(node, k=10):
    def find_cycle(ancestor, k):
        return (ancestor is not None and k > 0 and
                (ancestor.state == node.state or find_cycle(ancestor.parent, k - 1)))
    return find_cycle(node.parent, k)

def Actions(state):
    index = state.index("0")
    actions = []

    left_ok = [1,2,4,5,7,8]
    right_ok = [0,1,3,4,6,7]
    up_ok = [3,4,5,6,7,8]
    down_ok = [0,1,2,3,4,5]

    # actions are reversed between blank and numbered tiles
    if index in left_ok:
        actions.append('Right')
    if index in right_ok:
        actions.append('Left')
    if index in up_ok:
        actions.append('Down')
    if index in down_ok:
        actions.append('Up')
    
    return actions     # a list with at least 2 possible actions

def swap(string, i, j):
    '''Swap two characters with given indexes'''
    lst = list(string)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

def action_cost(s, action, s1):
    return 1

def child_node(node, action):
    '''Return a child node of the given node by the given action.'''
    s = node.state    
    index = s.index('0')

    # actions are reversed between blank and numbered tiles  
    if action == 'Right':
        s1 = swap(s, index, index-1)
    if action == 'Left':
        s1 = swap(s, index, index+1)
    if action == 'Down':
        s1 = swap(s, index, index-3)
    if action == 'Up':
        s1 = swap(s, index, index+3)
    
    cost = node.path_cost + action_cost(s, action, s1)
    child = Node(s1, node, action, cost)
    return child   # a new Node instance

def get_children(node):
    children = []
    s = node.state
    for action in Actions(s):
        child = child_node(node, action)
        children.append(child)
    return children

def path_actions(node):
    '''The sequence of actions from root to the given node'''
    if node == 'cutoff' or node == 'failure':
        return []
    if node.parent == None:
        return []
    # print()
    # node.visualize()
    return path_actions(node.parent) + [node.action]




init_state = input('Please input an intial state: ')
root = Node(init_state)
# root.visualize()
goal = "123804765"

# IDDFS
print('\n------------------------------------------------\n')
print('1) Iterative Deepening Depth-First Search')
start = time.monotonic()
print('   > Solutions: ', path_actions(iterative_deepening(root)))
end = time.monotonic()
print('   > Time Cost: ', str(end - start), 'seconds')


# A* with num_wrong_tiles
print('\n------------------------------------------------\n')
print('2) A* Search using num_wrong_tiles')
start = start = time.monotonic()
print('   > Solutions: ', path_actions(astar(root, num_wrong_tiles)))
end = time.monotonic()
print('   > Time Cost: ', str(end - start), 'seconds')

# A* with manhattan_distance
print('\n------------------------------------------------\n')
print('3) A* Search using manhattan_distance')
start = time.monotonic()
print('   > Solutions: ', path_actions(astar(root, manhattan_distance)))
end = time.monotonic()
print('   > Time Cost: ', str(end - start), 'seconds')

    