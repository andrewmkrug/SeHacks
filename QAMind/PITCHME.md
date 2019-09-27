

# Selenium Hacks

## Andrew Krug Medina

+++

# Who I am

* Been in Quality Engineering for Entire Career |
    * For Better or Worst |
* Cool things with Automation |
    * Dumb things with Automation |
* Continuously Learns Geeky Stuff |
* Run Diving into Selenium @ Selenium Conf |
* Committee member Selenium Conf |
* Solution Architect @ Sauce Labs|
* Blog @ LazyCoder.io |


---

# Inspired by Dave Haeffner
## Author of Selenium Guidebook

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
#
+++
### How do you fill out your toolbox?

+++?code=/assets/code/expected_outcome.py&title=Expected Outcome

@[5-8](Poorly Defined Test)
@[8](Everyone needs to learn one thing)

+++?code=/assets/code/person.py&title=How Will I Tell

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

# This will be fast

+++


# Very Fast

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
<h2 class="fragment"> "Undercovered" Topics ?</h2>

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
    - That component not purpose of test |

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

# Super Geeky

+++

@css[yellow](Warning)

+++

#### This is not a recommendation

+++

#### This is not maintainable

+++

#### Still geeky and I'm a nerd

+++

# lambdium
## headless chrome as a package

+++?image=/assets/image/Overloaded_robot.png&size=auto 80%&opacity=100


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
+++

# How About a Demo?

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

# Why Awesome = True

- Blacklisting |
- Bad Image Checking |
- Performance Testing |
    - Sort of |
- Load Testing |
    - Sort of |

+++

# How to use it

+++?code=/assets/code/browser_profile.java&title=How to Use BMP
@[24](Create the BMP Server)
@[27](Create the Proxy)
@[30](Add a cap for the Proxy and pass it in)
@[31](Get the browser running with it)
@[38](Start recording to HAR)
@[50-52](Save the HAR file)

+++

# Blacklisting

- List of URLs to block |
- Setup BMP to return 404 for matching resources |
- Useful to prevent loading of known slow resources |
    - Facebook |

+++

# Whitelist
- Pass in a pattern of matching URLS and everything else is blacklisted |

+++

# Whitelist

```java
List<String> allowUrlPatterns = new ArrayList<String>();
allowUrlPatterns.add("https?://.*(yourdomain.name)+.*");

proxyServer.whitelistRequests(allowUrlPatterns, 404);

```
@[2](Any subdomain and path from yourdomain.name)
@[4](Whitelsit the array, everything else 404)
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
    - https://github.com/lazycoderio/PerformanceSeleniumTests |
+++

# Shameless Plug

+++

# On Sauce Labs..

+++

# Add these capabilities
+++

# TODO: Code for Sauce Performance Testing
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

+++?image=assets/image/shield_robot.png&size=auto 80%&opacity=100
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
# IF you have read the installation instructions
+++
# Hard and Confusing Instructions?


+++

# Andrew Whats the Lazy Way?
+++

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


# 'k
## insert unfortunate manual step

---?video=/assets/video/Tapster_Duet.mp4&opacity=100

# @css[white](Tapsterbot)
<h3 class="fragment"><span class="white">Technically Webdriver JSONs to communicate</span></h3>

---

# Wait now where is the Code?

---?image=/assets/image/question_robot.png&size=auto 80%&opacity=100


