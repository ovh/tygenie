import re

from tygenie.alert_details.description_formatter import BaseContentFormatter

ATELIER_URL_BY_ID = (
    "https://interne.ovh.{tld}/atelier/astreinte/control.cgi?nummachine={id}"
)
ATELIER_URL_BY_NAME = (
    "https://interne.ovh.{tld}/atelier/astreinte/machines.cgi?nom={name}"
)


class PCI(BaseContentFormatter):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.execution_order["pre"] = [
            "pre_substitute_cariage_return_to_htmlttag",
        ]
        self.execution_order["post"] = [
            "post_substitute_unescape_characters",
            "post_custom_generate_atelier_url_by_id",
            "post_custom_generate_atelier_url_by_name",
        ]

    def pre_substitute_cariage_return_to_htmlttag(self):
        return {"regexp": r"\r?\n", "sub": "<br>"}

    def post_substitute_unescape_characters(self):
        return {"regexp": r"\\(\-|\_|\.|\+|\*|\#)", "sub": r"\1"}

    def post_custom_generate_atelier_url_by_id(self):
        hosts = re.findall(
            r"((host|snat)(\d+)\.(\S+)\.cloud\.ovh\.(net|us))", self.content
        )
        # [('host1234.preprod.gra1.cloud.ovh.net', 'host', 1234', 'preprod.gra1', 'net'), ('host12.bhs1.cloud.ovh.net', '12', 'bhs1', 'net')]
        for host in set(hosts):
            tld = ""
            host_id = host[2]
            host_name = host[0]
            if re.match(r".*(bhs|syd|sgp)\-?\d+", host[3]):
                tld = "ca"
            elif host[4] == "net":
                tld = "net"
            elif host[4] == "us":
                tld = "us"

            atelier_url = ATELIER_URL_BY_ID.format(id=host_id, tld=tld)
            self.content = re.sub(
                host_name, f"[{host_name}]({atelier_url})", self.content
            )

    def post_custom_generate_atelier_url_by_name(self):
        # Open nsxxx.ip-xxxxx  in atelier/astreinte by forging MD link
        hosts = re.findall(r"(ns\d+\.ip\-\d+\-\d+\-\d+\.(eu|us|net))", self.content)
        for host in hosts:
            tld = ""
            host_name = host[0]
            if host[1] == "net":
                tld = "ca"
            elif host[1] == "eu":
                tld = "net"
            elif host[1] == "us":
                tld = "us"

            atelier_url = ATELIER_URL_BY_NAME.format(name=host_name, tld=tld)
            self.content = re.sub(
                host_name, f"[{host_name}]({atelier_url})", self.content
            )
