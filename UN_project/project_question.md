##Tower of Babble? 
### Predicting (in)action by the UN Security Council by parsing “UNish”

It has been hypothesized that the UN, led by the Security Council, does nothing. In fact, “does the UN… do anything” is among the top predictive search suggestions offered by Google. Every year, hundreds of articles are published decrying ineffectiveness, bottlenecking, apathy, and political plays on the part of the UN, all of which appear to result in a damning lack of regard for populations affected by crises. 

As the UN’s primary decisionmaking body, the Security Council has borne the brunt of this criticism. Security Council resolutions “demanding an immediate end to hostilities” but resulting in little concrete action have generated biting satire. Some of the Council’s decisions, such as drawing down peacekeepers amidst a genocide, have surprised even the most forgiving of UN sympathizers.

**Project Question**

Based on the text of Security Council provisional meeting records (inputs) and resolutions (outcomes) passed over the last two decades, this project seeks to predict what kind of action the Security Council will take on an issue pertaining to peace and security that is brought before it. Possible outcomes include “soft” measures (deployment of observation missions), “prohibitive” measures (naval blockades, embargoes, sanctions against offending regimes), “hard” measures (missions authorized to use force to protect civilians in conflict, so-called “Chapter VII missions”), or no action.

Note: Issues such as the admission of new members and the appointment of officials to international tribunals, which also fall under the purview of the Security Council, will be left out of this analysis.

**Why I chose this question**

I work primarily with or in countries affected by some form of instability, most of which have a measurable UN presence. In many cases, the approach of the UN to crises in these countries has been roundly criticized. Where populations depend on UN action to ameliorate the situation, observers often try to analyze the text of UN records to determine what/whether anything will change in the near future. I would like to try to automate this analytical process. 

If successful, the model could also be applied to the analysis of other types of documents with real-world applications, such as legislative proceedings, to assist in the development of more actionable and responsible representative bodies. 

**Data**

* For inputs, I will use the texts of ~1,700 [provisional records of Security Council meetings](http://www.un.org/en/sc/meetings/index.shtml) held between January 1994 and June 2015. The timeframe of this project was limited by data availability: records of meetings held prior to January 1994 are not publicly available.  

* For outcomes, I will use the texts of 1,331 [Security Council resolutions](http://www.un.org/en/sc/documents/resolutions/) passed during the same time period. 






