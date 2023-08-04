@echo off

echo "    ___            __                               __     _         	
echo "   /   |  __  __  / /_  ____    ____ ___   ____ _  / /_   (_)  ______ 	
echo "  / /| | / / / / / __/ / __ \  / __ \`__ \ / __ \`/ / __/  / /  /___/	
echo " / ___ |/ /_/ / / /_  / /_/ / / / / / / // /_/ / / /_   / /  / /__   	
echo "/_/  |_|\__,_/  \__/  \____/ /_/ /_/ /_/ \__,_/  \__/  /_/   \___/   	
echo "                                                                     	
echo "       __           __                                               	
echo "  ____/ /  ____ _  / /_  ____ _                                      	
echo " / __  /  / __ \`/ / __/ / __ \`/                                    	
echo "/ /_/ /  / /_/ / / /_  / /_/ /                                       	
echo "\__,_/   \__,_/  \__/  \__,_/                                        	
echo "                                                                     	
echo "    __                      __    _                                  	
echo "   / /  ____   ____ _  ____/ /   (_)   ____    ____ _                	
echo "  / /  / __ \ / __ \`/ / __ /   / /   / __ \  / __ \`/              	
echo " / /  / /_/ // /_/ / / /_/ /   / /   / / / / / /_/ /                 	
echo "/_/   \____/ \__,_/  \__,_/   /_/   /_/ /_/  \__, /                  	
echo "                                            /____/                   		
pause

@echo off

:: Calculate the start timestamp
set _time=%time: =0%
set /a _hours=100%_time:~0,2%%%100,_min=100%_time:~3,2%%%100,_sec=100%_time:~6,2%%%100,_cs=%_time:~9,2%
set /a _started=_hours*60*60*100+_min*60*100+_sec*100+_cs

@echo on
cd %cd%\venv\Scripts\
call activate.bat

cd ..
cd ..
cd %cd%\base_app\

more<nul
echo .............................................
echo .............................................
more<nul
echo STARTING in %time% !!!
echo PLEASE WAIT ....
more<nul
echo .............................................
echo .............................................
more<nul
more<nul

python manage.py makemigrations
python manage.py migrate
python manage.py autoload_dataset

@echo off
:: Calculate the difference in cSeconds
set _time=%time: =0%
set /a _hours=100%_time:~0,2%%%100,_min=100%_time:~3,2%%%100,_sec=100%_time:~6,2%%%100,_cs=%_time:~9,2%
set /a _duration=_hours*60*60*100+_min*60*100+_sec*100+_cs-_started

:: Populate variables for rendering (100+ needed for padding)
set /a _hours=_duration/60/60/100,_min=100+_duration/60/100%%60,_sec=100+(_duration/100%%60%%60),_cs=100+_duration%%100


more<nul
echo __________________________________________________________________________
more<nul
echo DONE AT: %_time% EXECUTION TIME: %_hours%:%_min:~-2%:%_sec:~-2%.%_cs:~-2%
echo __________________________________________________________________________
pause

