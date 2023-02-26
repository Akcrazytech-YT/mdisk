### Mdisk Direct Link Bot

This bot will give you direct links of mdisk if you send your mdisk link to this bot! 

### Host it on VPS or Locally

```sh
git clone https://github.com/Akcrazytech-YT/mdisk
cd mdisk
python3 -m venv ./venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 -m Bot
```

and to stop the whole bot,
 do <kbd>CTRL</kbd>+<kbd>C</kbd>

> **If you wanna run this bot 24/7 on the VPS, follow thesesteps.**
> ```sh
> sudo apt install tmux -y
> tmux
> python3 -m Bot
> ```
> now you can close the VPS and the bot will run on it.

### Mandatory Vars
Before running the bot, you will need to set up the following mandatory variables:

- `API_ID` : This is the API ID for your Telegram account, which can be obtained from my.telegram.org.

- `API_HASH` : This is the API hash for your Telegram account, which can also be obtained from my.telegram.org.

- `BOT_TOKEN` : This is the bot token for the Telegram Media Streamer Bot, which can be obtained from [@BotFather](https://telegram.dog/BotFather).

- `Admin` : Edit Admin Telegram User ID in vars.py.

## Copyright

Copyright (C) 2023 [Akcrazytech-YT](https://github.com/Akcrazytech-YT) under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html).

Mdisk Direct link Bot is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 
