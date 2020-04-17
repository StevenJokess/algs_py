#!/usr/bin/env python
# coding=utf-8
'''
@version:
@Author: steven
@Date: 2020-04-17 21:30:12
@LastEditors: steven
@LastEditTime: 2020-04-17 23:50:06
@Description:算法图解 7.3 换钢琴 代码实现
'''
# 添加节点和邻居
graph = {}
# 起点为musicbook,简称muscbk
graph["muscbk"] = {}
graph["muscbk"]["record"] = 5
graph["muscbk"]["poster"] = 0

graph["record"] = {}
graph["record"]["guitar"] = 15
graph["record"]["grum"] = 20

graph["poster"] = {}
graph["poster"]["guitar"] = 30
graph["poster"]["grum"] = 35

graph["guitar"] = {}
graph["guitar"]["piano"] = 20

graph["grum"] = {}
graph["grum"]["piano"] = 10

graph["piano"] = {}  # 终点piano没有邻居

# 存储每个节点开销的散列表
infinity = float("inf")

costs = {}
costs["record"] = 5
costs["poster"] = 0
costs["guitar"] = infinity
costs["grum"] = infinity
costs["piano"] = infinity

# 存储父节点的散列表
parents = {}
parents["record"] = "muscbk"
parents["poster"] = "muscbk"
parents["guitar"] = None
parents["drum"] = None
parents["piano"] = None

processed = []  # 一个数组，用于记录处理过的节点。因为对于同一个节点，不用处理多次。


def find_lowest_cost_node(costs):
    # (2).to initial lowest_cost,removes other guessworks.
    lowest_cost = float("inf")
    # to initial cost node.
    lowest_cost_node = None
    # 遍历所有的节点
    for node in costs:
        cost = costs[node]
        # 如果当前节点的开销更低且未处理过
        if cost < lowest_cost and node not in processed:
            # 就将其视为开销最低的节点
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 在未处理的节点中找出开销最小的节点
node = find_lowest_cost_node(costs)

# 这个while循环在所有节点都被处理过后结束
while node is not None:
    cost = costs[node]
    # 遍历当前节点的所有邻居
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # 如果经当前节点前往该邻居更近
        if costs[n] > new_cost:
            # 就更新该邻居的开销
            costs[n] = new_cost
            # 同时将该邻居的父节点设置为当前节点
            parents[n] = node
    # 将当前节点标记为处理过
    processed.append(node)
    # 找出接下来要处理的节点，并做循环
    node = find_lowest_cost_node(costs)

if __name__ == '__main__':
    print("Cost from the start to each node:")
    print(costs)
