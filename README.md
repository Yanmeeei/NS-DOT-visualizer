## How to use

```commandline
python3 visualizer.py table_1.xlsx table_2.xlsx [suffix] 
```
Where table_1 contains the following info: 
- Layer name
- Average time consumption (in sec)
- Output size (in mb)
- Average memory consumptiom (optional)

and table_2 contains the dependency:
- Source 
- Destination

This visualizer will generate a file **DOT_graph_code_\<suffix>.txt**

##Attention
- When recoring the dependency, remember to include concat operations. 