#! /bin/sh

now=$(date +"%H-%M-%S")
new_folder=$(date '+%Y-%m-%d')
new_subFolder="features/reports/$new_folder/$now"
new_folder_sc="features/screenshots/$new_folder"
new_subFolder_sc="features/screenshots/$new_folder/$now"

#Create Subfolder to move all reports created by date and time
if [ -d "features/reports/$new_folder" ]
then
    #Directory exists
    mkdir "$new_subFolder"
    sleep 2
    find "features/reports/temp" -name '*.json' -exec mv {} "$new_subFolder" \;
else
    #Directory does not exist
    mkdir "features/reports/$new_folder"
    sleep 2
    mkdir "$new_subFolder"
    sleep 2
    find "features/reports/temp" -name '*.json' -exec mv {} "$new_subFolder" \;
fi

#Check if screenshots exists then move all of them
	if [ "$(ls -A "features/screenshots/temp")" ]
	then
    if [ -d "features/screenshots/$new_folder" ]
    then
        #Folder exists
        mkdir "$new_subFolder_sc"
        sleep 2
        find "features/screenshots/temp" -name '*.png' -exec mv {} "$new_subFolder_sc" \;
    else
       #Subfolder does not exist
       mkdir "features/screenshots/$new_folder"
       sleep 2
       mkdir "$new_subFolder_sc"
       find "features/screenshots/temp" -name '*.png' -exec mv {} "$new_subFolder_sc" \;
    fi
	fi

allure serve "$new_subFolder"
