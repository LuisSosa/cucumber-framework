#! /bin/sh

if [ -f "automation.log" ]; then
    rm automation.log
fi

#Check if exists path and remove all files generated for allure report
if [ -d "features/reports/temp" ]
then
    rm -rf features/reports/temp/*
fi
