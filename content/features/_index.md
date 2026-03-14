+++
title = "Features"
extra.header_image = "/halo.png"
template = "features_section.html"
sort_by = "weight"
+++

## What is Chellow?

Chellow is an open source web application for checking the UK electricity and gas bills of large
I&C (Industrial and Commercial) organisations. It's been used in production since early 2006, and
the code is hosted at [GitHub](https://github.com/WessexWater/chellow).

## What type of organisation is Chellow aimed at?

Chellow is suitable for organisations for which one or more of the following is
true:

* Large number of supplies.
* High energy usage.
* Complex contract. 


## The Bill Validation Process

Supplier bills are imported into Chellow, and then they are checked by comparing them to
virtual bills that are created by Chellow. Any differences are due to either the actual bill being
incorrect or the virtual bill being incorrect. Once errors in the virtual bill have been corrected,
any remaining differences can be queried with the supplier. The idea is that at the end of the
process, the organisation can be sure that it's paying the correct amount for its electricity and
gas.

## Some Features of Chellow

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
  * RAB
  * CfD
  * Capacity Market
* Chellow also handles exported, generated and displaced electricity.

As a result of the bill checking process, Chellow ends up with a good dataset of energy that
has been used by the organisation. This can then be used for monthly reports for finance,
energy purchasing, energy management. Chellow also ends up with a good model of energy costs,
which can be used for forecasting. The model can also be run under different scenarios to answer
questions such as: how much money would be saved if solar panels were to be installed?

## Screenshots of Tasks In Chellow

To give you an idea of how Chellow is used, here are some screenshots showing how various tasks
are achieved in Chellow.
