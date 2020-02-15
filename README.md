# python-simpleclient
A TCP based Socket client implemented in Python3.

## Quick refernce manual

### Starting the client

To start the SimpleClient, just run it with python:

    $ py client.py

### Autoconfiguration

The Client supports automatic configuration. 
Using this feature will allow you to skip the Startup Prompts.
To use the AutoConfiguration feature, just rename the config.py.disabled to config.py!

```python
HOST = "127.0.0.1"
PORT = 42069
# CHARTYPE = "utf-8"
```
Default content of config.py.disabled.
