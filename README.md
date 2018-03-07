# XML diff

Contents:

[`diff.py`](diff.py): main diff algorithm file  
[`demo.py`](demo.py): module that uses diff with demo data  
[`benchmark.py`](benchmark.py): module that uses diff with various data files inside [datafiles](datafiles) directory  


## Benchmark results

|Data file      |Duration (ms)|
|---------------|-------------|
|`10x`          |1.038        |
|`20x`          |4.941        |
|`40x`          |27.676       |
|`50x`          |47.908       |
|`60x`          |72.745       |
|`65x`          |87.894       |
|`65x_add`      |70.467       |
|`65x_add_minus`|84.918       |
|`70x`          |106.626      |
|`80x`          |159.179      |
|`100x`         |314.476      |
|`150x`         |941.780      |
|`250x`         |4233.445     |
|`500x`         |34402.443    |

