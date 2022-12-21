import numpy as np
import math
import time

n = 500

# A function that gives possible childrens for a node (full map)
def children_full(map,node):
  # Directions (8-connected grid)
  move = [[0,1],[1,1],[1,0],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]

  rbound,cbound = map.shape[0]-1, map.shape[1]-1
  node = np.array(node)
  ans = []
  for i in move:
    look = np.array(i)
    step = node + look
    r,c = step[0], step[1]
    # If in the grid
    if 0<=r<=rbound and 0<=c<=cbound:
      # If empty cell
      if map[r,c] == 0:
        ans.append(step)
  return ans # array of np.arrays

# A function that gives possible childrens for a node (shorter map)
def children(map,node, r1, c1):
  # Directions (8-connected grid)
  move = [[0,1],[1,1],[1,0],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]

  rbound,cbound = map.shape[0]-1, map.shape[1]-1
  node = np.array(node)
  ans = []
  for i in move:
    look = np.array(i)
    step = node + look
    r,c = step[0], step[1]
    # If in the grid
    if 0<=r-r1<=rbound and 0<=c-c1<=cbound:
      # If empty cell
      if map[r-r1,c-c1] == 0:
        ans.append(step)
  return ans 

# Heuristics (euclidean distance 2D - shorter because assumes no obstacles)
def h(node, goal):
  heur = np.linalg.norm(node-goal)
  return heur

# Shorter map (local area of map)
def local_map(map, node, n):
  rbound,cbound = map.shape[0]-1, map.shape[1]-1
  r1,c1 = max(0,node[0]-n), max(0,node[1]-n)
  r2,c2 = min(rbound,node[0]+n), min(cbound,node[1]+n)
  return map[r1:r2,c1:c2], r1, c1

# makes a dictionary to append in PQ
def transform_dict(node, value):
  assert isinstance(node, np.ndarray) # and node.shape == (2, 1)
  dic = {'node': node, 'g':value}
  return dic

# Priority stack (takes 2D argument)
class PS():
    def __init__(self):
      # array of dictionaries like: [{'node':22, 'g':3},{'node':28, 'g':1},{'node':62, 'g':2}]
      self.arr = []
        
    def push(self,x):
      self.arr.append(x)
      # sor w.r.t. to second value
      self.arr.sort(key=lambda i: i['g'],reverse=True)
        
    def out(self):
      # gives the full dictionary that is popped (for one node)
      dic = self.arr.pop()
      # returns the coordinate only
      node = dic['node']
      assert isinstance(node, np.ndarray) #and node.shape == (2, 1)
      return node

    def print(self):
      print(self.arr)
    
    def length(self):
      return len(self.arr)

# total_path = [np.array([0, 0])]
total_path = []
ulta_path = []


def RTAAstar(n,robotpos, targetpos, envmap):
  
  '''
  Fills the array next_states.

  arguments: number of nodes to expand 'n', start node 'robotpos', current goal position 'targetpos', map 'envmap'
  '''
  expanded = []
  go = True
  V = {tuple(robotpos):0}
  parent = {}
  open = PS()
  outer_V = {}
  open.push(transform_dict(robotpos, 0))
  local_focus = False

  # important part of map
  rbound,cbound = envmap.shape[0]-1, envmap.shape[1]-1
  if n < rbound and n < cbound:
    map,r1,c1 = local_map(envmap, robotpos, n)
    local_focus = True

  while open.arr:
    if open.length() >= n:
      go = False
    i = open.out()
    expanded.append(i)
    if local_focus:
      childs = children(map, i, r1, c1)
    else:
      childs = children_full(envmap, i)
    for j in childs:
      assert isinstance(tuple(j), tuple)
      if (tuple(j) not in V) or V[tuple(i)]+1 < V[tuple(j)]:
        V[tuple(j)] = V[tuple(i)]+1
        parent[tuple(j)] = i
        if np.array_equal(j, targetpos) == True:
          g_j = V[tuple(j)] + h(j, targetpos)
          outer_V[tuple(j)] = g_j
          break
        else:
          if go:
            g_j = V[tuple(j)] + h(j, targetpos)
            open.push(transform_dict(j, g_j))
          else:
            g_j = V[tuple(j)] + h(j, targetpos)
            outer_V[tuple(j)] = g_j
          
  if tuple(targetpos) in outer_V:
    r_from = targetpos
  else:
    r_from = min(outer_V, key=outer_V.get)
  i = 2
  while i>1:
      node = parent[tuple(r_from)]
      ulta_path.append(node)
      if np.array_equal(node, robotpos):
          break
      else:
          r_from = node
  # to remove the initial position repetetion
  ulta_path.pop()

  return ulta_path

def robotplanner(envmap, robotpos, targetpos):

  if len(ulta_path) == 0:
    # complete the function with arguments
    RTAAstar(n, robotpos, targetpos, envmap)
  x = ulta_path.pop()
  total_path.append(x)
  return x



