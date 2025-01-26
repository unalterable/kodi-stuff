#!/bin/bash

# Define the base directory and repository structure
BASE_DIR="."
REPO_ID="repository-myrepo"
ADDON_ID="plugin.video.mygraphqladdon"
ADDON_VERSION="1.0.0"

# Create folder structure
echo "Creating folder structure..."
mkdir -p $BASE_DIR/$REPO_ID/zips/$ADDON_ID

# Zip the add-on
echo "Zipping the add-on..."
cd $BASE_DIR/$REPO_ID/zips
zip -r "$ADDON_ID-$ADDON_VERSION.zip" $ADDON_ID
# rm -rf $ADDON_ID
cd -

# Generate MD5 checksum for addons.xml
echo "Generating addons.xml.md5..."
md5sum $BASE_DIR/$REPO_ID/addons.xml | awk '{ print $1 }' > $BASE_DIR/$REPO_ID/addons.xml.md5

echo "Repository creation complete! All files are located in the $BASE_DIR directory."
