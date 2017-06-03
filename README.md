# WowAir Python API

```python
from wowair import WowAirQuery

wowair = WowAirQuery(origin='YUL', destination='DUB')
for ticket in wowair.get_tickets():
    print ticket
```
