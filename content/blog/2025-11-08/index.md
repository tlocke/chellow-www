+++
title = "Forecasting NBP kWh"
date = 2025-11-08T00:00:00Z
template = "blog_post.html"
+++

We've had a run of NBP kWh related posts (
[Calculating NBP](/blog/2025-10-25/) and
[NBP Reconciliations](/blog/2025-11-15/), and this post rounds off the series by talking
about forecasting NBP kWh.

Even though actual TLMs are specific to the GSP Group and the particular half-hour,
estimated TLMs (ETLMs) apply to all GSP Groups and cover whole months and sometimes
multiple months. You can see the ETLMs on an
[Elexon webpage](https://www.elexon.co.uk/bsc/operational/transmission-losses/estimated-transmission-loss-adjustments/), here's a screenshot: 

![ETLMs Elexon](screenshot_etlm_elexon.png)

Further down on that page is a link to a CSV download of the ETLMs.

As an aside, it's really frustrating that this link can't easily be automatically
downloaded using a script, because it requires cookies, JavaScript etc and various
protections to prevent automated access. Elexon do have a 'scriptable downloads' section
on their portal, and I've written to them asking if they'd put the ETLMs there. In the
meantime we download the file to the
[rate repository](https://github.com/WessexWater/chellow-rates/tree/main/2025/electricity/etlms). Feel free to make use of this repository, it contains all the industry data that has
to be manually downloaded, and can be accessed using the
[GitHub API](https://docs.github.com/en/rest).

![Transmission Lines](transmission_lines.jpeg)

Okay, back to ETLMs. When [Chellow](https://www.chellow.org/) sees that a new ETLM file has
been added to the rate repository, it downloads it and stores the ETLMs in its database.
ETLMs are useful for two things, firstly they are used for forecasting, because as you can
see they go out to the end of this financial year. We can run the virtual bills in Chellow
for a time in the future and it will calculate the expected costs using the ETLMs and other
rates that apply at that future time.

Secondly, ETLMs are useful as a basis for the (initial, before reconciliations) bill from
the supplier. The first settlement run (with the code 'II') is 1 week after the time in
question, and so suppliers might not be able to use this for all half-hours. What they can
do instead is use the ETLMs, and then reconcile as updated actuals come in. The key thing
is that the supplier should use a standard version for TLMs (either ETLMs, or one of the
settlement runs). Otherwise, without knowing the TLM version we can't check that the bills
are correct.

See you next time! ✨
