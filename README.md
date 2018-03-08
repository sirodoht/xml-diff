# XML diff

Contents:

[`diff.py`](diff.py): main diff algorithm module  
[`demo.py`](demo.py): module that uses diff with demo data  
[`benchmark.py`](benchmark.py): module that uses diff with various data files inside [datafiles](datafiles) directory  


## Benchmark results

|Data file      |Size (left/right)|Duration (ms)|Memory (MB)|
|---------------|-----------------|-------------|-----------|
|`10x`          | 2.5K/2.1K       |~1           |~10        |
|`20x`          | 4.9K/4.0K       |~4           |~10        |
|`40x`          | 9.8K/8.0K       |~27          |~9         |
|`50x`          | 12K/10K         |~47          |~10        |
|`60x`          | 15K/12K         |~72          |~13        |
|`65x`          | 16K/13K         |~87          |~13        |
|`65x_add`      | 14K/16K         |~70          |~14        |
|`65x_add_minus`| 13K/13K         |~84          |~13        |
|`70x`          | 17K/14K         |~106         |~13        |
|`80x`          | 20K/16K         |~159         |~13        |
|`100x`         | 24K/20K         |~314         |~16        |
|`150x`         | 37K/30K         |~941         |~22        |
|`250x`         | 61K/50K         |~4233        |~42        |
|`500x`         | 123K/100K       |~34402       |~139       |

Duration was measured with [`time.process_time()`](https://docs.python.org/3/library/time.html#time.process_time).
Memory was measured with [`memory-profiler`](https://pypi.python.org/pypi/memory_profiler).


## Datafiles

Each number per datafile expresses the number of records this XML file holds.
For every record, the `left` file includes 6 properties, and the `right` 5, so
in (almost) all diffs the algorithm has to find lines that miss and lines that
exist in both versions (left and right). There are two exceptions, `65x_add`
and `65x_add_minus`. In `65x_add` the right version has more lines than the left,
and in `65x_add_minus` there are both line additions and line deletions. As we 
can see in the benchmarks, it didn't make much difference to the duration
(at least for those file sizes).
