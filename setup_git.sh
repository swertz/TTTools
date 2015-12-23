#!/bin/bash
# configure the origin repository
GITHUBUSERNAME=`git config user.github`
GITHUBUSERREMOTE=`git remote -v | grep upstream | awk '{print $2}' | head -n 1 | cut -d / -f 2`
git remote add origin git@github.com:${GITHUBUSERNAME}/${GITHUBUSERREMOTE}

git remote add blinkseb https://github.com/blinkseb/TTTools.git
# might fork:
git remote add OlivierBondu https://github.com/OlivierBondu/TTTools.git
git remote add delaere https://github.com/delaere/TTTools.git
git remote add BrieucF https://github.com/BrieucF/TTTools.git
git remote add swertz https://github.com/swertz/TTTools.git
git remote add vidalm https://github.com/vidalm/TTTools.git
git remote add camillebeluffi https://github.com/camillebeluffi/TTTools.git
git remote add acaudron https://github.com/acaudron/TTTools.git
git remote add AlexandreMertens https://github.com/AlexandreMertens/TTTools.git

