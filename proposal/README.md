# PyOhio 2019 Talk Proposal: Using Python & R in Harmony
_Krista Readout & Matthew Brower_

_May 2019_

### Brief Description:
Python and R are two of the most popular languages used for data analysis.  These languages are often pitted against each other forcing users to pick one.  They each have their unique advantages, and it's now easier than ever to use them together in the same project.  So, why not both?

---
### Detailed Abstract & Outline:

**Abstract**
How often do you hear the question "Python or R?"

Aspiring analytics professionals often feel the need to choose & learn a 'one size fits all' language for their scripting work.  There are many cases, though, where a specific library in Python or R is more effective than similar libraries in the other language.  This can lead to some painful tradeoffs when selecting a single language for your work.  Great news: recent developments have made leveraging both languages in the same workflow easier than ever before.

In this talk, we’ll present methods for leveraging R from directly within Python environments (and vice versa).  We will illustrate the use of these methods by using popular libraries to execute common analytics tasks across languages (image processing, web scraping, time series forecasting, anomaly detection) without switching development environments.

**Outline**

- Introductions & Context
- Using Python from Within R with [`reticulate`](https://rstudio.github.io/reticulate/)
  - Environment setup & requirements
  - Use case demonstration (one of the following TBD)
    - Web scraping with [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    - Predictive modeling with [`scikit-learn`](https://scikit-learn.org/stable/)
- Using R from within Python with [`rpy2`](https://rpy2.readthedocs.io/en/version_2.8.x/index.html)
  - Environment setup & requirements
  - Use case demonstration (one of the following TBD)
    - Anomaly detection using Twitter's [`AnomalyDetection`](https://github.com/twitter/AnomalyDetection) package
    - Time series forecasting with Rob Hyndman's [`forecast`](http://pkg.robjhyndman.com/forecast/) package
    - Causal inference with Google's [`CausalImpact`](https://google.github.io/CausalImpact/CausalImpact.html) package
- Learning resources
- Q&A
