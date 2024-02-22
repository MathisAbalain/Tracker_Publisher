# Tracker_Publisher

Ce dépôt présente un moyen de d'utiliser les trackers infrarouge VIVE avec le ROS. Un premier programme récupère les données du tracker depuis SteamVR, les enregistre dans un fichier puis les publie via websocket sous la forme d'un protobuf. Le noeud ROS tracker_publisher, lui, reçoit ces données et les republie sous forme de messages TF, adaptés à ROS. Ainsi, la position du tracker peut être visualisé sous Rviz, par exemple.

Le code est dans la branche master.

Pour utiliser ce projet, il faut d'abord avoir une version légérement modifiée de SteamVR.

# SteamVR

Étapes

- telecharger steamVR en version beta

- lancer steamVR une première fois. Dans le dossier .steam/steam/config , le fichier steamvr.vresettings est créé. Fermer steamVR. 

- dans le dossier .steam/steam/steamapps/common/SteamVR/drivers/null/resources/settings/ , modifier le fichier default.vrsettings et modifier le paramètre «enable» de ‘false’ à ‘true’. Cela permettra d’éditer le fichier steamvr.vrsettings.

- dans le dossier .steam/steam/config , modifier le fichier steamvr.vresettings  en ajoutant ces lignes :

> "steamvr"{
    "requireHmd" : false,
    "forcedDriver": null,
    "activateMultipleDrivers": true
},
"driver_null" : {
    "enable" : true
}

Maintenant, steamVR ne demandera pas de connecter un casque avant d’être utilisé, ce qui permet d’utiliser le tracker.

# Utiliser le tracker

- lancer le script vive_server.py , en spécifiant en argument l'adresse IP vers laquelle envoyer les données.

- lancer ensuite le noeud ROS tracker_publisher. Les données TF devraient apparaître dans l'invite de commande, et sont publiées vers les autres noeuds ROS.

