class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = StackNode(data)
        if self.top:
            node.next = self.top
        self.top = node

    def pop(self):
        if self.top:
            data = self.top.data
            self.top = self.top.next
            return data
        return None

    def print(self):
        node = self.top
        while node:
            print(node.data, end=" -> ")
            node = node.next
        print("None", end="")


class Project:
    def __init__(self, name, dependencies):
        self.name = name
        self.dependencies = dependencies
        self.state = "BLANK"

# time: O(P + D), space: O(P)
def build_order(projects, dependencies):
    graph = {}
    for project in projects:
        graph[project] = Project(project, [])
    for dependency in dependencies:
        graph[dependency[0]].dependencies.append(dependency[1])

    stack = Stack()
    for key in graph:
        project = graph[key]
        if project.state == "BLANK" and not DFS(graph, project, stack):
            return None
    return stack

def DFS(graph, project, stack):
    if project.state == "PARTIAL":
        return False # cycle

    if project.state == "BLANK":
        project.state = "PARTIAL"
        for d in project.dependencies:
            dependent = graph[d]
            if not DFS(graph, dependent, stack):
                return False
        project.state = "COMPLETE"
        stack.push(project.name)
    return True


projects = ["a", "b", "c", "d", "e", "f"]
dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]
order = build_order(projects, dependencies)
order.print()
