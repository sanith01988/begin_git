export BEEP=/usr/share/sounds/ubuntu/stereo/phone-incoming-call.ogg
if ping -q -c 4 -W 1 8.8.8.8 >/dev/null; then
  echo "Network is up"
else
  echo "Network is down"
paplay $BEEP
paplay $BEEP
paplay $BEEP
fi
