def most_leaf_nodes(total):

    layer = 0

    while 2 ** layer - 1 < total:
        layer += 1

    now_layer = layer - 1

    now_layer_nodes = 2 ** (layer - 2)

    now_total_nodes = 2 ** (layer - 1) - 1

    left_nodes = total - now_total_nodes

    leaf_nodes = now_layer_nodes - (left_nodes // 2 + left_nodes % 2) + left_nodes

    return leaf_nodes


print(most_leaf_nodes(2019))

