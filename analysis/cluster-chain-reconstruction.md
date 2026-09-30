# Cluster Chain Reconstruction

One exercise focused on reconstructing `FILE1.JPG` from the FAT32 image.

The workflow involved:

1. Identifying the deleted file's directory entry.
2. Determining the starting cluster.
3. Locating the corresponding FAT entry.
4. Following the cluster chain through the FAT.
5. Mapping cluster numbers to data-region offsets.
6. Reviewing the relevant sectors in Active@ Disk Editor.
7. Reconstructing the file from its allocated clusters.
8. Validating the recovered output.

This process reinforced how FAT-based recovery depends on both directory metadata and allocation-chain interpretation.
