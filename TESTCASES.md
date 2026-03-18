Testdokumentation für das Kniffelspiel 

Testfälle:
    Spielablauf:
        Wir haben den Spielablauf mit unterschiedlich vielen Spielern getestet.
        Sowohl bei einem Einzelspieler als auch bei 8 Spielern funktioniert das Programm wie vorgesehen. Jeder Spieler kommt 13-mal an die Reihe bevor das Spiel zu Ende ist.
    
    Falscheingaben:
        In die Abfrage der Spieleranzahl wurden Buchstaben, Sonderzeichen, zu große Zahlen, usw. eingegeben. Das Programm erneuert solange seine Frage, bis eine gültige Antwort eingegeben wird.

        Ebenso wurden in die Abfrage, ob der Spieler noch einmal würfeln will oder nicht etwaige falsche Antworten getippt. Auch hier lässt sich das Programm nicht beirren, bis es die richtige Antwort erhält.

        Die Frage nach den zu behaltenden Würfeln wurde ebenfalls getestet. Erhält das Programm eine andere Eingabe als eine Kombination aus gewürfelten Augenzahlen und Kommas akzeptiert es diese nicht und verlangt eine neue korrekte Eingabe.

        Wenn ein Spieler gefragt wird ob er alle 5 Würfel behalten und seinen Zug beenden möchte oder nicht. Lässt das Programm ebenfalls nur die gewünschten Antworten zu. Alle anderen Eingaben bewirken eine erneute Abfrage.

        Soll der Spieler entscheiden, wo er seine Punkte eintragen möchte so lässt das Programm nur Antworten in Form von Zahlen im Bereich von 1 bis 13 zu. Alles andere wird blockiert.
        Außerdem überprüft das Programm hierbei ob der vom Spieler gewürfelte Wert überhaupt in die gewünschte Zeile eingetragen werden kann. Falscheingaben sind daher nicht möglich.

        Muss ein Spieler eine Zeile mit der Zahl 0 beschreiben (streichen). Sind wieder nur ja oder nein gültig. Sonderzeichen, mit Leertaste unterbrochene Antworten, Zahlen, usw. werden nicht akzeptiert

        