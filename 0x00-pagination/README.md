Pagination with REST APIs

This project provides an implementation of pagination techniques in REST API design using Python. The primary focus is on dataset pagination, managing hypermedia metadata, and ensuring deletion-resilient pagination.
Resources

    REST API Design: Pagination
    HATEOAS

Learning Objectives

By the end of this project, you will be able to:

    Paginate a dataset with page and page_size parameters.
    Use hypermedia metadata to paginate datasets.
    Design deletion-resilient pagination.

Requirements

    Code runs on Ubuntu 18.04 LTS with Python 3.7.
    Code style follows pycodestyle (version 2.5.*).
    All functions and coroutines are type-annotated.
    Files and functions are well-documented.
    All files end with a newline.

Project Setup

Download and place the dataset Popular_Baby_Names.csv in the root directory of this project.
Tasks Overview

    Simple Helper Function
    Write a helper function, index_range, to calculate pagination range using page and page size parameters.

    Simple Pagination
    Implement a Server class with a get_page method to paginate the Popular_Baby_Names.csv dataset, with assertions to verify valid parameters.

    Hypermedia Pagination
    Extend pagination by implementing the get_hyper method in Server to return pagination metadata such as next_page, prev_page, and total_pages.

    Deletion-Resilient Hypermedia Pagination
    Implement deletion-resilient pagination using get_hyper_index, which maintains consistent data results even when items are removed from the dataset between requests.

Usage Examples

Run the examples provided in each task's main.py file to see the expected output.
# Running Task 1
$ python3 0-main.py

# Running Task 2
$ python3 1-main.py

# Running Task 3
$ python3 2-main.py

# Running Task 4
$ python3 3-main.py

Repository Structure
alx-backend/
└── 0x00-pagination/
    ├── 0-simple_helper_function.py
    ├── 1-simple_pagination.py
    ├── 2-hypermedia_pagination.py
    ├── 3-hypermedia_del_pagination.py
    └── README.md
License

This project is provided under the MIT License.
