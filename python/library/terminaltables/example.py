# -*- coding: utf-8 -*-
from terminaltables import AsciiTable, SingleTable, DoubleTable, GithubFlavoredMarkdownTable

table_data = [
    ["Name", "Size"],
    ["test1", "512M"],
    ["test2", "1G"],
]

ascii_table = AsciiTable(table_data)
print ascii_table.table

ascii_table.inner_row_border = True
print ascii_table.table

print

single_table = SingleTable(table_data)
print single_table.table

single_table.inner_row_border = True
print single_table.table

single_table.title="List"
print single_table.table

print 

gfw_table = GithubFlavoredMarkdownTable(table_data)
print gfw_table.table


"""
+-------+------+
| Name  | Size |
+-------+------+
| test1 | 512M |
| test2 | 1G   |
+-------+------+
+-------+------+
| Name  | Size |
+-------+------+
| test1 | 512M |
+-------+------+
| test2 | 1G   |
+-------+------+

┌───────┬──────┐
│ Name  │ Size │
├───────┼──────┤
│ test1 │ 512M │
│ test2 │ 1G   │
└───────┴──────┘
┌───────┬──────┐
│ Name  │ Size │
├───────┼──────┤
│ test1 │ 512M │
├───────┼──────┤
│ test2 │ 1G   │
└───────┴──────┘
┌List───┬──────┐
│ Name  │ Size │
├───────┼──────┤
│ test1 │ 512M │
├───────┼──────┤
│ test2 │ 1G   │
└───────┴──────┘

| Name  | Size |
|-------|------|
| test1 | 512M |
| test2 | 1G   |

"""
