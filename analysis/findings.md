# Findings

The FAT32 coursework demonstrated that deleted files may remain recoverable when directory metadata or data clusters have not yet been overwritten.

Key technical findings included:

- A deleted FAT directory entry can often be identified by the `E5` first-byte marker.
- File metadata such as starting cluster and file size can still remain intact after deletion.
- FAT chain values can be used to reconstruct fragmented or multi-cluster files.
- Cluster-to-offset calculations are essential when validating findings in a hex editor.
- FTK Imager provides a useful secondary validation step after low-level changes are made.

The lab also showed why forensic recovery should be performed on copies of evidence rather than the original media.
