Title: About Chellow
Date: 2020-01-04 18:31

Chellow is an open source web application for checking the UK electricity and
gas bills of large organisations. It's been used in production since early
2006, and the code is hosted at
[GitHub site](https://github.com/WessexWater/chellow).

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
