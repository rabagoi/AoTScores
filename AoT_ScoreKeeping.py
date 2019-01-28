'''
This Python script writes an HTML file to display
the scores for Astronomy on Tap. The number of
questions per round can be adjusted.

During the event, each team gets its own array in the
scores variable. Once the scores are filled in, the
script fills in the appropriate HTML table, which can
be displayed with a web browser.
'''

Nq = 5                      # Number of questions in a round
roundlength = 2*(Nq+1)      # Length of a round, including labels
indent = ' '*2              # Size of the indent

# Team names and scores. Fill in with teams and scores from each event.
scores= [
        ["Team 1",
            30, 30, 40, 50, 10, 75, 80, 80, 100, 60, 40, -500],

        ["Team &Sigma;<sub>n=0</sub> 1/2<sup>n</sup>",
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

        ["Team &pi;, Basically",
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

        ["Team 2<sup>2</sup>",
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

        ["Team V",
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]


# Add the HTML header.
def Header():
    data.write("<!DOCTYPE html>\n")
    data.write("<html>\n")
    data.write("<head>\n")
    data.write(indent+"<meta charset=\"utf-8\" />\n")
    data.write(indent+"<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n")
    data.write(indent+"<title>Astronomy on Tap Scoreboard (TEST)</title>\n")
    data.write(indent+"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n")
    data.write(indent+"<link rel=\"stylesheet\" type=\"text/css\" media=\"screen\" href=\"main.css\" />\n")
    data.write(indent+"<script src=\"main.js\"></script>\n")
    data.write("</head>\n")


# Write the HTML script.
with open("index.html", 'w') as data:
    Header()

    #Set background and text colors, font
    data.write("<body style=\"background-color:black; color:gold; font-family:Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif\">\n")
    data.write(indent+"<h1 style=\"font-size:60px; text-align:center\">Astronomy on Tap Scoreboard</h1>\n")
    data.write(indent+"<hr>\n")
    data.write(indent+"<table style=\"table-layout:fixed; width:100%; text-align:center; border-spacing:0px; font-size:larger\">\n")
    #Fill in the data cells of the table
    for i in range(len(scores[0])+2):

        # Strings for the opening tags, table row, and closing tags.
        ot = 2*indent+"<tr>\n"
        row = 3*indent
        ct = '\n'+2*indent+"</tr>\n"

        # Variable to set the question number, set to i%(1+N_questions).
        # Change this if the number of questions per round is different.
        qnum = i%6
        qlabel = "Question"+(" #"+str(qnum) if i!=0 else '')

        # Add special labels for the halftime and final questions.=
        if i == 0:
            ot = ot.replace("<tr>", "<tr style=\"font-size:larger; font-weight:bolder\">")
        if i == roundlength/2:
            qlabel = "Halftime"
            ot = ot.replace("<tr>", "<tr style=\"font-weight:bolder; background-color:dimgray\">")
        elif i == roundlength:
            qlabel = "Final"
            ot = ot.replace("<tr>", "<tr style=\"font-weight:bolder; background-color:dimgray\">")
        elif i == roundlength+1:
            qlabel = "Halftime Totals"
            ot = ot.replace("<tr>", "<tr style=\"font-weight:bolder; font-size:x-large\">")
            ot = 2*indent+"<tr><td><br></td></tr>\n" + ot
        elif i == roundlength+2:
            qlabel = "Final Scores"
            ot = ot.replace("<tr>", "<tr style=\"font-weight:bolder; font-size:x-large\">")

        # Add question number
        ot += 3*indent+"<td>"+qlabel+"</td>\n"
        # Write the scores for each round.
        for j in range(len(scores)):
            if i <= roundlength:
                row += "<td>"+str(scores[j][i])+"</td>"
            elif i == roundlength+1:
                row += "<td>"+str(sum(scores[j][1:Nq+2]))+"</td>"
            elif i == roundlength+2:
                row += "<td>"+str(sum(scores[j][1:]))+"</td>"

        data.write(ot+row+ct)

    data.write(indent+"</table>\n")
    data.write("</body>\n")
    data.write("</html>")