# Lab Methodology

## Tools

- Active@ Disk Editor
- FTK Imager
- Autopsy 4.22.1 (used in related coursework)

## General Process

1. Open the forensic image in a disk editor.
2. Examine the FAT32 boot sector.
3. Record bytes per sector and sectors per cluster.
4. Calculate cluster size.
5. Locate FAT1, FAT2, and the data region.
6. Inspect directory entries for deleted records.
7. Decode starting-cluster and file-size fields.
8. Follow FAT chains for multi-cluster files.
9. Make controlled edits only on a working copy.
10. Validate results in FTK Imager.

## Evidence Handling

The original course image should remain unchanged. Any modification used to demonstrate recovery should be performed only on a duplicate working copy.
