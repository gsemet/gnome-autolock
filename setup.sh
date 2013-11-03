#!/bin/bash

mkdir -p ~/.config/autostart/
cp -v resources/configure-autolock.desktop /usr/share/applications/autolock.desktop
cp -v resources/autolock.desktop ~/.config/autostart/autolock.desktop

update-desktop-database
