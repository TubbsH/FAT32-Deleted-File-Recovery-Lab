# FAT32 Structure Analysis

FAT32 stores information about files using several major structures: the boot sector, File Allocation Tables, directory entries, and the data region.

In the coursework, the boot sector was used to identify values including bytes per sector and sectors per cluster. With 512 bytes per sector and 8 sectors per cluster, each cluster contained 4096 bytes.

The FAT tables were then examined to understand how cluster chains describe file allocation. Directory entries were analyzed at the hex level to identify file names, attributes, starting clusters, and file sizes.

This process demonstrated how file recovery requires understanding both metadata and the underlying data region rather than relying only on graphical forensic tools.
