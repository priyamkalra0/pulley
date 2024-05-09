# Pulley: Simple tool for pulling files and directories (recursively) over the Android Debug Bridge
## Usage
ADB Shell needs to be installed and available on PATH. Connection to the device must also be established before hand.  
The tool is not avaiable as a package, so you need to manually download and include it in your project, after that it can be used as such:
```py
from pulley import Pulley

pulley = Pulley(as_package="com.example.package")
pulley.pull_dir(remote_path=f"/data/data/com.example.package", local_path="./sample")
```

The above snippet will pull all the private appdata of the (debug-enabled) package `com.example.package` to ./sample directory.
It will also print all pulled files to the console like so:
```
/data/data/com.example.package/databases/classplus_v2.db
/data/data/com.example.package/databases/classplus_v2.db-journal
/data/data/com.example.package/databases/clevertap
/data/data/com.example.package/databases/clevertap-journal
/data/data/com.example.package/databases/com.google.android.datatransport.events
/data/data/com.example.package/databases/com.google.android.datatransport.events-journal
/data/data/com.example.package/databases/google_analytics_v4.db
/data/data/com.example.package/databases/google_analytics_v4.db-journal
/data/data/com.example.package/databases/google_app_measurement_local.db
/data/data/com.example.package/databases/google_app_measurement_local.db-journal
/data/data/com.example.package/files/PersistedInstallation.W0RFRkFVTFRd+MTo3MjIxNTU1NjYxOTQ6YW5kcm9pZDowZWFiYTFjOThjZGZmYWJjNWVmZWVi.json
/data/data/com.example.package/files/generatefid.lock
/data/data/com.example.package/no_backup/com.google.android.gms.appid-no-backup
/data/data/com.example.package/shared_prefs/FirebaseAppHeartBeat.xml
/data/data/com.example.package/shared_prefs/INTERCOM_DEDUPER_PREFS.xml
/data/data/com.example.package/shared_prefs/INTERCOM_SDK_PREFS.xml
/data/data/com.example.package/shared_prefs/Survicate.xml
/data/data/com.example.package/shared_prefs/WizRocket.xml
/data/data/com.example.package/shared_prefs/WizRocket_counts_per_inapp.xml
/data/data/com.example.package/shared_prefs/WizRocket_local_events.xml
/data/data/com.example.package/shared_prefs/com.google.android.gms.analytics.prefs.xml
/data/data/com.example.package/shared_prefs/com.google.android.gms.appid.xml
/data/data/com.example.package/shared_prefs/com.google.android.gms.measurement.prefs.xml
/data/data/com.example.package/shared_prefs/com.google.firebase.crashlytics.xml
```
