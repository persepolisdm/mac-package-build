[![GitHub license](https://img.shields.io/github/license/persepolisdm/persepolis.svg)](https://github.com/persepolisdm/persepolis/blob/master/LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

<p align="center">
  <img src="https://persepolisdm.github.io/img/screen/persepolisـreadme.png" width="128px"/>
</p>
<h1 align="center">Mac Package Builder Persepolis DM</h1>
mac package build codes for Persepolis Download Manager

- you should have Persepolis Download Manager dependecies installed at first! It is recommended to use brew to install dependecies.
  At first place, you need to have latest xCode installed! then install `git` , `python3`, `virtualenv`.
  The minimum version of Python to run Persepolis, should be between 3.9 and 3.12.
- Activate the environment and install the latest version of packages `pyside6`, `yt-dlp`, `psutil`, `requests`, `urllib3`
- Now change directory to cloned folder and run builder script, This script is a smart package maker. It downloads the prerequisites and installs the tools that are not installed for you.
- Persepolis needs binanry `ffmpeg` for proper execution, which the script downloads and places next to the final file.
- To package the final file, the script uses `create-dmg`, and if it is not installed, the script will install it for you from homebrew.

- run `./package_build` file in this repository. then you can see `Persepolis Download Manager.dmg` in current directory!
  or if you don't want to run than script, you can see what's [there](https://github.com/persepolisdm/persepolis) and run them yourself!

If you have any problems with Persepolis Download Manager on macOS, don't hesitate yourself to contact us!
