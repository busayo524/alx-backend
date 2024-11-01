# 0x01. Caching

This project is part of the ALX Backend specialization. In this project, we implement various caching algorithms to optimize data retrieval and improve system performance. The caching algorithms covered include FIFO, LIFO, LRU, MRU, and LFU, each providing a unique approach to managing cached data.

## Table of Contents
1. [Background](#background)
2. [Learning Objectives](#learning-objectives)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Tasks](#tasks)
    - [Basic Dictionary Cache](#basic-dictionary-cache)
    - [FIFO Cache](#fifo-cache)
    - [LIFO Cache](#lifo-cache)
    - [LRU Cache](#lru-cache)
    - [MRU Cache](#mru-cache)
    - [LFU Cache](#lfu-cache)
7. [Requirements](#requirements)
8. [Author](#author)

## Background
Caching is a technique for temporarily storing frequently accessed data in a "cache," allowing faster access than querying the source repeatedly. This project covers a variety of cache replacement policies:
- **FIFO (First-In-First-Out)**: Discards the oldest entries first.
- **LIFO (Last-In-First-Out)**: Discards the most recent entries first.
- **LRU (Least Recently Used)**: Discards the least recently accessed entries.
- **MRU (Most Recently Used)**: Discards the most recently accessed entries.
- **LFU (Least Frequently Used)**: Discards the least accessed entries, with LRU as a tiebreaker.

## Learning Objectives
By completing this project, we aim to understand:
- What a caching system is and its purpose.
- The definitions of FIFO, LIFO, LRU, MRU, and LFU.
- The limitations and challenges of caching systems.

## Project Structure
```plaintext
0x01-caching/
├── base_caching.py          # Defines the base cache class with common methods and attributes
├── 0-basic_cache.py         # Implements a basic cache without limits
├── 1-fifo_cache.py          # Implements a FIFO cache
├── 2-lifo_cache.py          # Implements a LIFO cache
├── 3-lru_cache.py           # Implements an LRU cache
├── 4-mru_cache.py           # Implements an MRU cache
├── 100-lfu_cache.py         # Implements an LFU cache
├── README.md                # Project documentation
└── tests/
    ├── 0-main.py            # Test cases for Basic Cache
    ├── 1-main.py            # Test cases for FIFO Cache
    ├── 2-main.py            # Test cases for LIFO Cache
    ├── 3-main.py            # Test cases for LRU Cache
    ├── 4-main.py            # Test cases for MRU Cache
    └── 100-main.py          # Test cases for LFU Cache
