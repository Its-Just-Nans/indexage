"""assets"""

from string import Template

CSS = """
.thumbnail {
  position: relative;
  z-index: 0;
}

.thumbnail:hover {
  background-color: transparent;
  z-index: 50;
}

.thumbnail span {
  position: absolute;
  padding: 5px;
  left: -1000px;
  border: 1px dashed gray;
  display: none;
  color: black;
  text-decoration: none;
}

.thumbnail span > * {
  border-width: 0;
  padding: 2px;
  min-width: 800px;
}

.thumbnail:hover span {
  display: block !important;
  top: 0;
  left: 60px; /*position where enlarged image should offset horizontally */
"""


BACK_ICO = "data:image/gif;base64,R0lGODlhFAAWAMIAAP///8z//5mZmWZmZjMzMwAAAAAAAAAAACH+TlRoaXMgYXJ0IGlzIGluIHRoZSBwdWJsaWMgZG9tYWluLiBLZXZpbiBIdWdoZXMsIGtldmluaEBlaXQuY29tLCBTZXB0ZW1iZXIgMTk5NQAh+QQBAAABACwAAAAAFAAWAAADSxi63P4jEPJqEDNTu6LO3PVpnDdOFnaCkHQGBTcqRRxuWG0v+5LrNUZQ8QPqeMakkaZsFihOpyDajMCoOoJAGNVWkt7QVfzokc+LBAA7"

FOLDER_ICO = "data:image/gif;base64,R0lGODlhFAAWAMIAAP/////Mmcz//5lmMzMzMwAAAAAAAAAAACH+TlRoaXMgYXJ0IGlzIGluIHRoZSBwdWJsaWMgZG9tYWluLiBLZXZpbiBIdWdoZXMsIGtldmluaEBlaXQuY29tLCBTZXB0ZW1iZXIgMTk5NQAh+QQBAAACACwAAAAAFAAWAAADVCi63P4wyklZufjOErrvRcR9ZKYpxUB6aokGQyzHKxyO9RoTV54PPJyPBewNSUXhcWc8soJOIjTaSVJhVphWxd3CeILUbDwmgMPmtHrNIyxM8Iw7AQA7"

UNKNOWN_ICO = "data:image/gif;base64,R0lGODlhFAAWAMIAAP///8z//5mZmTMzMwAAAAAAAAAAAAAAACH+TlRoaXMgYXJ0IGlzIGluIHRoZSBwdWJsaWMgZG9tYWluLiBLZXZpbiBIdWdoZXMsIGtldmluaEBlaXQuY29tLCBTZXB0ZW1iZXIgMTk5NQAh+QQBAAABACwAAAAAFAAWAAADaDi6vPEwDECrnSO+aTvPEQcIAmGaIrhR5XmKgMq1LkoMN7ECrjDWp52r0iPpJJ0KjUAq7SxLE+sI+9V8vycFiM0iLb2O80s8JcfVJJTaGYrZYPNby5Ov6WolPD+XDJqAgSQ4EUCGQQEJADs="

HTML_TEMPLATE = f"""
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <title></title>
        <style></style>
    </head>
    <body>
        <h1></h1>
        <table>
            <tr>
                <th valign="top">
                    <img src="{FOLDER_ICO}" alt="[ICO]" />
                </th>
                <th><a href="?C=N;O=D">Name</a></th>
                <th><a href="?C=M;O=A">Last modified</a></th>
                <th><a href="?C=S;O=A">Size</a></th>
                <th><a href="?C=D;O=A">Description</a></th>
            </tr>
            <tr>
                <th colspan="5"><hr /></th>
            </tr>
            <tr>
                <td valign="top">
                    <img src="{BACK_ICO}" alt="[PARENTDIR]" />
                </td>
                <td><a href="..">Parent Directory</a></td>
                <td>&nbsp;</td>
                <td align="right">-</td>
                <td>&nbsp;</td>
            </tr>
            <placeholder></placeholder>
            <tr>
                <th colspan="5"><hr /></th>
            </tr>
        </table>
        <address></address>
    </body>
</html>"""


ROW_TEMPLATE = Template(
    """<tr>
    <td valign="top"><img src="$url" alt="[   ]" /></td>
    <td><a $add href="$file">$file $other</a></td>
    <td align="right">$date</td>
    <td align="right">$size</td>
    <td>&nbsp;</td>
</tr>"""
)
