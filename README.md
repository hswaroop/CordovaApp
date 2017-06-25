# CordovaApp
Automating the Android app build process using Apache Cordova CLI.

The csv file is a template which seems familiar to the python script which i have created.
So I would recommend to follow this template.

To start building a cordova app - you can go to https://cordova.apache.org/docs/en/latest/guide/cli/
The doc explains everything in detail.

I would list some basic commands from that doc that would help you creating your app.

1. cordova create hello com.example.hello HelloWorld
2. cordova platform add android

To build the app - 
You will need Java SDK - http://www.oracle.com/technetwork/java/javase/downloads/index.html
              Android SDK - http://filehippo.com/download_android_sdk/tech/ (A helpful link to get the Android SDK as well)
              Gradle - https://gradle.org/
              
You have to change the environment variables accordingly for all three of these

# After this you will be able to run cordova build command
3. cordova build

These 3 basic commands will help you build the cordova app.

Instructions for using the script -

1. Make a new folder inside the app folder which you have created.
2. Place your icons and splash screens inside that
- Just these two files should be there inside this folder.

3. Place the your modified csv file and the pyhton script inside the same directory where the app folder resides.
4. In your config.xml delete everything inside the "platform" element.

Just these recommendations and you are good to go to automate the building process.

* Let me know if you have any difficulty or face any errors, I would be happy to resolve every issue.




