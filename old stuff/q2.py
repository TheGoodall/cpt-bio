from graphviz import Digraph

dot = Digraph()

top = Digraph()

top.attr(rank="same")



top.node("A")
top.node("B")
top.node("C")
top.node("D")
top.node("E")
top.node("F")

dot.subgraph(top)


dot.node("AB")
dot.edge("AB", "A", "7.5")
dot.edge("AB", "B", "7.5")


dot.node("ABE")
dot.edge("ABE", "AB", "4.5")
dot.edge("ABE", "E", "12")

dot.node("CD")
dot.edge("CD", "C", "15")
dot.edge("CD", "D", "15")

dot.node("ABCDE")
dot.edge("ABCDE", "ABE", "6.25")
dot.edge("ABCDE", "CD", "3.25")

dot.node("ABCDEF")
dot.edge("ABCDEF", "ABCDE", "6.875")
dot.edge("ABCDEF", "F", "25.125")


dot.render('q2.gv')
