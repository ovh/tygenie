# OVHCloud tygenie PCI team plugin

This is the OVHCLoud tygenie PCI team's plugin to be used with Tygenie

# Table of Contents

- [Requirements](#requirements)
- [Compatibility](#compatibility)
- [Limitations](#limitations)
- [Installation](#installation)
  - [pip](#pip)
- [Configuration](#configuration)

<a name="features"></a>

## Requirements

- python >= 3.11

<a name="compatibility"></a>

## Compatibility

- Tested/used on GNU/Linux and MacOS

<a name="limitations"></a>

## Installation

<a name="pip"></a>

### pip

pip install tygenie-plugins-ovh-pci

```bash
pip install tygenie-plugins-ovh-pci
```

Or by using directly code from stash repository

```bash
git clone ssh://git@stash.ovh.net:7999/cloud/tygenie.git
git checkout pci
cd tygenie
pip install .
```

<a name="configuration"></a>

## Configuration

Enable plugin called "PCI" (name of the directory inside plugins/ directory)

```json5
{
  tygenie: {
   plugins: {
      alert_formatter: "PCI", //                                         plugin name to use to display alert list (you might customize columns, messages, ... check plugin part)
      content_transformer: "PCI", //                                     plugin name to use to that allow you to parse alert detail and customize the rendered markdown
    },
}
```
