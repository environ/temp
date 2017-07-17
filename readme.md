Raspberry PI ja pythonit kasutades DS18B20 anduritelt temperatuuri lugemiseks ja edastamiseks json abil (emoncms serverisse ntx)

add cron

sudo crontab -e


@reboot sudo python -u ~/temp/temp.py &
*/20 * * * * sudo ~/temp/kontroll.sh
