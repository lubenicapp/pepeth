from utils.w3 import w3
import threading
import json


def block_number():
    return w3.eth.get_block_number()


def blocks_prop(count=1000, prop='size'):
    last = block_number()
    props = [0] * count
    threads = []
    for i in range(count):
        s = threading.Thread(target=get_block_data, args=(last - count + i, prop, props, i))
        s.start()
        threads += [s]
    for t in threads:
        t.join()
    return {prop: props}


def get_block_data(nth_block, prop, data, index):
    block = w3.eth.getBlock(nth_block)
    data[index] = block[prop]
