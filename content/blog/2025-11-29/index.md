+++
title = "ECOES"
date = 2025-11-29T00:00:00Z
template = "blog_post.html"
+++

In the [previous post](https://www.chellow.org/blog/2025-11-22/) I wrote that each supply
has an LLFC, or to be more precise, each MPAN has an LLFC, one for import and one for
export if the supply has an export MPAN. The electricity industry view of all electricity
supplies and their characteristics (such has LLFC) is stored in a database called
[ECOES](https://www.ecoes.co.uk/). Any non-domestic customer can sign up to ECOES and ask
to be granted visibility of the MPANs for which they're a customer.

There's a web interface to the database which is useful for doing one-off lookups, but the
really useful thing is the CSV download of all your supplies and their characteristics.
Here is the info you get on each MPAN:

* MPAN
* Address
* Current Supplier and Registration Effective From Date
* Meter Timeswitch Class and Effective From Date
* Line Loss Factor and Effective From Date
* Profile Class
* Standard Settlement Configuration
* Measurement Class
* Energisation Status
* Data Aggregator
* Data Collector
* Meter Operator and Effective From Date
* GSP Group and Effective From Date
* Distributor name and Dip Id
* Domestic Premises Indicator
* Meter Serial Number and Meter Installation Date
* Meter Type
* Meter Asset Provider

The industry is undergoing a transition to the DIP ([Data Integration Platform](https://www.elexon.co.uk/what-we-do/about-our-services/data-integration-platform-dip/)) and you can see
this beginning to be introduced into ECOES, with the `Distributor Dip Id` column showing
the new DIP id, rather than the old Market Participant Id. The other columns are still on
the old system though. The ISD ([Industry Standing Data](https://www.elexon.co.uk/bsc/data/industry-standing-data/)) replaces the old Market Domain Data, recasting its contents in DIP
form. The ISD contains a mapping between the old and new systems, which is helpful for
dealing with the two systems.

![Stack Of Papers](stack_of_papers.png)

As a programmer of the [Chellow](https://www.chellow.org/) system, I'm having to make sure
that we handle the transition as gracefully as possible. I've opted for a gradual morphing
of old to new, rather than a big bang approach. The full zipped ISD file comes to over 400
MB, although that does included the line loss factors.

Anyway, the ECOES data is incredibly useful for checking the information held in Chellow
against the industry information. Any discrepancies are flagged up for investigation. In a
similar way to bill checking, if there's a difference then either Chellow is wrong or the
industry is wrong or both!

Finally, in the ECOES CSV output, the following headings are present, but without any data. They are waiting for the transition to the DIP.

* Supplier Dip Id
* Duos Tariff Id
* Duos Tariff Id Effective From Date
* Market Segment Indicator
* Market Segment Indicator Effective From Date
* Data Service Dip Id
* Data Service Effective From Date
* Data Service Effective To Date
* Data Service Mpid
* Metering Service Dip Id
* Metering Service Effective From Date
* Metering Service Effective To Date
* Metering Service Mpid

See you next time! ✨
