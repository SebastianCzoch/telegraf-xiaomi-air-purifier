# telegraf-xiaomi-air-purifier
[![Build Status](https://travis-ci.org/SebastianCzoch/telegraf-xiaomi-air-purifier.svg?branch=master)](https://travis-ci.org/SebastianCzoch/telegraf-xiaomi-air-purifier/branches) [![PyPI version](https://badge.fury.io/py/telegraf-xiaomi-air-purifier.svg)](https://badge.fury.io/py/telegraf-xiaomi-air-purifier) [![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/SebastianCzoch/telegraf-xiaomi-air-purifier/blob/master/LICENSE)

Telegraf plugin for the Xiaomi Air Purifier (supports versions: 2, 2pro, 2s)

## Requirements
- Device have to be accesable (in the same network)
- You have to have the python in at least 3.5 version

## Installation
```bash
$ pip install telegraf-xiaomi-air-purifier
```

## Usage
```bash
$ telegraf-xiaomi-air-purifier --ip DEVICE_IP_ADDRESS
```

### Example telegraf configuration
```ini
[[inputs.exec]]
  commands = ["telegraf-xiaomi-air-purifier --ip DEVICE_IP_ADDRESS"]
  data_format = "influx"

  [inputs.exec.tags]
    location = bedroom
```

## License
See [LICENSE](https://github.com/SebastianCzoch/telegraf-xiaomi-air-purifier/blob/master/LICENSE) file.
