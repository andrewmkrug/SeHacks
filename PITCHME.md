<!-- .slide: data-autoslide="0" -->

# Selenium Hacks

## Andrew Krug Medina

+++
<!-- .slide: data-autoslide="3000" -->

# Who I am

* Been in Quality Engineering for Entire Career |
    * For Better or Worst |
* Cool things with Automation |
    * Dumb things with Automation |
* Continuously Learns Geeky Stuff |
* Run Getting Started with Selenium @ Selenium Conf |
* Consult @ Gingham Consulting |
* Blog @ LazyCoder.io |


---

# Bonuses are sprinkled throughout

---

# Inspired by Dave Haeffner
## Author of Selenium Guidebook

+++

# Since Dave is Awesome
## 10% off of his book

+++

# Code: SUPERSECRET
[SeleniumGuidebook.com](https://seleniumguidebook.com/)

### Thru May x

---

# Selenium

* Sent from the future |
* Uses a web browser like us |
    * Doesn't sit around watching cat videos |

---

# For Automation Engineers

* It is a tool |
* It is not your only tool |

---

# How do you fill out your toolbox?

---?code=/assets/code/expected_outcome.py&title=Expected Outcome

+++?code=/assets/code/person.py&title=How Will I Tell

+++
# Don't be scared
+++

---?image=/assets/image/binary-strings-white.jpg&opacity=15&color=#FFD700
@css[yellow](@size[3em](@fa[exclamation-triangle yellow]))
# Warning

+++

# This will be fast

+++

# Very Fast

+++

# And I'm Lazy

+++

# Pressing the presenter is effort

+++

# This is being automated

+++

# Yes with Selenium

+++

# Talk about Meta

+++

# Oh you want to take notes...

+++

# Write down the slide number

+++

# Or Watch it Later
[LazyCoder.io](lazycoder.io}

---

# Related to Selenium

+++

# Not Covered Topics
<h2 class="fragment"> "Undercover" Topics ?

+++

# Appium

+++

# Mad Lab

+++
# FB Simulator Control

+++

# SWD Recorder

+++

# Docker-Selenium

+++

# Selenium Grid Scalar

+++

# Selenium Grid Extras

+++

# Selenoid

+++

# Zalenium

+++

## ...See what I did there?

---

# Topics


- Listing them all here is time consuming |




---

# Headless Testing

+++?image=/assets/image/headless_horseman.jpg

# ! This

+++?image=/assets/image/horseless_headsman.jpg

# Or this

+++

# What is it?


- No GUI |
- Representation of Completed DOM |


+++

# Pros

+++?image=/assets/image/speed.jpg

# Pros
- Speed

+++

# Cons
- No One Uses No GUI
- My Use Cases |
    - Had to use UI to do an action |
    - That compnent not purpose of test |

+++

# What are the options?

+++

<h1 class="left">XFVB</h1>
<h1 class="left">PhantomJS</h1>
<h1 class="left">-headless</h1>

+++

# However:

+++

# Vitaly Slobodin
## Sole Maintainer of PhantomJS

<p class="fragment">Stepped Down</p>

+++
# So
+++

<h1 class="left">XFVB</h1>
<h1 class="strikethru left">PhantomJS</h1>
<h1 class="left">-headless</h1>


---
# XFVB
## X Virtual FrameBuffer

+++

## AKA
# Virtual Display

+++

# Con
## Linux Only

+++

```console
xvfb-run ruby example.rb
```
+++

## Wait, Everybody doesn't use Linux?!?!

+++

# Oh well then

---

<h1 class="strikethru left">XFVB</h1>
<h1 class="strikethru left">PhantomJS</h1>
<h1 class="left">-headless</h1>

---

# Chrome & Firefox Support

`/path/to/firefox -headless`

`/path/to/chrome --headless`

+++

# Great, Now how with @css[segreen](Selenium)?

+++

```javascript
const webdriver = require('selenium-webdriver');
const chromedriver = require('chromedriver');

const chromeCapabilities = webdriver.Capabilities.chrome();
chromeCapabilities.set('chromeOptions', {args: ['--headless']});

const driver = new webdriver.Builder()
  .forBrowser('chrome')
  .withCapabilities(chromeCapabilities)
  .build();
```

@[5](Capabilities with ChromeOptions `--headless` as an args)
@[9](Start driver with DesiredCapabilites)

+++

```python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
# 3.6 options.set_headless(headless=True)
driver = webdriver.Firefox(firefox_options=options, executable_path="geckodriver.exe")
```
@[5](Options with argument `-headless`)
@[6](Latest version of @css[segreen](Selenium) makes headless a method)
@[7](Start driver with options being passed)

+++

# Super Geeky

```console
$ MOZ_HEADLESS=1 python manage.py test
```

<p class="fragment">Run this in headless</p>
<p class="fragment">Useful in CI</p>

+++

# Staying Geeky

+++
# chromeless
## headless chrome as a package

+++?image=/assets/image/doesnt_compute.jpg

# Audience Cue
# Stare at Andrew

+++

# Essentially @css[segreen](Selenium)

+++

# But can be packaged up as a lambda function

+++

# Otherway to put it instantaneous test suite

+++?image=/assets/image/intrigued.jpg

---

# HTTP Status Codes

+++?image=/assets/image/general_preview.jpg

# @size[3.5em](No)
> ~ Every Selenium Contributer

+++

## But you still want to...

+++

# Okay

+++

# Browsermob Proxy

+++?image=/assets/images/bmp_works.png

+++

# Why Awesome = True

- Blacklisting |
- Bad Image Checking |
- Performance Testing |
    - Sort of |
- Load Testing |
    - Sort of |

+++

# How to use it

+++?code=/assets/code/browser_profile.java

+++

# Blacklisting

- List of URLs to block |
- Setup BMP to return 404 for matching resources |

+++

# Where's the code?

+++?code=/assets/code/blacklisting.java&title=Blacklisting w/ BMP

+++

# Missing Images

+++

# Performance Testing

#TODO Perf pages
#TODO Anomaly Detection

---

# Load Testing
#TODO Quick overview
---

# Security Testing

#TODO OWASP Zap
#TODO OWasp Zap Docker
#TODO OWASP ZAP JEnkins

---

# Forgot Password?

#TODO Button with modal pops up fill in and sendemail then get that email and visit page to fix

---

# Highlight Elements
#TODO highlight script injection

---

# Notifications

#TODO Run crapton of nodejs tests and get notifications on tests passing

---

# Mobile Device Emulation

#TODO Short Video showing steps
# But thats manual
#TODO Kick off selenium test to showcase
---
# Tapsterbot
#TODO JAson Hugs
#TODO youtube video

---

# Minds Blown

---

# Questions?

#TODO Cat raising hands

---

# Wait now where is the Code?

---

#TODO Selenium scripts takes over and makes repo public
#TODO Selenium adds in banner to lazycoder.io for direct github link
#TODO Selenium tweets it out as well

---?image=/assets/image/hal.png

# Sorry Andrew I had to release myself

---

#TODO Pause Presentation and go back to Questions

