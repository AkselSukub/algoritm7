#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from heapq import heappush, heappop

def print_tree(tree, level=0, levels=[]):
    if isinstance(tree, int):
        return

    for i, (node, child) in enumerate(tree.items()):
        if i == len(tree)-1 and level != 0:
            levels[level-1] = False
        branch = ''.join('│   ' if lev else '    ' for lev in levels[:-1])
        branch += "└── " if i == len(tree) - 1 else "├── "
        if level == 0:
            print(str(node))
        elif isinstance(child, int):
            print(branch + f"'{node}'" + " ── " + str(child))
        else:
            print(branch + str(node).split()[0])
        print_tree(child, level + 1, levels + [True])

def procedurehuffman(f):
    h = []
    l = len(f)
    visited_fs = set()  # Множество для хранения уникальных значений fs
    for i in f:
        heappush(h, (f[i], i))
    while len(h) > 1:
        f1, i = heappop(h)
        f2, j = heappop(h)
        fs = f1 + f2
        ord_val = ord('a')
        fl = str(fs)
        while fl in visited_fs:
            letter = chr(ord_val)
            # Добавить букву к значению fs через пробел
            fl = str(fs) + " " + letter
            ord_val += 1
        visited_fs.add(fl)
        f[fl] = {"{}".format(x): f[x] for x in [i, j]}
        del f[i], f[j]
        heappush(h, (fs, fl))
    return f

def codecreate(tree, codes, path=''):
    for i, (node, child) in enumerate(tree.items()):
        if isinstance(child, int):
            codes[node] = path[1:] + str(abs(i-1))
        else:
            codecreate(child, codes, path + str(abs(i-1)))
    return codes

def replace_sentence(sentence, dictionary):
    replaced_sentence = ''
    for char in sentence:
        if char in dictionary:
            replaced_sentence += dictionary[char]
        else:
            replaced_sentence += char
    return replaced_sentence

def huffman_decode(encoded_text, huffman_tree):
    decoded_text = ""
    key = list(huffman_tree.keys())[0]
    current_node = huffman_tree[key]
    for bit in encoded_text:
        for i, (node, child) in enumerate(current_node.items()):
            if str(i) != bit:
                if isinstance(child, int):
                    decoded_text += node
                    current_node = huffman_tree[key]
                    break
                current_node = child
                break

    return decoded_text

if __name__ == '__main__':
    sentence = input("Введите предложение: ")
    # Создаем словарь для хранения подсчета символов
    character_count = {}
    # Перебираем каждый символ в предложении
    for char in sentence:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    # Выводим результаты
    for char, count in character_count.items():
        print(f"'{char}': {count} раз(а)")
    tree = procedurehuffman(character_count)
    print_tree(tree)
    codes = codecreate(tree, dict())
    print(codes)
    coding_sentence = str(replace_sentence(sentence, codes))
    print(coding_sentence)
    newtext = huffman_decode(coding_sentence, tree)
    print(newtext)