Title: Introduction
Date: 2019-08-26 14:31

Chellow is an open source web application for checking UK electricity and gas
bills for large organisations. It's been used in production since early 2006,
and so it's about time it had its own website, besides the [GitHub site](https://github.com/WessexWater/chellow) where the code is hosted.

Chellow is suitable for organisations for which one or more of the following is
true:

* Large number of supplies.
* High energy usage.
* Complex contract. 

Supplier bills are imported into Chellow, and then they are checked by
comparing them to virtual bills that are created by Chellow. Any differences
are due to either the actual bill being incorrect or the virtual bill being
incorrect. Once errors in the virtual bill have been corrected, any remaining
differences can be queried with the supplier. The idea is that at the end of
the process, the organisation can be sure that it's paying the correct amount
for its electricity and gas.

Some of the features of Chellow are:

* Automatic downloading of half-hourly data from data collector sites. The
  data is checked for missing data and estimates and a live list of errors is
  maintained. This can be sent to the data collector so that they can correct
  the errors.
* Based on [Market Domain Data](https://www.elexon.co.uk/operations-settlement/market-domain-data/).
* Uses Loss Adjustment Factors from Elexon to calculate GSP kWh.
* Uses Transmission Loss Multipliers from the National Grid to calculated
  NBP kWh.
* Has several built-in tariff elements, including:
  * DNUoS
  * TNUoS
  * AAHEDC
  * CCL
  * RO
* Chellow also handles exported, generated and displaced electricity.

As a result of the bill checking process, Chellow ends up with a good dataset
of electricity that has been used by the organisation. This can then be used
for monthly reports for finance, purchasing and operations departments. Chellow
also ends up with a good model of electricity costs, which can be run under
different scenarios to answer questions such as: how much money would be saved
if a solar panel were to be installed?

So that's an overview of Chellow, and I've probably missed a lot out. There are
all sorts of good ideas for this site, such as screenshots, tutorials and
videos. So if you'd like to contribute please do.
