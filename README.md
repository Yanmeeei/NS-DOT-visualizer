## How to use

```commandline
python3 visualizer.py table_1.csv table_2.csv [suffix] 
```
Where table_1 contains the following info: 
- Layer name
- Average time consumption (in sec)
- Output size (in mb)
- Average memory consumptiom 

Note: measure the data for every layer only once. 

and table_2 contains the dependency:
- Source 
- Destination

Note: measure the dependency for every output, but only before it is used in another layer. 


This visualizer will generate a file **DOT_graph_code_\<suffix>.txt**

## Attention
- When recoring the dependency, remember to include concat operations.

# Update: colorer
can use standard part/dep/prof to color network

```shell
python3 colorer.py prof.csv dep.csv part.csv
```