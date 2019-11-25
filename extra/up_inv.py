#!/usr/bin/env python3

import sys
import re
import shutil

"""
Вспомогательный скрипт для переноса хоста из одной инвентори группы в другую в
рамках сортировки хостов.

Input: up_inv.py <inventory> <hostname> <ping> <setup> <sudo>

<inventory> - path to inventory file
<hostname> - checked hostname
<ping> - ping is ok (boolean)
<setup> - ansible setup is ok? (boolean)
<sudo> - ansible become is ok? (boolean)

"""

def move_host(inv, host, block):
    print(inv, host, block)
    with open(inv, 'r') as r:
        with open('tempfile', 'w') as w:
            cur_block = None
            host_not_found = True
            writed = False

            for line in r:
                block_match = re.match(r'\[(.*)\]', line)
                if block_match:
                    # Если полностью прошли нужный блок и не нашли хост то
                    # добавляем в конец блока
                    if cur_block == block and host_not_found:
                        w.write(host+'\n')
                        writed = True

                    cur_block = block_match.group(1)
                    w.write(line)
                    continue

                host_match = re.match(host, line)
                if host_match:
                    if cur_block == block:
                        host_not_found = False
                        writed = True
                    else:
                        # Не вставлять хост если не тот блок из
                        # зарезирвированных
                        if cur_block in ['unreachable', 'ping', 'reachable',
                                         'best']:
                            continue

                w.write(line)

            if not writed:
                # Если прошли весь файл и не нашли нужный блок, то нужно его
                # добавить
                if cur_block != block:
                    w.write('['+block+']\n')
                w.write(host+'\n')
                writed = True

    shutil.move('tempfile', inv)


def main():
    print(sys.argv)

    inv = sys.argv[1]
    host = sys.argv[2]

    false_list = ['False', 'false', 'f']
    if sys.argv[3] in false_list:
        block = 'unreachable'
    elif sys.argv[4] in false_list:
        block = 'ping'
    elif sys.argv[5] in false_list:
        block = 'reachable'
    else:
        block = 'best'

    move_host(inv, host, block)


if __name__ == "__main__":
    main()
