'''
 通过计算脚本深度，为脚本设置合适的优先级
 脚本之间的依赖关系可以认为是一个有向无环图，且较为稀疏
 因此首先采用邻接表来表示脚本间的依赖关系，可以是一个dict，key为脚本，value为该脚本的子节点
'''
# 维护一个isVisited字典和一个depthInfo字典
for script,childScript in adjaTable:
    if not isVisited[script]:
	isVisited[script] = True
	depthInfo[script] = getDepth(script,isVisited,adjaTable,depthInfo)

getDepth(script,isVisited,adjaTable,depthInfo):
    if not adjaTable.has_key(script):
	return 0
    cur_max = 0
    for childScript in adjaTable[script]:
        if not isVisited[childScript]:
            isVisited[script] = True
	    depthInfo[childScript] = getDepth(childScript,isVisited,adjaTable,depthInfo) 
        cur_max = max(cue_max,depthInfo[childScript])
    return cur_max+1

# 其实与二叉树求深度的递归方式一样，取子节点中最大深度加1，即为当前节点的深度
