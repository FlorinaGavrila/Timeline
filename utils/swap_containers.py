#!/usr/bin/env python
"""
Script to swap containers from left to right or vice-versa.
If you add a photo (container) in the middle of the timeline, 
you would have two containers underneath another.
Note at which line in the index.html you need to reshuffle the
containers and provide it to this script.

To use this script:
python3 path/to/index.html path/to/index_update.html line_number_to_start

Rename index.html to index_old.html
Rename index_update.html to index.html
"""

import sys

source_file_path = sys.argv[1]
destination_file_path = sys.argv[2]
start_line_to_process = int(sys.argv[3])

line_index = 0

with open(source_file_path, 'r') as source_file:
    with open(destination_file_path, 'w') as destination_file:
        for line in source_file:
            line_index += 1
            if line_index >= start_line_to_process:
                if "_left" in line:
                    destination_file.write(line.replace("_left",
                                                        "_right"))
                elif "_right" in line:
                    destination_file.write(line.replace("_right",
                                                        "_left"))
                else:
                    destination_file.write(line)
            else:
                destination_file.write(line)
