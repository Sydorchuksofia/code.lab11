
def tree_by_levels(node):
    if node is None:
        return []
    res = []
    like_que = [node]
    while like_que != []:
        elem = like_que[0]
        res.append(elem.value)
        if elem.left:
            like_que.append(elem.left)
        if elem.right:
            like_que.append(elem.right)
        if len(like_que) > 1:
            like_que = like_que[1:]
        else:
            like_que = []
    return res
