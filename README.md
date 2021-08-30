<h1 align="center">
  <br>
  <a href="https://gitlab.com/zagyarakushi/chs"><img src="https://gitlab.com/zagyarakushi/chs/-/raw/master/img/lock.png" alt="CHS"></a>
</h1>

<h4 align="center">Cheap Home Security using any devices and some scripts</h4>

Note: This project was originally pushed to Gitlab and as such, all issues, pull/merge requests and any other disucussion or changes should be made [here](https://gitlab.com/zagyarakushi/chs). (In case you are wondering, I have this mirrored on Github so people can follow the project even if they prefer Github. Also it acts as a backup.)

[![License](https://img.shields.io/badge/License-MIT-lightgray.svg?style=flat-square)]()


# Table of contents
-----------------

* [Introduction](#introduction)
* [Installation](#installation)
* [Usage](#usage)
* [Known issues and limitations](#known-issues-and-limitations)
* [Getting help](#getting-help)
* [Contributing](#contributing)
* [License](#license)


# ⚡ Introduction
------------

This is a project to use smartphones, tablets, IP cameras, computers, raspberry pis and any other thing that has a camera and allows you to stream the feed as a security camera with motion detection. Once a motion is detected, an email will be sent with the image and video.

This project will use FOSS as much as possible.

![screenshot](https://gitlab.com/zagyarakushi/chs)


# 📖 Installation
------------

## Server setup

You will need python for the scripts which is installed by default on almost all Linux distributions. Then you need to install Motion.

#### Install Motion on Debian, Ubuntu or Raspbian
```bash
apt install motion
```

#### Void Linux
```bash
xbps-install -S motion
```

#### Clone the repository
```bash
git clone https://gitlab.com/zagyarakushi/chs
```

## Client/Camera Setup

Clients can be anything as mention in [Introduction](#introduction). As an example, andoird phone will be used as a camera in this guide. However, Motion accept any RTSP stream so any other devices that allows RTSP stream should work. In this case, all you need is to install Spynet Camera from F-droid.


# 📝 Usage
-----

## Server

Configure script and  Motion (Will be explained in the future) and run it. This will start the monitoring process and once a motion is detected, it will save an image in specified directory. By running the script in this same directory, the script will automatically detect new image and email it to specified email addresses.

## Client

Run Spynet Cam and check settings to suit your use case. Make sure that RTSP stream is enabled.


# ⭐ Known issues and limitations
----------------------------

* 24/7 recording on a NAS with automatic deletion of video after storage starts getting filled up.
* Maybe automatic setup and configuration with a nice program.
* Step by step configuration guide.


# ✌️ Getting help
------------

You can create an issue and I will try to help you as much as I can.


# 🔔 Contributing
------------

First read the code of conduct and contributing file. Then you can fork the repository, add your own stuff and create a pull/merge request.


# ⚠ License
-------

MIT


# 🤓 Acknowledgements
--------

Project icon is made by Freepik (https://www.flaticon.com/free-icon/lock_5336529)
