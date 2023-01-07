[![Security Status](https://www.murphysec.com/platform3/v3/badge/1611037292781666304.svg)](https://www.murphysec.com/accept?code=53983537fcaa354e214ba496d0d88e93&type=1&from=2&t=2)

# logging4
A tiny logging tool

## install
```bash
$pip install --upgrade logging4 
```

## usage

```python
import sys
import logging4

logger = logging4.Logger(name="MyLogger")

formatter = '[[time]] - [[name]] - [[level_name]] - [[msg]]'

# add/del channel
logger.add_channel(filename='log.txt', level=logging4.WARNING)
logger.add_channel(filename=sys.stdout, level=logging4.ERROR, formatter=formatter)
logger.add_channel(filename='log2.txt', level=logging4.INFO)
logger.del_channel(filename='log2.txt')
```

use logger:
```python
logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')
```