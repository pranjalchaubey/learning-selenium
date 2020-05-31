echo off
title AI Poet Development Setup
echo AI Poet Development Setup
echo ========================================================
echo ========================================================
echo ========================================================
echo This batch file will create the AI Poet development environment 
echo
echo Make sure you have modified C:/Users/pranjal/anaconda3/Scripts/activate
echo The path should point to the ../anaconda3/Scripts/activate
timeout /T 10 /NOBREAK
echo Setup Execution Starting.... 
echo ========================================================
echo ========================================================
echo ========================================================
echo Activating Conda Base Environment 
timeout /T 2
::
::
:: PLEASE CHANGE THE PATH BELOW
:: KINDLY ENSURE THAT IT POINTS TO ../anaconda3/Scripts/activate
call c:/Users/pranj/anaconda3/Scripts/activate
::
::
echo ========================================================
echo ========================================================
echo ========================================================
echo Creating the 'ai-poet' environment 
timeout /T 2
call conda create -n ai-poet pip python=3.7.6 numpy pandas scikit-learn matplotlib tqdm beautifulsoup4 tabulate pipdeptree lxml selenium pylint
echo ========================================================
echo ========================================================
echo ========================================================
echo Activating ai-poet environment 
timeout /T 2
call conda activate ai-poet
echo ========================================================
echo ========================================================
echo ========================================================
echo CONGRATULATIONS! You have succesfully setup the AI Poet 
echo Development Environment! 
timeout /T 10