# Tygenie: Opsgenie Terminal UI

Tygenie is a terminal user interface used to handle Opsgenie alerts

Initially created to test [textual python framework](https://www.textualize.io/) it became day after day a complete and powerful tool to handle alerts on a daily basis at [OVH](https://github.com/ovh)

# Table of Contents

- [Features](#features)
- [Screenshots](#screenshots)
- [Requirements](#requirements)
- [Compatibility](#compatibility)
- [Limitations](#limitations)
- [Installation](#installation)
  - [pipx](#pipx)
  - [uv](#uv)
  - [pip](#pip)
- [Start the application](#start-the-application)
- [Configuration](#configuration)
- [Sample config](#sample-config)
- [Plugin](#plugin)
  - [Add your own plugin](#add-your-own-plugin)
    - [Customise alert list](#customise-alert-list)
    - [Customise alert description](#customise-alert-description)
  - [Enable the plugin](#enable-the-plugin)
- [Opsgenie API / OpenAPI / python-client](#opsgenie-api--openapi--python-client)
- [Related links](#related-links)
- [License](#license)

<a name="features"></a>

## Features

- list alerts by pages
- display details / description / tags / notes
- display current on-call user
- create your own display filter with your own key bindings to display specific alerts
- ack / unack alert
- tag / untag alert / custom tag
- add note
- automatic and manual refresh
- open alert in web browser
- In-app settings editor
- Alerts list might be customized by a plugin
- Alert details / description might be customised by a plugin

<a name="screenshots"></a>

## Screenshots

**Overview:**

> <img src="./assets/screenshots/overview.png" alt="overview" width="80%"/>

**In-app settings editor:**

> <img src="./assets/screenshots/settings.png" alt="settings" width="80%"/>

<a name="requirements"></a>

## Requirements

- python >= 3.11

<a name="compatibility"></a>

## Compatibility

- Tested/used on GNU/Linux and MacOS

<a name="limitations"></a>

## Limitations

- Desktop notification might not work on MacOS as [the application needs to be signed](https://github.com/samschott/desktop-notifier?tab=readme-ov-file#notes-on-macos) it depends how you installed python (eg using homebrew won't work)

- To select/past text in the application depending the terminal you are using use the following key:

  - iTerm Hold the OPTION key.
  - Gnome Terminal Hold the SHIFT key.
  - Windows Terminal Hold the SHIFT key.

Please refer to [textual FAQ](https://textual.textualize.io/FAQ/#how-can-i-select-and-copy-text-in-a-textual-app)

## Installation

<a name="pip"></a>

### pip

Each release of Tygenie is published on [pypi](https://pypi.org/project/tygenie/) so simply do a pip install

```bash
pip install tygenie
```

Or by using directly code from Github repository with pipx/uv

<a name="pipx"></a>

### pipx

```bash
pipx install git+https://github.com/ovh/tygenie.git
```

<a name="uv"></a>

### uv

```bash
uv tool install git+https://github.com/ovh/tygenie.git
```

<a name="start-the-application"></a>

## Start the application

```bash
tygenie
```

Or you might specify a custom configuration file

```bash
$ tygenie --help
usage: tygenie [-h] [--config CONFIG]

options:
  -h, --help            show this help message and exit
  --config CONFIG, -c CONFIG

```

<a name="configuration"></a>

## Configuration

```json5
{
  // Opsgenie configuration part
  opsgenie: {
    api_key: "", //                                                     Your Opsgenie integration API key
    username: "", //                                                    Your Opsgenie username
    host: "https://api.eu.opsgenie.com", //                             Opsgenie API endpoint
    webapp_url: "https://app.eu.opsgenie.com", //                       The Web URL to access Opsgenie from your web browser
    on_call_schedule_ids: [],
  },
  // Tygenie configuration part
  tygenie: {
    refresh_period: 60, //                                              Number of seconds between 2 automatic refresh (min 60s)
    open_detail_alert_on_enter: false, //                               If you don't want tygenie to automatically load alert details set it to true and press enter to get the details
    log: {
      enable: false, //                                                 Will enable API logging
      file: "/tmp/tygenie.log", //                                      Path where the log will be written
    },
    desktop_notification: {
      enable: true, //                                                  To enable desktop notification when new alerts are detected set it to true
      urgency: "Critical", //                                           Urgency level: can be Critical, Normal, Low
      when_on_call_only: false, //                                      When enable is true will send notification only when you are on call
    },
    alert_details: {
      default_tab: "description", //                                    Default tab displayed when loading alert details, values might be: RAW, tags, details, description
    },
    alerts: {
      date_format: "%d/%m %H:%M", //                                    Date format
      sort: "updatedAt", //                                             Field used to sort alerts when doing API call
      limit: 20, //                                                     Number of alerts to display
      display_page_by_priority: false, //                               To sort by priority set it to true
    },
    note_on_ack: {
      enable: false, //                                                 To automatically add a note when acking an alert set it to true
      message: "Alert has been acknowledged using Tygenie", //          Note to be added
    },
    note_on_unack: {
      enable: false, //                                                 To automatically add a note when unacking an alert set it to true
      message: "Alert has been unacknowledged using Tygenie", //        Note to be added
    },
    note_on_close: {
      enable: false, //                                                 To automatically add a note when closing an alert set it to true
      message: "Alert has been closed using Tygenie", //                Note to be added
    },
    note_on_tag: {
      enable: false, //                                                 To automatically add a note when adding a tag on alert set it to true
      message: "Tag '{tag}' has been added using Tygenie", //           Note to be added, you might use '{tag}' notation to add the value of the tag in the note
    },
    note_on_untag: {
      enable: false, //                                                 To automatically add a note when removing a tag on alert set it to true
      message: "Tag '{tag}' has been removed using Tygenie", //         Note to be added, you might use '{tag}' notation to add the value of the tag in the note
    },
    keybindings: {
      //                                                                Keybindings for each actions
      ack: "a", //                                                      to ack an alert
      unack: "U", //                                                    to unack an alert
      close: "c", //                                                    to close an alert
      tag: "t", //                                                      to tag an alert
      untag: "T", //                                                    to untag an alert
      refresh: "r", //                                                  to manually refresh alert list
      next_page: "right", //                                            load next page (will also work with page down, G, down key on last alert)
      previous_page: "left", //                                         load previous page (will also work with page up, g, up key on first alert)
      open_in_webbrowser: "ctrl+w", //                                  to open the selected alert in your default web browser
      focus_on_alerts_list: "f5", // to get focus on alert list
    },
    plugins: {
      alert_formatter: null, //                                         plugin name to use to display alert list (you might customize columns, messages, ... check plugin part)
      content_transformer: null, //                                     plugin name to use to that allow you to parse alert detail and customize the rendered markdown
    },
    default_tag: "XXXXX", //                                            default tag to apply to an alert
    default_filter: "opened", //                                        default defined filter to use hen starting the application
    filters: {
      //                                                                define your query filters here
      mine: {
        //                                                              mine filter will display the alert you are the owner of when using 'm' key
        key: "m",
        filter: "owner:<your username>",
        description: "Mine",
      },
      opened: {
        key: "o", //                                                    opened filter will display opened alerts only when using key 'o'
        filter: "status:open",
        description: "Opened",
      },
      all: {
        key: "A", //                                                    All filter, will display all the alerts
        filter: "",
        description: "All",
      },
    },
  },
}
```

When starting the application for the first time you will be bring on the
Settings screen which allow you to set your Opsgenie API key, username
and other related information.

<a name="sample-config"></a>

## Sample config

A sample config file is available [here](https://github.com/ovh/tygenie/blob/master/assets/tygenie.json)

<a name="plugin"></a>

## Plugin

Tygenie supports two type of customisation:

- Columns displayed in alerts (add/remove/rename) and content of each row (content is passed to a parser you might override)

- Content of alert description is also passed to parser and you might parse the content to change it before being displayed in Markdown

<a name="add-your-own-plugin"></a>

### Add your own plugin

1. In plugin directory add a directory with the name of your plugin, let's say 'Bob'
2. Depending what you want to customise:

- the alert list: add a file in Bob directory called 'alerts_list_formatter.py'
- content of alert description: add a file in Bob directory called 'alert_description_formatter.py'

<a name="customise-alert-list"></a>

#### Customise alert list

In file 'Bob/alerts_list_formatter.py'

```python

from rich.text import Text
from tygenie.alerts_list.formatter import BaseFormatter

# The class name must be the same as the plugin name
class Bob(BaseFormatter):
    # map method of the class with a column name
    # the dict is ordered so it will be displayed as it is declared
    # all the fields returned by the API are available by default
    displayed_fields = {
        "created_at": "Created",
        "status": "Status",
        "priority": "Priority",
        "region": "Region", # Custom field
        "message": "Message",
        "owner": "Owner",
        "closed_by": "Closed by",
    }

    # Let's add a custom field that we compute from the message
    # And return a rich Text object which allow us to customise the style
    def region(self, value) -> Text:
        m = re.match(r"^\[([^\[]+)\].*$", self.to_format["message"])
        region = ""
        if m and m.groups():
            region = m.group(1)
        return Text(region, style="#ffcf56")

    # Remove the region from the message as region is now a new column
    # And limit the length to 100 characters
    # And return a rich Text object with default style
    def message(self, value) -> Text:
        value = re.sub(r"^\[([^\[]+)\]\s*\:?\s*", "", value)
        if len(value) > 100:
            value = value[0:100] + "..."
        return Text(str(value))
```

Now the alert list has a new column called Region and the message does not contain any more the region string.

**Alert list with plugin**

> <img src="./assets/screenshots/overview_with_plugin.png" alt="Alert list with plugin" width="80%"/>

<a name="customise-alert-description"></a>

#### Customise alert description

In file 'Bob/description_alert_formatter.py'

The alert description content might be customised in 2 steps:

- before the content has been passed to Markdown processor, useful to sanitize content
- after the content has been passed to Markdown processor, useful to customize output (create clickable links)

The plugin should inherit from **tygenie.alert_details.description_formatter.BaseContentFormatter**

This class expose an **_execution_order_** dictionary **{"pre": [], "post": []}** which allow you to pass a list of methods that will be called respecting the order you list them

The only thing you have to to is implement your custom method and list them in the execution_order dictionary

```python
import re
from tygenie.alert_details.description_formatter import BaseContentFormatter

class Bob(BaseContentFormatter):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.execution_order["pre"] = [
            "pre_substitute_cariage_return_to_htmlttag",
        ]
        self.execution_order["post"] = [
            "post_custom_generate_url_by_id",
        ]

    # pre_substitute_* is a special form of method name that does the substitute for you
    # Just return a dict {"regexp": r"your regexp to match", "sub": r"the substitution"}
    def pre_substitute_cariage_return_to_htmlttag(self):
        return {"regexp": r"\r?\n", "sub": "<br>"}

    # Let's say your description return a list of ids you can easily find "#12345 #6789"
    # You would like to be able to click on that id to open a custom web interface that gives details on that id
    # And we want to do it after markdown processing
    def post_custom_generate_url_by_id(self):
        ids = re.findall( r"#(\d+)", self.content)
        url_base = 'https://www.corporate.com/mytool/details?id={id}'
        for id in set(ids):
            url = url_base.format(id=id)
            self.content = re.sub(
                f'#{id}', f"[#{id}]({url})", self.content
            )
```

<a name="enable-the-plugin"></a>

### Enable the plugin

Edit the settings file then go to the plugins json key:

```json
{
  "tygenie": {
    "plugins": {
      "alerts_list_formatter": "Bob",
      "alert_description_formatter": "Bob"
    }
  }
}
```

<a name="opsgenie-api--openapi--python-client"></a>

## Opsgenie API / OpenAPI / python-client

The current Opsgenie API python SDK does not implement the full API and the available [swagger.json](https://github.com/opsgenie/opsgenie-oas/blob/master/swagger.json) file is not a Swagger 2.0 compliant file.

A fork of opsgenie-oas repository had been done by Github user [bougar](https://github.com/bougar/opsgenie-oas) which contains a compliant Swagger 2.0 files. This file has been used to generate the Opsgenie client API consumer used in Tygenie.

The swagger file has been converted to openapi 3.0 and consumed by [openapi-python-client](https://github.com/openapi-generators/openapi-python-client)

<a name="related-links"></a>

## Related links

- Contribute: <https://github.com/ovh/tygenie/blob/master/CONTRIBUTING.md>
- Report bugs: <https://github.com/ovh/tygenie/issues>

<a name="license"></a>

## License

See <https://github.com/ovh/tygenie/blob/master/LICENSE>
