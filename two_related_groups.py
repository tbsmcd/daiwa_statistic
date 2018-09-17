# -*- coding: utf-8 -*-
import os
from graphviz import Digraph


def main():
    g = Digraph(format='png')

    g.node('S', '差 di = xi - yi を求める', shape='box')
    g.node('D01', 'di は正規分布か？', shape='diamond')
    g.node('D02', '検定可能なデータ数か？', shape='diamond')
    g.node('R01', '1標本 t 検定', shape='box')
    g.node('R02', 'Wilcoxon 検定', shape='box')
    g.node('R03', '符号検定', shape='box')
    g.node('R04', '検定不可', shape='box')

    g.edge('S', 'D01')
    g.edge('D01', 'R01', 'yes')
    g.edge('D01', 'D02', 'no')
    g.edge('D02', 'R02', 'yes')
    g.edge('D02', 'R03', 'yes')
    g.edge('D02', 'R04', 'no')

    cd = os.path.dirname(os.path.abspath(__file__))
    g.render(filename=os.path.join(cd, 'related2groups'))


if __name__ == '__main__':
    main()