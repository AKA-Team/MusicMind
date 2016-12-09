#!/bin/sh
while true; do
    read -p "Download the database (187M) ? " yn
    case $yn in
        [Yy]* ) echo "\nTables\n- train(userID text, songID text, Plays integer)\n- song(songID text, title text, release text, artistName text, year integer)\n";
		wget https://transfer.sh/o5q2l/msd.sqlite3; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
