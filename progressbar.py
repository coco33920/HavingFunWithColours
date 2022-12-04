import time
import os
class Progressbar: 
    """ 
        Simple class to emulate progress bar in standard out
        @params: 
            title: name of the progress bar (displayed first)
            total: number of jobs to be executed
            length: default 60, length of the progress bar
            char: default '#' character used to display the progress
    """
    def __init__(self,title,total,length=60,char="#"):
        self.title = title
        self.total = total
        self.started = time.time()
        self.length = self.compute_ideal_length()
        self.char = char
    
    @staticmethod
    def time_display(second):
        return time.strftime("%H:%M:%S", time.gmtime(second))

    def pretty_time_display(self):
        return self.time_display(time.time() - self.started)
    

    def compute_eta(self,current):
        """Compute the ETA to finish the jobs based on the current time and progress"""
        elapsed = (time.time() - self.started)
        total = int((float(self.total)*float(elapsed))/float(current)) #produit en croix
        return total-elapsed #temps restant

    def compute_ideal_length(self):
        """Compute the ideal length of the bar based on the width of the terminal"""
        width = os.get_terminal_size()[0] #total width
        number = len(str(self.total))*2 + 6 #width used by the progress display (XXX/XXX) 
        title_width = 15 #width of the title
        end_width = 36 #width used by the XXX% and time elapsed/ETA display and the blank after the |
        remaining_size = width - (number+title_width+end_width)
        return remaining_size


    def update(self,current):
        """Updates the progress of the bar"""
        current = current + 1 #on va de 0 à total-1 sinon...
        self.length = self.compute_ideal_length() #au cas où l'envie de réduire le terminal vienne à l'idée...
        progress = (float(current)/float(self.total)) #proportion
        inner = self.char*int(((progress)*(self.length))) #nombre de caractère à afficher
        space = ' '*int((self.length-len(inner))) #reste rempli avec des espaces
       
        title_padding =' '*(15-len(self.title)) #padding après le titre pour rester aligner

        progress_padding = ' '*(len(str(self.total))-len(str(current))) #padding avant le nombre pour rester aligner quand on passe de 0 à 10 à 100 etc.
        percent_padding = 1 #padding avant le pourcentage

        if progress < 0.1:
            percent_padding = 2

        if current == self.total:
            percent_padding = 0

        percent_padding = ' '*percent_padding
        eta = self.time_display(self.compute_eta(current))

        print("%s%s %s(%d / %d) |%s%s| %s%d%% Durée %s ETA %s" % (
            self.title,
            title_padding,
            progress_padding,
            current,
            self.total,
            inner,
            space,
            percent_padding,
            progress*100,
            self.pretty_time_display(),
            eta), end='\r')
