<<<<<< Partie Réalisation >>>>>> Si le boitier est déjà réalisé, vous pouvez dès maintenant aller à la seconde partie "mise en place"

**Liste des composants :**

Une raspberry PI3
Une carte micro SD de 16Go vide
Un Écran, un clavier et une souris.
Un ordinateur compatible wifi (Windows, Mac, Linux)
Un dÉtecteur HC-SR501
Une caméra raspberry V2 NoIR
6 LEDs
6 Résistances d'une centaine d'Ohm
Un bouton poussoir
Un amplificateur Kemo M031N
Un haut-parleur Visaton FRS 5 X 2235 86 dB 52.5 mm
Une plaque d'essai (soudure)
Une rallonge du câble de la caméra si jamais utilisation de la partie audio.

Téléchargez sur votre ordinateur NOOBs ZIP : https://www.raspberrypi.org/downloads/noobs/
Une fois que le fichier est téléchargé, dézippez le et copier les fichiers sur la carte SD. Glissez la carte SD dans l'emplacement dédié de la raspberry.
Reliez le raspberry PI à un écran ainsi qu'à un clavier et souris. Une fois que cela est fait, alimentez la raspberry via le port micro usb.
Une fenêtre NOOBS va apparaître à l'écran. Veuillez cliquer sur Rasbian puis Install. 
En haut à droite de l'interface de la raspberry, il y a un symbole (une flèche vers le bas et l'autre vers le haut) qui devrait être fixe et de couleur grise. 
Cela signifie que vous n'êtes pas connecté à internet via le câble Ethernet. Cliquez sur ce symbole et appuyez sur Turn On Wi-Fi. 
Connectez-vous traditionnellement au Wifi de votre choix. Une fois que cela est fait, ouvrez le terminal de la raspberry (LXTerminal) et tapez la commande ifconfig. Cela vous donne plusieurs informations. Tout en bas, il y une ligne commençant par wlan0. A partir de là, cherchez une ligne inet XXX.XXX.XXX.XXX. (192.168.43.4 / password:musique2)
Retenez bien cette adresse.
Après avoir terminé l'installation, ouvrez le terminal de la raspberry . 
Puis rentrez la commande : git clone --recursive https://github.com/Mathis13/Alarme-detection-de-mouvement
Le fichier téléchargé est situé dans le répertoire /home/pi. Ouvrez le fichier ProgrammeFinal.py avec un logiciel tel que geany (pour télécharger geany, Ouvrez le terminal et tapez la commande : sudo apt-get install geany).

Ensuite il va falloir télécharger les modules nécessaires au bon fonctionnement du programme : RPi.GPIO ; time ; sys ; smtplib ; os ; picamera ; pygame.
Ouvrez le terminal et tapez la commande : sudo pip install NomDuModule. 
Par exemple pour le module time, il suffit de taper dans le terminal :sudo pip install time

Puis il va falloir activer différentes fonctions de votre rapsberry. Pour cela, tapez dans le terminal sudo raspi-config. Vous allez arriver sur une Fenêtre graphique. 
Commençons par les ports de la raspberry. Rendez-vous dans la partie 5 de la fenêtre : "Interfacing Options". Puis vous allez 
Sélectionnez tout d'abord P1 Camera puis OUI puis OK. Ensuite P2 SSH puis OUI puis OK. Pour la connexion SSH, il vous sera peut-être demandé de changer
de mot de passe. Pour finir P8 Remote GPIO puis OUI puis OK. 
Maintenant revenez sur la première fenêtre et sélectionnez 7 Advanced Options. Puis rendez-vous dans la partie A4 Audio. Choisissez 1 Force 3.5mm jack.
Maintenant vous pouvez sortir de l'interface avec Finish. Il vous faudra surement si cela n'est pas demandŽ de rebooter la raspberry PI.

**Câblage :**

Vous pouvez trouver la fonction de chaque port de la raspberry sur : 
https://deusyss.developpez.com/tutoriels/RaspberryPi/PythonEtLeGpio/

Pour le détecteur : En prenant le détecteur de face (les 2 potentiomètres oranges à l'arrière), 
la broche la plus ˆ gauche est relié à la masse, celle du milieu doit être relié au port GPIO7 (SPI-CE1), et la broche la plus à droite au +5V (de la raspberry)

Pour la caméra : Elle doit être reliée au port CSI (juste à côté de la prise jack) coté bleu orienté vers la prise Ethernet.

Les LEDs et les Résistances : La patte la plus longue de chaque LED doit être reliée respectivement au port GPIO (21, 20, 16, 26, 19, 13). 
Les pattes les plus courtes doivent être relié à la masse par l'intermédiaire d'une résistance.

Pour le bouton poussoir : Une des broches du bouton doit être relié à la masse. L'autre doit être câblé au port GPIO12.

Pour la partie audio, utilisez la plaque de soudure. Prenez l'amplificateur audio de fasse (nom du boitier face à vous). Il suffit de brancher la broche la plus à gauche sur une patte du haut-parleur. Puis la broche juste à coté sur l'alimentation du raspberry. La troisième doit être relié à la fois à la masse et à l'autre patte du haut-parleur. Les deux dernières broches doivent être relié à la prise jack de la rapsberry (si l'on retourne la  raspberry, au niveau de la prise jack on peut retrouver les ports gauche : port PP25 ; droite : PP26).

Il existe ainsi deux types de boitier. L'un avec haut-parleur et l'autre sens.
Après avoir imprimé le boitier (les fichiers STL de la boite ainsi que du couvercle en fonction de votre version). Veuillez installer les composants.
Tout d'abord commencez par placer la caméra ainsi que le détecteur, puis ensuite le raspberry PI.
Une fois que tout cela est fait, vous pouvez fermer le boitier et alimenter la raspberry PI. Pour permettre la connexion entre le couvercle et la boîte, 
il vous faudra insérer un morceaux de métal pour fixer le tout.

<<<<<< Partie Mise en place >>>>>>

Tout d'abord il faut activer les applications qui utilisent la connexion moins sécurisée sans les 
paramètres de votre adresse email.

Modifier ProgrammeFinal:
A la ligne 51, vous pouvez saisir la durée en secondes de votre enregistrement vidéo.
A la ligne 84, rentrez l'adresse complète gmail d'expédition (fonctionne avec tout les autres plateformes : il suffit de modifier la ligne 107 en remplaçant gmail par le système choisit, ex: adressetest@yaoo.com --> l107 : 'smtp.yahoo.com',587
A la ligne 85, rentrez l'adresse complète gmail de réception.
A la ligne 91, définissez l'objet de votre email.
A la ligne 93, veuillez saisir le texte de votre email.
A la ligne 109, vous devez rentrer le mot de passe de l'adresse d'expédition.
Avant de continuer, il faut que vous vous connectiez par internet (directement sur le site de gmail), ˆ l'adresse d'expédition, afin de faire connaître l'adresse IP de votre machine. Une fois que vous vous êtes connectez, vous pouvez fermer votre navigateur.

A partir de là, vous pouvez déconnectez la raspberry en effectuant un SHUTDOWN (terminal commande : shutdown -h now)
Pour vous connectez à la raspberry via votre ordinateur. Alimentez à nouveau la raspberry PI. 
Quel que soit votre ordinateur, connectez-vous au même Wifi que la raspberry.
#	Puis si vous êtes sous windows, téléchargez Putty : 
https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html (32 ou 64 bits en fonction 
de votre ordinateur). Ouvrez le fichier téléchargez et lancez l'installation. Une fois cela terminé, ouvrez l'application Putty.
Dans la case Saved Sessions, rentrez l'adresse IP de la raspberry que vous avez retenu. Puis cliquez sur Save. 
Ensuite sélectionnez cette adresse dans le menu juste en dessous puis cliquez sur Load. 
Une fois que l'adresse est apparu dans la case Host Name cliquez sur open. Vous retrouvez le terminal de la raspberry sur votre ordinateur.
(désormais l'adresse est enregistrée, à chaque que vous voulez vous connectez cliquez sur l'adresse puis sur load).
#	Si vous êtes sous Mac ou Linux, ouvrez simplement votre terminal puis rentrez la commande : ssh pi@adresseIPdelaraspberryretenu
Comme sous Windows, vous retrouvez le terminal de la raspberry.


**Lancement**

Maintenant que tout est connecté, il faut que vous vous rendiez dans le répertoire du fichier ProgrammeFinal.py. Pour cela naviguez dans les dossiers du 
Raspberry avec cd Nomdudossier pour aller dans un dossier, ls pour afficher le contenu du dossier et cd..  pour revenir une ƒtape en arrière.
Le fichier téléchargez est situé dans le répertoire /home/pi. Une fois le répertoire du fichier ProgrammeFinal.py trouvé, vous pouvez lancer le programme
avec la commande : python ProgrammeFinal.py. 
A partir de la votre système est opérationnel.
Pour arreter le programme, il suffit de faire un ctrl+c sur le terminal.

