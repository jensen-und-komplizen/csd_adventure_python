# Backlog Items für CSD (Python)
## Generell
* Ich mag "close eyes" nicht. Da könnte ein "restart game" o.ä. besser sein. Damit wird klar, was hier eigentlich gemeint ist.
* "grab" scheint dazzu zu führen, dass Dinge direkt eingesteckt werden. Bei einigen macht es Sinn, dass man sich diese erst einmal ansieht, bevor man sie sich einsteckt.
* Statt "use door to ..." wäre der Befehl "go to ..." besser. "Use ..." sollte verwendbar sein, wenn man einen Gegenstand nutzen kann.
* Die Farben sollten der aus der Java - Version entsprechen.
* Die Texte sollte möglichst der Java - Version entsprechen. Es sei denn, wir finden da was besseres.
* Wir sollen eine Uhr in einem Raum haben, welche die Zeit von <https://csd-timeservice.idiot.games/> abfragt.

## Loo
* Ich möchte im Loo keine Aktionen angezeigt bekommen, die ich hier nicht ausführen kann.
* Ich möchte Aktionen dann angezeigt bekommen, wenn ich diese "entdeckt" habe, z.B.
	* Gegeben: Ich bin im Loo
	* Und: ich habe "look around" eingeben
	* Wenn: ich "look at dirty door" eingebe
	* Dann: sehe ich, dass es sich um die Tür zum Washroom handelt
	* Und: es wird der Button "use door to washroom" sichtbar
	* Und: beim nächsten Aufrauf von "look around" lese ich nicht mehr "pretty dirty door", sondern "door to washroom"
* Mir scheint, als zeigt das Kommando "help" mehr, als über die Buttons möglich. Dies ist inkonsistent und sollte so nicht sein.
* Einige Buttons sorgen dafür, dass im Textfeld kurz ein Text erscheint. Dieser verschwindet sehr schnell wieder und ist kaum zu lesen. Das wirkt eher wie eine Fehler und sollte weg.
* Der Starttext "[...] but at least you have your inventory" liest sich irgendwie steif. Da sollte etwas anderes stehen.
* Ich fänd es gut, wenn die Spielerin anfänglich gar nicht weiß, dass sie Dinge einstecken kann. Das sollte sie herausfinden. Und lasst uns das nicht "Inventory" nennen. Sie hat ihre Hosentaschen. Und vielleicht kommt da im Laufe des Spiels noch ein Rucksack, eine Jacke o.ä. hinzu.
* Wenn sie aufwacht und sich umsieht, dann sollte sie eine Visitenkarte auf dem Boden sehen.
* Die Visitenkarte auf dem Boden kann sie aufheben und lesen. Da steht dann ihr Name und der Jobtitel.
* Die Visitenkarte kann man entweder ablegen oder einstecken.
* Wenn die Visitenkarte eingesteckt wird, so kann man die in der eigenen Hosentasche wiederfinden und ggf. wieder hervorholen.
* Wenn ich die Magazine gesehen habe, dann möchte ich bei "help" nicht mehr "magazines" lesen, sondern die Titel.
* Bei "look around" sollen nur die Dinge angezeigt werden, die sich um mich herum befinden. Dinge aus meiner Tasche sollen hier nicht aufgeführt werden.
* Dinge, die ich mit mir herumtrage, sollen dann angezeigt werden, wenn ich meine Taschen durchsuche oder andere Dinge, die ich mit mir herumtrage, welche Dinge enthalten können (Taschen o.ä.)
* Die Witze kann ich nur nach Bestätigung wieder von vorn lesen. Beim Toilletenpapier ist das anders. Da fängt es wieder von vorn an. Das sollte wie bei den Witzen funktionieren.
* Ich möchte den Coin ansehen können, auch wenn ich diesen noch nicht aufgehoben dann. In dem Fall wäre es gut, die Option zum Aufheben geboten zu bekommen.
* Aus irgend einem Grund führt "grab coin" nicht zum Aufheben, sondern es scheint, als würde die App den Befehl nicht verstehen, obwohl in "help" darauf hingewiesen wird.
* Ich hätte gern einen Befehl "commands", der alle im aktuellen Raum in der aktuellen Situation möglichen Befehle aufzählt.


## Washroom
* Im "Washroom" Einstiegstext heißt es "wash room", nicht "washroom". Das sollte einheitlich sein.
* Aus irgend einem Grund führt "grab coin" nicht zum Aufheben, sondern es scheint, als würde die App den Befehl nicht verstehen, obwohl in "help" darauf hingewiesen wird.
* Es macht keinen Sinn, wenn ich aus dem "Loo" komme und "look around" eingebe, dass ich dann auf der anderen Seite des Raumes zwei Türen sehe: eine Tür zum "Hallway", eine Tür zum "Loo". Die Tür zum Loo sollte hinter mir sein.
* In "look around" sollte die Tür, die zum "Hallway" führt, erst als solche im Text erkennbar sein, wenn man das kleine Türschild gelesen hat.
* Es soll ja etwas über Scrum gelernt werden. Da wäre es schön, wenn statt nur "DoD" "DoD (Definition of Done" zu lesen wäre.
* Da es sich bei der DoD um einen Scrum-Term handelt, sollte man etwas darüber im Spiel lernen können.
* Scrum-Terme sollten anders gehighlighted sein als andere Dinge, da man etwas über Scrum lernen kann. Der Befehl dazu könnte "learn about ..." lauten.
* In der Java-Variante gibt es im "Washroom" einen "Bin" neben der Sink.
* Man sollte den "Washroom" wirklich nur dann verlassen haben, wenn man die DoD erfüllt. Dazu muss man diese aber auch gelesen haben. Das wäre so eine Art Quest.

## Hallway
* "You enter a dark hallway" anstatt "You enter a hallway that looks dark".lo
* Die Tür zum "Teamroom" soll erst als solche identifiziert werden, wenn man sich das Schild an der Tür angesehen hat.
* Es scheint, als kann man nicht in den "Team room".
* In der Java - Version gibt es auf dem Flur ein "dirty poster". Hätt' ich gern.
* In der Java - Version gibt es auf dem Flur drei Türen: eine zur Küche, eine zum Washroom und eine, die spooky ist. Die "spooky door" ist die zum Teamroom.