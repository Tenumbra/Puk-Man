# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    # Create open stack, list to track all visited states and start state
    Open = util.Stack()
    visited = []
    start = (problem.getStartState(),None,[])
    
    # Place start node in the open set
    Open.push(start)
    
    while not Open.isEmpty():
        
        n = Open.pop()
        Loc = n[0]
        Path = n[2]
        
        if problem.isGoalState(Loc) and Loc not in visited:
            return Path
        
        for succ in problem.getSuccessors(Loc):
            if succ[0] not in visited:
                visited.append(Loc)
                Open.push((succ[0],succ[1], Path + [succ[1]]))
    return []

#helper function to show everything in stack
def show(Stack):
    a = []
    while not Stack.isEmpty():
        a.append(Stack.pop())
    a.reverse()
    
    return a

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    # Create open stack, list to track all visited states and start state
    Open = util.PriorityQueue()
    
    all_visited = {}
    start = (problem.getStartState(),None,[])
       
    # Place start node in the open set
    Open.push(start,1)
       
    while not Open.isEmpty():
        
        n = Open.pop()
        
        Loc = n[0]
        Path = n[2]
        
        #This save state has everything you need
        if problem.isGoalState(Loc) and Loc not in all_visited:
            return Path
        
        for succ in problem.getSuccessors(Loc):
            if succ[0] not in all_visited:
                all_visited[Loc] = problem.getCostOfActions(Path)
                Open.push((succ[0],succ[1], Path + [succ[1]]),1)
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # Create open stack, list to track all visited states and start state
    att = []
    Open = util.PriorityQueue()
    
    # Place start node in the open set
    Open.push([[(problem.getStartState(), None, 0)], 0], 0)

    while not Open.isEmpty():
        
        n = Open.pop()
        
        Loc = n[0]
        path = n[1]
        end = Loc[-1][0]
        
        #This save state has everything you need
        if problem.isGoalState(end):
            expand = []
            for state in Loc:
                expand.append(state[1])
            expand.pop(0)
            return expand

        if not(end in att):
            for succ in problem.getSuccessors(end):
                cost = path + succ[2]
                Open.push([Loc + [succ], cost], cost)
                
            att.append(end)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # Create open stack, list to track all visited states and start state
    att = []
    Open = util.PriorityQueue()
    
    # Place start node in the open set
    Open.push([[(problem.getStartState(), None, 0)], 0],
                heuristic(problem.getStartState(), problem))

    while not Open.isEmpty():
        
        n = Open.pop()
        
        Loc = n[0]
        path = n[1]  
        end = Loc[-1][0]

        #This save state has everything you need
        if problem.isGoalState(end):
            expand = []
            for state in Loc:
                expand.append(state[1])
            expand.pop(0)
            return expand

        if not(end in att):
            for succ in problem.getSuccessors(end):
                nPath = Loc + [succ]
                cost = path + succ[2]
                Open.push([nPath, cost], cost + heuristic(succ[0], problem))
                
            att.append(end)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
