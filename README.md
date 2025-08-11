# xml_repair_tool
This tool completes missing closed XML tags, thus allowing to use some info from a valid XML.

## INSTRUCTIONS (lazy style)

1. `python xml_repair_tool.py output.xml > fix_output.xml`
2. `cat output.xml fix_output.xml > fixed_output.xml`
3. `rebot fixed_output.xml`

On a Windows cmd window, you need to replace:

2. `copy /b output.xml+fix_output.xml fixed_output.xml`
