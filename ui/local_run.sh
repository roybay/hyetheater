#!/bin/sh

echo installing
npm install --verbose --cache /root/.npm

echo installing react-scripts
npm install react-scripts@3.4.1 -g --verbose --cache /root/.npm

echo starting
npm start --verbose
