import difflib
                f.write("old file mode %o\n" % old_mode)
            f.write("new file mode %o\n" % new_mode) 
            f.write("deleted file mode %o\n" % old_mode)
    f.writelines(difflib.unified_diff(old_contents, new_contents, 