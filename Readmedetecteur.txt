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
Une rallonge du c‰ble de la camŽra si jamais utilisation de la partie audio.

TŽlŽchargez sur votre ordinateur NOOBs ZIP : https://www.raspberrypi.org/downloads/noobs/
Une fois que le fichier est tŽlŽchargŽ, dŽzippez le et copier les fichiers sur la carte SD. Glissez la carte SD dans l'emplacement dŽdiŽ de la raspberry.
Reliez le raspberry PI ˆ un ƒcran ainsi qu'ˆ un clavier et souris. Une fois que cela est fait, alimentez la raspberry via le port micro usb.
Une fentre NOOBS va appara”tre ˆ l'Žcran. Veuillez cliquer sur Rasbian puis Install. 
En haut ˆ droite de l'interface de la raspberry, il y a un symbole (une flche vers le bas et l'autre vers le haut) qui devrait tre fixe et de couleur grise. 
Cela signifie que vous n'tes pas connectŽ ˆ internet via le c‰ble Ethernet. Cliquez sur ce symbole et appuyez sur Turn On Wi-Fi. 
Connectez-vous traditionnellement au Wifi de votre choix. Une fois que cela est fait, ouvrez le terminal de la raspberry (LXTerminal) et tapez la commande 
ifconfig. Cela vous donne plusieurs informations. Tout en bas, il y une ligne commenant par wlan0. A partir de lˆ, cherchez une ligne inet XXX.XXX.XXX.XXX.
Retenez bien cette adresse.
Aprs avoir terminŽ l'installation, ouvrez le terminal de la raspberry . 
Puis rentrez la commande : git clone --recursive https://github.com/Mathis13/Alarme-detection-de-mouvement
Le fichier tŽlŽchargŽ est situŽ dans le rŽpertoire /home/pi. Ouvrez le fichier ProgrammeFinal.py avec un logiciel tel que geany (pour tŽlŽcharger geany, 
Ouvrez le terminal et tapez la commande : sudo apt-get install geany).

Ensuite il va falloir tŽlŽcharger les modules nŽcessaires au bon fonctionnement du programme : RPi.GPIO ; time ; sys ; smtplib ; os ; picamera ; pygame.
Ouvrez le terminal et tapez la commande : sudo pip install NomDuModule. 
Par exemple pour le module time, il suffit de taper dans le terminal :sudo pip install time

Puis il va falloir activer diffŽrentes fonctions de votre rapsberry. Pour cela, tapez dans le terminal sudo raspi-config. Vous allez arriver sur une Fenêtre graphique. 
Commenons par les ports de la raspberry. Rendez-vous dans la partie 5 de la fentre : "Interfacing Options". Puis vous allez 
Sélectionnez tout d'abord P1 Camera puis OUI puis OK. Ensuite P2 SSH puis OUI puis OK. Pour la connexion SSH, il vous sera peut-tre demandŽ de changer
de mot de passe. Pour finir P8 Remote GPIO puis OUI puis OK. 
Maintenant revenez sur la premire fentre et sŽlectionnez 7 Advanced Options. Puis rendez-vous dans la partie A4 Audio. Choisissez 1 Force 3.5mm jack.
Maintenant vous pouvez sortir de l'interface avec Finish. Il vous faudra surement si cela n'est pas demandŽ de rebooter la raspberry PI.

**C‰blage :**

Vous pouvez trouver la fonction de chaque port de la raspberry sur : 
https://deusyss.developpez.com/tutoriels/RaspberryPi/PythonEtLeGpio/

Pour le dŽtecteur : En prenant le dŽtecteur de face (les 2 potentiomtres oranges à l'arrire), 
la broche la plus ˆ gauche est reliŽ ˆ la masse, celle du milieu doit tre reliŽ au port GPIO7 (SPI-CE1), et la broche la plus ˆ droite au +5V (de la raspberry)

Pour la camŽra : Elle doit tre reliŽe au port CSI (juste à côté de la prise jack) cotŽ bleu orientŽ vers la prise Ethernet.

Les LEDs et les RŽsistances : La patte la plus longue de chaque LED doit tre reliŽe respectivement au port GPIO (21, 20, 16, 26, 19, 13). 
Les pattes les plus courtes doivent tre reliŽ ˆ la masse par l'intermŽdiaire d'une rŽsistance.

Pour le bouton poussoir : Une des broches du bouton doit tre reliŽ ˆ la masse. L'autre doit tre c‰blŽ au port GPIO12.

Pour la partie audio, utilisez la plaque de soudure. Prenez l'amplificateur audio de fasse (nom du boitier face ˆ vous). Il suffit de brancher la broche la plus ˆ gauche sur une patte du haut-parleur. Puis la broche juste ˆ cotŽ sur l'alimentation du raspberry. La troisime doit tre reliŽ ˆ la fois ˆ la masse et ˆ l'autre patte du haut-parleur. Les deux dernires broches doivent tre reliŽ ˆ la prise jack de la rapsberry (si l'on retourne la  raspberry, au niveau de la prise jack on peut retrouver les ports gauche : port PP25 ; droite : PP26).

Il existe ainsi deux types de boitier. L'un avec haut-parleur et l'autre sens.
Aprs avoir imprimŽ le boitier (les fichiers STL de la boite ainsi que du couvercle en fonction de votre version). Veuillez installer les composants.
Tout d'abord commencez par placer la camŽra ainsi que le dŽtecteur, puis ensuite le raspberry PI.
Une fois que tout cela est fait, vous pouvez fermer le boitier et alimenter la raspberry PI. Pour permettre la connexion entre le couvercle et la bo”te, 
il vous faudra insŽrer un morceaux de mŽtal pour fixer le tout.

<<<<<< Partie Mise en place >>>>>>

Tout d'abord il faut activer les applications qui utilisent la connexion moins sécurisée sans les 
paramètres de votre adresse email.

Modifier ProgrammeFinal:
A la ligne 51, vous pouvez saisir la durŽe en secondes de votre enregistrement vidéo.
A la ligne 84, rentrez l'adresse complte gmail d'expŽdition (fonctionne avec tout les autres plateformes : il suffit de modifier la ligne 107 en remplaçant gmail par le système choisit, ex: adressetest@yaoo.com --> l107 : 'smtp.yahoo.com',587
A la ligne 85, rentrez l'adresse complte gmail de rŽception.
A la ligne 91, dŽfinissez l'objet de votre email.
A la ligne 93, veuillez saisir le texte de votre email.
A la ligne 109, vous devez rentrer le mot de passe de l'adresse d'expŽdition.
Avant de continuer, il faut que vous vous connectiez par internet (directement sur le site de gmail), ˆ l'adresse d'expŽdition, afin de faire conna”tre l'adresse IP de votre machine. Une fois que vous vous ætes connectez, vous pouvez fermer votre navigateur.

A partir de là, vous pouvez dŽconnectez la raspberry en effectuant un SHUTDOWN (terminal commande : shutdown -h now)
Pour vous connectez à la raspberry via votre ordinateur. Alimentez à nouveau la raspberry PI. 
Quel que soit votre ordinateur, connectez-vous au mme Wifi que la raspberry.
#	Puis si vous ætes sous windows, tŽlŽchargez Putty : 
https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html (32 ou 64 bits en fonction 
de votre ordinateur). Ouvrez le fichier tŽlŽchargez et lancez l'installation. Une fois cela terminŽ, ouvrez l'application Putty. 
Dans la case Saved Sessions, rentrez l'adresse IP de la raspberry que vous avez retenu. Puis cliquez sur Save. 
Ensuite sŽlectionnez cette adresse dans le menu juste en dessous puis cliquez sur Load. 
Une fois que l'adresse est apparu dans la case Host Name cliquez sur open. Vous retrouvez le terminal de la raspberry sur votre ordinateur.
(dŽsormais l'adresse est enregistrŽe, ˆ chaque que vous voulez vous connectez cliquez sur l'adresse puis sur load).
#	Si vous ætes sous Mac ou Linux, ouvrez simplement votre terminal puis rentrez la commande : ssh pi@adresseIPdelaraspberryretenu
Comme sous Windows, vous retrouvez le terminal de la raspberry.


**Lancement**

Maintenant que tout est connectŽ, il faut que vous vous rendiez dans le rŽpertoire du fichier ProgrammeFinal.py. Pour cela naviguez dans les dossiers du 
Raspberry avec cd Nomdudossier pour aller dans un dossier, ls pour afficher le contenu du dossier et cd..  pour revenir une ƒtape en arrire.
Le fichier tŽlŽchargez est situé dans le rŽpertoire /home/pi. Une fois le rŽpertoire du fichier ProgrammeFinal.py trouvŽ, vous pouvez lancer le programme
avec la commande : python ProgrammeFinal.py. 
A partir de la votre systme est opŽrationnel.
Pour arrter le programme, il suffit de faire une ctrl c sur le terminal.

