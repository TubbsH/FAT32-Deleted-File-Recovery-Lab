#!/usr/bin/env python3
"""Calculate a FAT32 data-region offset for a given cluster."""

import argparse

def cluster_offset(data_region_start: int, cluster_number: int, cluster_size: int) -> int:
    if cluster_number < 2:
        raise ValueError("FAT32 data clusters begin at cluster 2.")
    return data_region_start + ((cluster_number - 2) * cluster_size)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("cluster", type=int)
    parser.add_argument("--data-start", type=lambda x: int(x, 0), required=True)
    parser.add_argument("--cluster-size", type=int, default=4096)
    args = parser.parse_args()

    offset = cluster_offset(args.data_start, args.cluster, args.cluster_size)
    print(f"Cluster: {args.cluster}")
    print(f"Offset (decimal): {offset}")
    print(f"Offset (hex): 0x{offset:X}")

if __name__ == "__main__":
    main()
