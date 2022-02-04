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
    find "features/reports/temp" -type f \( -iname \*.json -o -iname \*.png \) -exec mv {} "$new_subFolder" \;
else
    #Directory does not exist
    mkdir "features/reports/$new_folder"
    sleep 2
    mkdir "$new_subFolder"
    sleep 2
    find "features/reports/temp" -type f \( -iname \*.json -o -iname \*.png \) -exec mv {} "$new_subFolder" \;
fi

#allure serve "$new_subFolder"
