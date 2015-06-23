##Tower of Babble? 
### Predicting (in)action by the UN Security Council

Critics of the United Nations routinely claim that the UN does nothing in times of crisis - in fact, “does the UN… do anything” is among the top predictive search suggestions offered by Google. As the UN’s primary decisionmaking body, the Security Council has borne the brunt of this criticism. Security Council resolutions “demanding an immediate end to hostilities” but resulting in little concrete action have generated biting satire, and many have come to expect that the Security Council will ultimately fail to act when action is most needed. 

###Project Question###

Based on the text of Security Council provisional meeting records (inputs) and resolutions (outcomes) passed over the last two decades, this project seeks to predict what kind of action the Security Council will take on an issue pertaining to peace and security that is brought before it.

Possible outcomes can best be described along a continuum or scale, with outcomes on the "positive" side including “soft” measures (deployment of observation missions), “prohibitive” measures (naval blockades, embargoes, sanctions against offending regimes), and “hard” measures (missions authorized to use force to protect civilians in conflict, so-called “Chapter VII missions”). On the "negative" side, the corresponding outcomes would be the reversal of prior actions taken, such as the withdrawal of peacekeepers or the non-renewal of sanctions. At the zero (0) mark would be the outcome of "no action". 

* Note: The terms "positive" and "negative" to describe outcomes are not meant to be subjective qualitative or moral judgments regarding the propriety of the action(s) taken. **These terms are only used to illustrate where such outcomes would fall along an imaginary continuum for data coding purposes.** This is an important distinction: for instance, in some cases, "negative" outcomes such as the end of a peacekeeping mission can mean that positive developments have occurred in a country (that it has achieved stability, that power has been transfered peacefully, etc). In other cases, "positive" outcomes such as the enactment of certain "soft measures" could be seen as being insufficient (too weak, apathetic) in the face of a potentially massive crisis and could thus be viewed negatively by some observers. This project will not concern itself with determining whether a certain UN action is generally "good" or generally "bad" for humanity writ large.

* Note 2: Issues such as the admission of new members and the appointment of officials to international tribunals, which also fall under the purview of the Security Council, will be left out of this analysis, as they have no immediate bearing on matters of peace and security.

###Why I chose this question###

I work primarily with or in countries affected by some form of instability, most of which have a measurable UN presence. Where populations depend on UN action to ameliorate their condition, observers often try to analyze the text of UN records to determine how/whether the approach of the UN will change in the near future. Attempts to predict UN actions also inform operational decisions made by businesses, NGOs, and other international institutions, such as whether to expand or contract projects; these operational decisions often have major financial implications. Currently, these predictions rest mostly on grapevine rumors. I would like to try to automate this analytical process.  

If successful, the model could also be applied to the analysis of other types of documents with real-world applications, such as legislative proceedings or government directives. This could assist in the development of more actionable and responsible representative bodies, as well as help businesses and organizations better plan for future operations.  

###Data###

* For inputs, I will use the texts of ~2,200 [provisional records of Security Council meetings](http://www.un.org/en/sc/meetings/index.shtml) held between January 1994 and June 2015. The timeframe of this project was limited by data availability: records of meetings held prior to January 1994 are not publicly available.  

* For outcomes, I will use the texts of ~1,300 [Security Council resolutions](http://www.un.org/en/sc/documents/resolutions/) passed during the same time period. 






