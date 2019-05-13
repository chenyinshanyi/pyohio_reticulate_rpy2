# PyOhio 2019 Talk Proposal: Using Python & R in Harmony
_Krista Readout & Matthew Brower_

_May 2019_

### Brief Description:
Python and R are two of the most popular languages used for data analysis. They are often pitted against each other in pro con lists, forcing users to pick just one. Each has unique advantages, and it's now easier than ever to use them in the same project. Python or R? Why not both?

---
### Detailed Abstract & Outline:

**Abstract**

How often do you hear the question "Python or R?"

Aspiring analytics professionals often feel the need to choose & learn a 'one size fits all' language for their scripting work.  There are many cases, though, where a specific library in Python or R is more effective than similar libraries in the other language.  This can lead to some painful tradeoffs when selecting a single language for your work.  Great news: recent developments have made leveraging both languages in the same workflow easier than ever before.

In this talk, we’ll present methods for leveraging R from directly within Python environments (and vice versa).  We will illustrate the use of these methods by using popular libraries to execute common analytics tasks across languages (web scraping, predictive modeling, time series forecasting, anomaly detection) without switching development environments.

**Outline**

- Introductions & Context
  - Speaker bios
  - Motiviation for proposal / talk
- Using R from within Python with [`rpy2`](https://rpy2.readthedocs.io/en/version_2.8.x/index.html)
  - Environment setup & requirements
  - Use case demonstration (one of the following TBD)
    - Anomaly detection using Twitter's [`AnomalyDetection`](https://github.com/twitter/AnomalyDetection) package
      - There's no popular Python equivalent to this package (used at many e-commerce companies to detect sudden changes in KPIs).
    - Time series forecasting with Rob Hyndman's [`forecast`](http://pkg.robjhyndman.com/forecast/) package
      - `forecast` provides a great interface for many different kinds of time-series forecasts (ARIMA, TBATS, etc.); a one-stop shop that's lacking an analogous equivalent in Python.
    - Causal inference with Google's [`CausalImpact`](https://google.github.io/CausalImpact/CausalImpact.html) package
      - There's no easily-availble Python substitute to this package used for estimating the impact of an event / policy change without A/B testing.
- Using Python from Within R with [`reticulate`](https://rstudio.github.io/reticulate/)
  - Environment setup & requirements
  - Use case demonstration (one of the following TBD)
    - Web scraping with [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) or [`scrapy`](https://scrapy.org/)
      - R's web scraping options are somewhat limited & Python has mature, widely-used libraries available for use
    - Predictive modeling with [`scikit-learn`](https://scikit-learn.org/stable/)
      - R has many modeling libraries, but the interfaces are often inconsistent which results in fragmented code.  `scikit-learn` provides a unified interface to many different modeling techniques for faster, cleaner iteration on projects.
- Learning resources
- Q&A
