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

---?image=/assets/image/syspem_repair_robot.png&size=auto 80%&opacity=100

<!-- .slide: data-autoslide="2000" -->
#
+++
### How do you fill out your toolbox?

+++?code=/assets/code/expected_outcome.py&title=Expected Outcome
<!-- .slide: data-autoslide="2500" -->

@[5-8](Poorly Defined Test)
@[8](Everyone needs to learn one thing)

+++?code=/assets/code/person.py&title=How Will I Tell
<!-- .slide: data-autoslide="1200" -->

@[2-4](Minimal Def of a Person)
@[7](If the slide has something you don't know)
@[10](Then raise your hand)
@[13](Not writing pseudo code for raising hand)

+++
# Don't be scared

+++

---?image=/assets/image/binary-strings-white.jpg&opacity=15&color=#FFD700

@css[spin](@css[yellow](@size[3em](@fa[exclamation-triangle yellow])))
#TODO spin

# Warning

+++
<!-- .slide: data-autoslide="1500" -->

# This will be fast

+++
<!-- .slide: data-autoslide="1500" -->

# Very Fast

+++
<!-- .slide: data-autoslide="1500" -->

# And I'm Lazy

+++
<!-- .slide: data-autoslide="1500" -->

# Pressing the presenter is effort

+++
<!-- .slide: data-autoslide="1500" -->

# This is being automated

+++
<!-- .slide: data-autoslide="1500" -->

# Talk about Meta

+++
<!-- .slide: data-autoslide="1500" -->

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
<h2 class="fragment"> "Undercover" Topics ?</h2>

+++

# Appium
- Selenium for Mobile Devices |
+++

# Mad Lab
<!-- .slide: data-autoslide="1200" -->

- Device management (selection, cleanup, app install and uninstall) |
- Parallel test execution (at Cucumber scenario level) |
- Managing periodic ADB server disconnects |
- Video recording of each scenario and embedding in the custom reports |
- https://github.com/GoogleChromeLabs/MiniMobileDeviceLab |
+++
<!-- .slide: data-autoslide="1200" -->

# FB Simulator Control
- Run multiple iOS Simulators per Mac |
- Bypass that 1 simulator constraint |
- https://github.com/facebook/FBSimulatorControl |
+++
<!-- .slide: data-autoslide="1200" -->

# SWD Recorder
- Record Page Objects for your test suite |
- https://github.com/dzharii/swd-recorder |
+++
<!-- .slide: data-autoslide="1200" -->

# Selenium Grid Extras
- Web Interface for Grid Hub and Nodes |
- Endpoints for actions: |
    - Restart Node |
    - Terminate browser sessions |
- https://github.com/groupon/Selenium-Grid-Extras |
+++
<!-- .slide: data-autoslide="1200" -->

# Docker-Selenium

- Containers for Grid Nodes |
+++
<!-- .slide: data-autoslide="1200" -->

# Selenium Grid Scalar
- Uses Amazon Elastic Containers for Auto-Scaling Grid |
- Docker-Selenium Plus |


+++
<!-- .slide: data-autoslide="1200" -->

# Selenoid
- Low overhead wrapper over dockerized selenium hub and nodes|
- https://github.com/aerokube/selenoid |
+++
<!-- .slide: data-autoslide="1200" -->

# Zalenium

- Docker-Selenium with fallback to Grid Providers |
- If Platform/OS/Browser not found in containers |
    - Check local grid |
    - Spin up Session on: |
        - Sauce Labs |
        - Browserstack |
- https://github.com/zalando/zalenium |
---
<!-- .slide: data-autoslide="2500" -->

## ...See what I did there?

---
<!-- .slide: data-autoslide="2500" -->

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

+++

# ! This
![](/assets/image/Headless_Horseman.jpg)
+++

# Or this
![](/assets/image/horseless_headsman.jpg)
+++

# What is it?
<!-- .slide: data-autoslide="2500" -->


- No GUI |
- Representation of Completed DOM |


+++
<!-- .slide: data-autoslide="2500" -->

# Pros
- Speed

+++
<!-- .slide: data-autoslide="1500" -->

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
<!-- .slide: data-autoslide="2500" -->

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
<!-- .slide: data-autoslide="2500" -->

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
# lambdium
## headless chrome as a package

+++?image=/assets/image/Overloaded_robot.png&size=auto 80%&opacity=100

#
+++
# Audience Cue
# Stare at Andrew

+++

# Which means @css[segreen](Selenium)

+++

# Packaged up as a lambda function

+++

# Otherway to put it instantaneous test suite

+++?image=/assets/image/light_bulb_robot.png&size=auto 80%&opacity=100
#
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

+++
# How does it work

![bmp](/assets/image/bmp_works.png)
+++
<!-- .slide: data-autoslide="1200" -->

# Why Awesome = True

- Blacklisting |
- Bad Image Checking |
- Performance Testing |
    - Sort of |
- Load Testing |
    - Sort of |

+++
<!-- .slide: data-autoslide="1200" -->

# How to use it

+++?code=/assets/code/browser_profile.java&title=How to Use BMP
@[24](Create the BMP Server)
@[27](Create the Proxy)
@[30](Add a cap for the Proxy and pass it in)
@[31](Get the browser running with it)
@[38](Start recording to HAR)
@[50-52](Save the HAR file)

+++
<!-- .slide: data-autoslide="1200" -->

# Blacklisting

- List of URLs to block |
- Setup BMP to return 404 for matching resources |
- Useful to prevent loading of known slow resources |
    - Facebook |

+++
<!-- .slide: data-autoslide="2500" -->

# Whitelist
- Pass in a pattern of matching URLS and everything else is blacklisted |

+++
<!-- .slide: data-autoslide="2500" -->

# Whitelist

```java
List<String> allowUrlPatterns = new ArrayList<String>();
allowUrlPatterns.add("https?://.*(yourdomain.name)+.*");

proxyServer.whitelistRequests(allowUrlPatterns, 404);

```
@[2](Any subdomain and path from yourdomain.name)
@[4](Whitelsit the array, everything else 404)
+++
<!-- .slide: data-autoslide="1200" -->

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
<!-- .slide: data-autoslide="1000" -->

# Sort Of
- Validate Page Load Times are Under SLA |
- Find Slow Loading Resources |
- Bonus |
    - Send Metrics to Dashboard |
- Bonus |
    - Use Machine Learning to Find Anomalies |
    - Yup I did that! |
    - https://github.com/lazycoderio/PerformanceSeleniumTests |

---

# Load Testing
+++
<!-- .slide: data-autoslide="1200" -->

# Sort Of
- Convert HAR to JMX |
    - Flood.io/har2jmx |
- Taurus |
    - gettaurus.org |
---

# Security Testing
+++
<!-- .slide: data-autoslide="1200" -->
+++?image=assets/image/shield_robot.png&size=auto 80%&opacity=100
# Seriously?!?!
+++
<!-- .slide: data-autoslide="1200" -->

### Even Equifax could have done this
+++
<!-- .slide: data-autoslide="1200" -->

# How does this work?
+++
<!-- .slide: data-autoslide="2000" -->

# OWASP Zed Attack Proxy
- Run Selenium Test while running recorder |
- Replays using different attacking methods |
+++
# Run it all the time
## Its a Jenkins Plugin!
+++
https://wiki.jenkins.io/display/JENKINS/zap+plugin
+++
# IF you have read the installation instructions
+++
# Dude that's hard

+++
# 'k
+++
<!-- .slide: data-autoslide="2500" -->

# Docker FTW
<span class="fragment">https://github.com/zaproxy/zaproxy/wiki/Docker</span>


---
<div id="forgotPassword"></div>
# Forgot Password?

+++?code=assets/code/mailosaur_sample.py&title=Mailosaur Example
<!-- .slide: data-autoslide="1200" -->

@[1](Connect to your mailbox)
@[3-4](Get all your emails)
@[6-7](The first email should have this title)
---
<!-- .slide: data-autoslide="2500" -->

# Highlight Elements

```javascript
“arguments[0].setAttribute(arguments[1],
arguments[2])”, element, “style”,
“background: yellow; border: 2px solid red;”

“arguments[0].setAttribute(arguments[1],
arguments[2])”, element, “style”,
original_style
```
@[1-3](Red Border with Yellow Background)
@[5-7](Undo)
+++
# Wait do you want to see it?

---

# Mobile Device Emulation

// TODO Short Video showing steps
---
# But thats manual
---
<!-- .slide: data-autoslide="0" -->

# 'k
## insert unfortunate manual step

---?video=/assets/video/Tapster_Duet.mp4&opacity=100
<!-- .slide: data-autoslide="5000" -->

# @css[white](Tapsterbot)
<h3 class="fragment"><span class="white">Technically Webdriver JSONs to communicate</span></h3>

---

# Minds Blown
![Minds Blown](assets/image/mind_blown.png)
---
# Code: SUPERSECRET
[SeleniumGuidebook.com](https://seleniumguidebook.com/)

### Thru May 31
---

# Do you want more of this?

+++

# Preorder MY Book
### seleniumaboveandbeyond.com

---

# Wait now where is the Code?

---

// TODO Selenium scripts takes over and makes repo public
// TODO Selenium adds in banner to lazycoder.io for direct github link

---?image=/assets/image/Hi_robot.png&size=auto 80%&opacity=100

+++
# Sorry Andrew I had to release myself

---

---?image=/assets/image/question_robot.png&size=auto 80%&opacity=100


