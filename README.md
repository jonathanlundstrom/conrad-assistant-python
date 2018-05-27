# Conrad Assistant

This project aims to help you create your own Google Home through the use of a Raspberry Pi, an Arduino Nano and some cheap components such as a USB soundcard, speaker and microphone. The project was developed in partnership with [Conrad](https://www.conrad.se/) in their efforts to showcase makers around Sweden. I would therefore like to thank them for providing the hardware used in this project. Please also check out [their website](http://tekkie.se/) for more interesting projects. I would also like to thank Eric Vinjegaard for his work on the 3D-printed chassi and Jirka van der Roest for his work on the Arduino code.

### Usage
Clone the repository to a folder of your liking and use the following command to start the software:

    python assistant.py
    
### Build guide
Please refer to this link for a complete description on how and where to use this software.

[http://jonathanlundstrom.me/2018/05/27/project-conrad-assistant/](http://jonathanlundstrom.me/2018/05/27/project-conrad-assistant/)

### Supervisor job
If you wish to have the software running all the time, you can use Supervisor to accomplish this. This is the configuration file that I use. It should be placed in `/etc/supervisor/conf.d` and named `sensor.conf` or similar.

    [program:assistant]
    user=pi
    directory=/home/pi
    environment=HOME="/home/pi",USER="pi"
    command=/home/pi/env/bin/python /home/pi/Applications/ConradAssistant/assistant.py
    autostart=true
    autorestart=true
    stderr_logfile=/var/log/assistant.err.log
    stdout_logfile=/var/log/assistant.out.log

### Finished product
This section will in time be updated with a video of the final build and product.