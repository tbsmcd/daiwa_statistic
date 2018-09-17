# -*- coding: utf-8 -*-
import os
from graphviz import Digraph


def main():
    g = Digraph(format='png')

    g.node('D01', '大標本（母分散既知）か？', shape='diamond')
    g.node('D02', '正規分布か？', shape='diamond')
    g.node('D03', '等分散か？', shape='diamond')
    g.node('D04', '検定可能なデータ数か？', shape='diamond')
    g.node('B01', '分散比 F 検定', shape='box')
    g.node('B02', '変数変換で正規化', shape='box')
    g.node('R01', '正規検定', shape='box')
    g.node('R02', '2標本 t 検定', shape='box')
    g.node('R03', 't 検定(Welch の方法)', shape='box')
    g.node('R04', 'Mann-Whitney 検定', shape='box')
    g.node('R05', '検定不可', shape='box')

    g.edge('D01', 'R01', 'yes')
    g.edge('D01', 'D02', 'no')
    g.edge('D02', 'B01', 'yes')
    g.edge('B01', 'D03')
    g.edge('D03', 'R02', 'yes')
    g.edge('D03', 'R03', 'no')
    g.edge('D03', 'R04', 'no')
    g.edge('D02', 'B02', 'no')
    g.edge('B02', 'B01')
    g.edge('D02', 'D04', 'no')
    g.edge('D04', 'R05', 'no')
    g.edge('D04', 'R04', 'yes')

    cd = os.path.dirname(os.path.abspath(__file__))
    g.render(filename=os.path.join(cd, 'independent2groups'))


if __name__ == '__main__':
    main()