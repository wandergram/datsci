##Google Motion Chart##

Motion Chart is a great data visualization tool that can help you analyze your data in new and exciting ways. Watch [this TED talk by Hans Rosling](http://www.ted.com/talks/hans_rosling_shows_the_best_stats_you_ve_ever_seen?language=en#t-283227) to see it in action. Here's how to create your own.

**Instructions**:

**Collect data**: 

To get the best results, you'll want time series data for a relatively long list of entities (countries, states, cities, companies, etc). 

*If you only have data for one year or one point in time, you can still use Motion Chart for a cool visualization - more on this below.*

In the example datasets provided above (pop_gnp.xls, life_ruralpop.xls), I use global time series data for:

* life expectancy and rural population as percentage of total between 1946 and 2006, and
* raw population figures and raw GNP figures between 1963 and 1993. 

*Data collected for American University, Fall 2008.*

For the static data example (state failure and nuclear safeguards), see the end of this document.

Good data sources for similar stats include [Data.UN.org](http://data.un.org) & [Data.WorldBank.org](http://data.worldbank.org)

Collect your data in a spreadsheet application such as Excel.

**Set up data**:

* Motion Chart requires a spreadsheet with at least four columns (but no more than six). 
* The first MUST be titled “entity”, otherwise Motion Chart can get whiny. 
* The second column MUST be titled “time” – this is the year for each observation. The third and fourth columns will contain the numeric values for your variables.  
* If you'd like, you can add a fifth column to categorize your data for better visualization – for example, add regions of the world as a fifth column to color-code countries by region later on, or add something like "Red State/Blue State" to states, etc.

**Clean data**: 

* Your data cannot have #NULL! values in any of the cells. You should replace the #NULL! values with a blank; if they're replaced with a dot or a dash, Motion Chart won't work, and if they’re replaced with zeros, the dynamics of the data will be skewed. 

* All columns have to be formatted in the "General" format in Excel, otherwise Google Sheets will tell you it can't read the data for Motion Chart.

**Upload data**:

* Upload your Excel file to Google Docs, then select "Open with Google Sheets". You'll need to work in Sheets.

* Try to keep the file size under 1MB.

**Adding Motion Chart**:

* Select all columns.
* Go to Insert -> Chart. The Motion Chart option should be the first one you see under "Recommended charts". Click on Insert. 
* If you don't see Motion Chart as your first option, Sheets probably doesn't like your data format. Click on the Charts tab, then Trends, the third one down should be Motion Chart. See if it'll let you add it from there.
* You can move it to its own sheet through the little dropdown menu in the top right corner of the chart.
* Click the Play button to watch!

**Options for playing with Motion Chart**:

* Set color and size properties by variable.
* Select particular entities.
* If "trails" is selected, you can click on one circle and track its movement relative to the rest.

**Examples**:

GNP & population, 1986 (the giant red circle is America. Hells yeah.):

![GNP & population, 1986](http://s15.postimg.org/66j2lu1x7/gnp_pop86.png "GNP & Population, 1986")

Life expectancy & rural population, 1986, with Indonesia selected:

![Life expectancy & rural population, 1986](http://s24.postimg.org/tbgsl2ps5/life_ruralpop86.png "Life expectancy & rural population, 1986")

**Motion Chart for Static Data**

If you only have static data for one year or one time period, you can still use Motion Chart. Perform all the same steps as above. You won't have a play button, but you can set colors and sizes for a neat visualization.

In the *static_data.xls* example provided above, I used a dataset I created for my thesis, capturing nuclear safeguards enacted by a country and its score on the Failed States Index (FSI). The higher the FSI score, the less stable a country is; the higher the nuclear safeguards score, the more safeguards against illicit proliferation have been enacted. 

*FSI 2009 data from [The Fund for Peace](http://fundforpeace.org), nuclear safeguards scores indexed from UN Security Council Resolution 1540 reporting mechanisms.*

Even without time series movement, changing the size of the circles so that the more agreements a country had signed, the larger its circle would be, and changing the color of the data points so that the country’s position on the Failed States Index would correspond to a color (red – most fragile, orange – highly unstable and so forth) still worked -  it allowed me to demonstrate that the countries with the smallest circles (that is, the fewest nuclear agreements, treaties and initiatives) were all red, or very weak states. This showed that weak and fragile states are empirically proven to be less likely to cooperate with nuclear nonproliferation regimes, which is in and of itself an important piece of information and a good starting point for further research. 

Here's what it looks like:

![FSI scores & nuclear safeguards](http://s13.postimg.org/41i4jkxo7/nukes_fsi09.png "FSI scores & nuclear safeguards")
