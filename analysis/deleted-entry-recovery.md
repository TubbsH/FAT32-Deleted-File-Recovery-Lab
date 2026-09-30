# Deleted Directory Entry Recovery

In FAT file systems, deletion commonly changes the first byte of a directory entry to `E5`, indicating that the entry is available for reuse.

The coursework included locating deleted entries and restoring the first filename character in a controlled disk image. Entries such as `_NE.TXT`, `_WO.TXT`, and `_HREE.TXT` were examined and restored by replacing the deletion marker with the expected filename character.

After editing, the image was re-opened in FTK Imager to verify whether the restored entries appeared correctly.

This exercise demonstrated the relationship between raw hex values, directory-entry metadata, and how forensic tools interpret file-system structures.
