**Liste des composants :**

Une raspberry PI3
Une carte micro SD de 16Go vide
Un �cran, un clavier et une souris.
Un ordinateur compatible wifi (Windows, Mac, Linux)
Un d�tecteur HC-SR501
Une cam�ra raspberry V2 NoIR
6 LEDs
6 R�sistances d'une centaine d'Ohm
Un bouton poussoir
Un amplificateur Kemo M031N
Un haut-parleur Visaton FRS 5 X 2235 86 dB 52.5 mm
Une plaque d'essai (soudure)
Une rallonge du c�ble de la cam�ra si jamais utilisation de la partie audio.

**Mise en place**

T�l�chargez sur votre ordinateur NOOBs ZIP : https://www.raspberrypi.org/downloads/noobs/
Une fois que le fichier est t�l�charg�, d�zippez le et copier les fichiers sur la carte SD. Glissez la carte SD dans l'emplacement d�di� de la raspberry.
Reliez le raspberry PI � un �cran ainsi qu'� un clavier et souris. Une fois que cela est fait, alimentez la raspberry via le port micro usb.
Une fen�tre NOOBS va appara�tre � l'�cran. Veuillez cliquer sur Rasbian puis Install. 
En haut � droite de l'interface de la raspberry, il y a un symbole (une fl�che vers le bas et l'autre vers le haut) qui devrait �tre fixe et de couleur grise. 
Cela signifie que vous n'�tes pas connect� � internet via le c�ble Ethernet. Cliquez sur ce symbole et appuyez sur Turn On Wi-Fi. 
Connectez-vous traditionnellement au Wifi de votre choix. Une fois que cela est fait, ouvrez le terminal de la raspberry (LXTerminal) et tapez la commande 
ifconfig. Cela vous donne plusieurs informations. Tout en bas, il y une ligne commen�ant par wlan0. A partir de l�, cherchez une ligne inet XXX.XXX.XXX.XXX.
Retenez bien cette adresse.
Apr�s avoir termin� l'installation, ouvrez le terminal de la raspberry . 
Puis rentrez la commande : git clone --recursive https://github.com/Mathis13/Alarme-detection-de-mouvement
Le fichier t�l�charg� est situ� dans le r�pertoire /home/pi. Ouvrez le fichier ProgrammeFinal.py avec un logiciel tel que geany (pour t�l�charger geany, 
Ouvrez le terminal et tapez la commande : sudo apt-get install geany).

Ensuite il va falloir t�l�charger les modules n�cessaires au bon fonctionnement du programme : RPi.GPIO ; time ; sys ; smtplib ; os ; picamera ; pygame.
Ouvrez le terminal et tapez la commande : sudo pip install NomDuModule. 
Par exemple pour le module time, il suffit de taper dans le terminal :sudo pip install time

Puis il va falloir activer diff�rentes fonctions de votre rapsberry. Pour cela, tapez dans le terminal sudo raspi-config. Vous allez arriver sur une Fen�tre graphique. 
Commen�ons par les ports de la raspberry. Rendez-vous dans la partie 5 de la fen�tre : "Interfacing Options". Puis vous allez 
S�lectionnez tout d'abord P1 Camera puis OUI puis OK. Ensuite P2 SSH puis OUI puis OK. Pour la connexion SSH, il vous sera peut-�tre demand� de changer
de mot de passe. Pour finir P8 Remote GPIO puis OUI puis OK. 
Maintenant revenez sur la premi�re fen�tre et s�lectionnez 7 Advanced Options. Puis rendez-vous dans la partie A4 Audio. Choisissez 1 Force 3.5mm jack.
Maintenant vous pouvez sortir de l'interface avec Finish. Il vous faudra surement si cela n'est pas demand� de rebooter la raspberry PI.


Modifier ProgrammeFinal:
A la ligne 51, vous pouvez saisir la dur�e en secondes de votre enregistrement vid�o.
A la ligne 84, rentrez l'adresse compl�te gmail d'exp�dition.
A la ligne 85, rentrez l'adresse compl�te gmail de r�ception.
A la ligne 91, d�finissez l'objet de votre email.
A la ligne 93, veuillez saisir le texte de votre email.
A la ligne 109, vous devez rentrer le mot de passe de l'adresse d'exp�dition.
Avant de continuer, il faut que vous vous connectiez par internet (directement sur le site de gmail), � l'adresse d'exp�dition, afin de faire conna�tre l'adresse IP de votre machine. Une fois que vous vous �tes connectez, vous pouvez fermer votre navigateur.

A partir de l�, vous pouvez d�connectez la raspberry en effectuant un SHUTDOWN (terminal commande : shutdown -h now)
Pour vous connectez � la raspberry via votre ordinateur. Alimentez � nouveau la raspberry PI. 
Quel que soit votre ordinateur, connectez-vous au m�me Wifi que la raspberry.
#	Puis si vous �tes sous windows, t�l�chargez Putty : 
https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html (32 ou 64 bits en fonction 
de votre ordinateur). Ouvrez le fichier t�l�chargez et lancez l'installation. Une fois cela termin�, ouvrez l'application Putty. 
Dans la case Saved Sessions, rentrez l'adresse IP de la raspberry que vous avez retenu. Puis cliquez sur Save. 
Ensuite s�lectionnez cette adresse dans le menu juste en dessous puis cliquez sur Load. 
Une fois que l'adresse est apparu dans la case Host Name cliquez sur open. Vous retrouvez le terminal de la raspberry sur votre ordinateur.
(d�sormais l'adresse est enregistr�e, � chaque que vous voulez vous connectez cliquez sur l'adresse puis sur load).
#	Si vous �tes sous Mac ou Linux, ouvrez simplement votre terminal puis rentrez la commande : ssh pi@adresseIPdelaraspberryretenu
Comme sous Windows, vous retrouvez le terminal de la raspberry.

**C�blage :**

Vous pouvez trouver la fonction de chaque port de la raspberry sur : 
https://deusyss.developpez.com/tutoriels/RaspberryPi/PythonEtLeGpio/

Pour le d�tecteur : En prenant le d�tecteur de face (les 2 potentiom�tres oranges � l'arri�re), 
la broche la plus � gauche est reli� � la masse, celle du milieu doit �tre reli� au port GPIO7 (SPI-CE1), et la broche la plus � droite au +5V (de la raspberry)

Pour la cam�ra : Elle doit �tre reli�e au port CSI (juste � c�t� de la prise jack) cot� bleu orient� vers la prise Ethernet.

Les LEDs et les R�sistances : La patte la plus longue de chaque LED doit �tre reli�e respectivement au port GPIO (21, 20, 16, 26, 19, 13). 
Les pattes les plus courtes doivent �tre reli� � la masse par l'interm�diaire d'une r�sistance.

Pour le bouton poussoir : Une des broches du bouton doit �tre reli� � la masse. L'autre doit �tre c�bl� au port GPIO12.

Pour la partie audio, utilisez la plaque de soudure. Prenez l'amplificateur audio de fasse (nom du boitier face � vous). Il suffit de brancher la broche la plus � gauche sur une patte du haut-parleur. Puis la broche juste � cot� sur l'alimentation du raspberry. La troisi�me doit �tre reli� � la fois � la masse et � l'autre patte du haut-parleur. Les deux derni�res broches doivent �tre reli� � la prise jack de la rapsberry (si l'on retourne la  raspberry, au niveau de la prise jack on peut retrouver les ports gauche : port PP25 ; droite : PP26).

Il existe ainsi deux types de boitier. L'un avec haut-parleur et l'autre sens.
Apr�s avoir imprim� le boitier (les fichiers STL de la boite ainsi que du couvercle en fonction de votre version). Veuillez installer les composants.
Tout d'abord commencez par placer la cam�ra ainsi que le d�tecteur, puis ensuite le raspberry PI.
Une fois que tout cela est fait, vous pouvez fermer le boitier et alimenter la raspberry PI. Pour permettre la connexion entre le couvercle et la bo�te, 
il vous faudra ins�rer un morceaux de m�tal pour fixer le tout.

**Lancement**

Maintenant que tout est connect�, il faut que vous vous rendiez dans le r�pertoire du fichier ProgrammeFinal.py. Pour cela naviguez dans les dossiers du 
Raspberry avec cd Nomdudossier pour aller dans un dossier, ls pour afficher le contenu du dossier et cd..  pour revenir une �tape en arri�re.
Le fichier t�l�chargez est situ� dans le r�pertoire /home/pi. Une fois le r�pertoire du fichier ProgrammeFinal.py trouv�, vous pouvez lancer le programme
avec la commande : python ProgrammeFinal.py. 
A partir de la votre syst�me est op�rationnel.
Pour arr�ter le programme, il suffit de faire une ctrl c sur le terminal.

