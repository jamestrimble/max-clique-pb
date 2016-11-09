import sys

class Graph(object):
    def __init__(self, adjmat):
        self.n = len(adjmat)
        self.adjmat = adjmat
        self.degree = [sum(row) for row in self.adjmat]

    def write_opb(self):
        constraints = []
        for i in range(self.n-1):
            for j in range(i+1, self.n):
                if not self.adjmat[i][j]:
                    constraints.append("-1 x{} -1 x{} >= -1;".format(i+1, j+1))

        objective = " ".join("-1 x{}".format(i+1) for i in range(self.n))

        print "* #variable= {} #constraint= {}".format(self.n, len(constraints))
        print "min: {} ;".format(objective)
        for c in constraints:
            print c

def read_instance(lines):
    lines = [line.strip().split() for line in lines]
    p_line = [line for line in lines if line[0]=="p"][0]
    e_lines = [line for line in lines if line[0]=="e"]
    n = int(p_line[2])
    adjmat = [[False] * n for _ in range(n)]
    for e in e_lines:
        v, w = int(e[1])-1, int(e[2])-1
        if v==w:
            print "Loop detected", v
        if adjmat[v][w]:
            print "Duplicate edge", v, w
        adjmat[v][w] = adjmat[w][v] = True
    return Graph(adjmat)

if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        g = read_instance([line for line in f.readlines()])
    g.write_opb()
