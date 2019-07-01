"""Python Homework #2 - Functions"""

import functions

#Name of the song
sSongName = "Am I Wrong"
#Type of the song
sGenere = "Pop"
#Release date
sReleasedDate = "April 12, 2013"
#Album
sAlbum = "Black Star Elephant"
#Singer
sArtist = "Nico & Vinz"
#Producer
sProducers = "William Wiik Larsen"
#Length of the song in mintues
nDuration = 4.07

# Print details
print("Song\t\t: \t"+sSongName)
print("Genere\t\t: \t"+sGenere)
print("Released Date\t: \t"+sReleasedDate)
print("Album\t\t: \t"+sAlbum)
print("Video Available : "+str(functions.VideoAvailable(functions.url())))
print("Video Url\t\t: \t"+functions.url())
print("Artist\t\t: \t"+sArtist)
functions.composers()
print("Producer(s)\t: \t"+sProducers)
print("Duration(mins)\t: \t"+str(nDuration))
functions.nominations()
