+++
title = "Elexon Importer"
date = 2025-11-22T00:00:00Z
template = "feature_page.html"
description = "Automatic import of Elexon data"
weight = 3
+++

For most industry data we can use APIs, but some, such as DNO charging statements, have to be
manually downloaded. We download them centrally to a repository which we call the
[Rate Server](https://github.com/WessexWater/chellow-rates).

Clicking on the <code>Automatic Importer: Rate Server</code> link takes you to the page for
importing the files from the rate server into Chellow. The importer runs once a day automatically by
default, so you should rarely have to attend to it.

## Rate Server Importer

![Rate Server Importer](screenshot_rate_server_importer.png)

For a new installation of Chellow it's a good idea to click the <code>Import Now</code> button
to start an import. Click the browser <code>refresh</code> button to see the latest progress in the
log. Make sure it completes successfully.

![Import Completed](screenshot_rate_server_completed.png)
