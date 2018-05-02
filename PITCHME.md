<!-- .slide: data-autoslide="0" -->

# Selenium Hacks

## Andrew Krug Medina

+++
<!-- .slide: data-autoslide="1500" -->

# Who I am

* Been in Quality Engineering for Entire Career |
    * For Better or Worst |
* Cool things with Automation |
    * Dumb things with Automation |
* Continuously Learns Geeky Stuff |
* Run Diving into Selenium @ Selenium Conf |
* Committee member Selenium Conf |
* Consult @ Gingham Consulting |
* Blog @ LazyCoder.io |


---

# Inspired by Dave Haeffner
## Author of Selenium Guidebook

+++

# Since Dave is Awesome
## 10% off of his book

---

# Selenium

* Sent from the future |
* Uses a web browser like us |
    * Doesn't sit around watching cat videos |

---

# For Automation Engineers

* It is a tool |
* Not your only tool |

---

# How do you fill out your toolbox?

+++?code=/assets/code/expected_outcome.py&title=Expected Outcome
@[5-8](Poorly Defined Test)
@[8](Everyone needs to learn one thing)

+++?code=/assets/code/person.py&title=How Will I Tell
@[2-4](Minimal Def of a Person)
@[7](If the slide has something you don't know)
@[10](Then raise your hand)
@[13](Not writing pseudo code for raising hand)

+++?video=/assets/video/dont_be_scared.mp4
# Don't be scared

+++

---?image=/assets/image/binary-strings-white.jpg&opacity=15&color=#FFD700

@css[spin](@css[yellow](@size[3em](@fa[exclamation-triangle yellow])))
#TODO spin

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

# Talk about Meta

+++

# Oh you want to take notes...

+++

# Write down the slide number

+++

# Or Watch it Later
##[LazyCoder.io](lazycoder.io)

---

# Content is Related to Selenium

+++

# Not Covered Topics
<h2 class="fragment"> "Undercover" Topics ?

+++

# Appium
- Selenium for Mobile Devices |
+++

# Mad Lab
- Device management (selection, cleanup, app install and uninstall) |
- Parallel test execution (at Cucumber scenario level) |
- Managing periodic ADB server disconnects |
- Video recording of each scenario and embedding in the custom reports |
- https://github.com/GoogleChromeLabs/MiniMobileDeviceLab |
+++
# FB Simulator Control
- Run multiple iOS Simulators per Mac |
- Bypass that 1 simulator constraint |
- https://github.com/facebook/FBSimulatorControl |
+++

# SWD Recorder
- Record Page Objects for your test suite |
- https://github.com/dzharii/swd-recorder |
+++

# Selenium Grid Extras
- Web Interface for Grid Hub and Nodes |
- Endpoints for actions: |
    - Restart Node |
    - Terminate browser sessions |
- https://github.com/groupon/Selenium-Grid-Extras |
+++

# Docker-Selenium

- Containers for Grid Nodes |
+++

# Selenium Grid Scalar
- Uses Amazon Elastic Containers for Auto-Scaling Grid |
- Docker-Selenium Plus |


+++

# Selenoid
- Low overhead wrapper over dockerized selenium hub and nodes|
- https://github.com/aerokube/selenoid |
+++

# Zalenium

- Docker-Selenium with fallback to Grid Providers |
- If Platform/OS/Browser not found in containers |
    - Check local grid |
    - Spin up Session on: |
        - Sauce Labs |
        - Browserstack |
- https://github.com/zalando/zalenium |
---

## ...See what I did there?

---

# Topics

- Listing them all here is time consuming |


---

# & Bonuses are sprinkled throughout

+++

# Why
+++

# Because Sprinkles are for winners

+++

# Your are all Winners
---

# Headless Testing

+++?image=/assets/image/headless_horseman.jpg

# ! This

+++?image=https://media.giphy.com/media/xX0jkVS8ZuTdu/giphy.gif

# Or this

+++

# What is it?


- No GUI |
- Representation of Completed DOM |


+++

# Pros

+++?image=/assets/image/speed.png

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
# XVFB
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
```console
xvfb-run mvn test
```
+++
```console
xvfb-run your-test-cmds
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

# Missing Images
![](/assets/image/nothere.jpg)
+++
# HTTP Library
- Capture HAR log |
- Use library to make request to each source |
- Validate Response Code 200 |
- Can also validate size/type |
---
# Performance Testing
+++
# Sort Of
- Validate Page Load Times are Under SLA |
- Find Slow Loading Resources |
- Bonus |
    - Send Metrics to Dashboard |
- Bonus |
    - Use Machine Learning to Find Anomalies |
    - Yup I did that! |

---

# Load Testing
+++
# Sort Of
- Convert HAR to JMX |
    - Flood.io/har2jmx |
- Taurus |
    - gettaurus.org |
---

# Security Testing
+++
# Seriously?!?!
+++
### Even Equifax could have done this
+++
# How does this work?
+++
# OWASP Zed Attack Proxy
- Run Selenium Test while running recorder |
- Replays using different attacking methods |
+++
# Run it all the time
## Its a Jenkins Plugin!
+++
https://wiki.jenkins.io/display/JENKINS/zap+plugin
+++
# Dude thats hard

+++
# 'k
+++
# Docker FTW
<span class="fragment">https://github.com/zaproxy/zaproxy/wiki/Docker</span>


---
<div id="forgotPassword"></div>
# Forgot Password?

+++?code=assets/code/mailosaur_sample.py&title=Mailosaur Example// TODO Button with modal pops up fill in and sendemail then get that email and visit page to fix
@[1](Connect to your mailbox)
@[3-4](Get all your emails)
@[6-7](The first email should have this title)
---

# Highlight Elements

```javascript
Highlighting

“arguments[0].setAttribute(arguments[1],
arguments[2])”, element, “style”,
“border: 2px solid red;”

“arguments[0].setAttribute(arguments[1],
arguments[2])”, element, “style”,
original_style
```

+++
# Wait do you want to see it?

<div id="highlight"></div>


---

# Mobile Device Emulation

// TODO Short Video showing steps
---
# But thats manual
---
### Awesomeness ahead
// TODO Kick off selenium test to showcase
---
# Tapsterbot
// TODO Jason Hugs
// TODO youtube video as Webm

---?image=assets/image/mind_blown.png&opacity=100

# Minds Blown
---
# Code: SUPERSECRET
[SeleniumGuidebook.com](https://seleniumguidebook.com/)

### Thru May xz
---

# Do you want more of this?

+++

# Preorder MY Book
## seleniumaboveandbeyond.com
### lazycoder.io/book

---
# Questions?

// TODO Cat raising hands

---

# Wait now where is the Code?

---

// TODO Selenium scripts takes over and makes repo public
// TODO Selenium adds in banner to lazycoder.io for direct github link
// TODO Selenium tweets it out as well

---?image=/assets/image/hal.png

# Sorry Andrew I had to release myself

---

// TODO Pause Presentation and go back to Questions

