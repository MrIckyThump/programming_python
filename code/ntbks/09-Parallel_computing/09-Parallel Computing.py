#!/usr/bin/env python
# coding: utf-8

# # Parallel computing
# 
# - distributing the workload of complex processes can speed up work
# - a lot of processes can be parallelised
# - there are however cases where subprocesses can not be split up any more
# 
# - there is a fundamental limit to the speed up archievable
from joblib import Parallel, delayed
from math import sqrt
import time


def f(k):
    return 2*k

def benchmark(function, function_name):
    start = time.time()
    function()
    end = time.time()
    print("{0} seconds for {1}".format((end - start), function_name))

# #### Normal fast code

def list_single_thread(BIG=20000):
    list_a = [f(i) for i in range(BIG)]

# #### Parallelized code


def list_multi_thread(n_jobs=-1, BIG=20000): #default parameter is all cores
    list_b = Parallel(n_jobs=n_jobs)(delayed(f)(i) for i in range(BIG))

# #### Do a benchmark
if __name__ == '__main__':
    benchmark(list_single_thread,"single-threading")
    benchmark(list_multi_thread, "multi-threading")

# # But why is it not working?
# - joblib does not work in interactive sessions for some reason
